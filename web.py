from flask import Flask, jsonify, send_file, Response
from pymongo import MongoClient
import gridfs
from gridfs import GridFS
from flask_cors import CORS
from bson import ObjectId
from io import BytesIO
import mimetypes

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client['admin']
fs = gridfs.GridFS(db)

@app.route('/admin', methods=['GET'])
def get_admin():
    admins = db['admin'].find()
    result = []
    for admin in admins:
        admin['_id'] = str(admin['_id'])
        result.append(admin)
    return jsonify(result)

@app.route('/bicycles', methods=['GET'])
def get_bicycles():
    bicycles = db['bicycles'].find()
    result = []
    for bicycle in bicycles:
        bicycle['_id'] = str(bicycle['_id'])
        result.append(bicycle)
    return jsonify(result)

@app.route('/users', methods=['GET'])
def get_users():
    users = db['users'].find()  # users 컬렉션에서 데이터 조회
    result = []
    for user in users:
        user['_id'] = str(user['_id'])
        result.append(user)
        #user_data = {
            #'userID': user.get('userId'),  # userID 필드만 추출
            #'password': user.get('password') # password 필드만 추출
        #}
        #result.append(user_data)
    return jsonify(result)

@app.route('/reports', methods=['GET'])
def get_reports():
    reports = db.reports.find()
    result = []
    for report in reports:
        result.append({
            "id": str(report["_id"]),
            "bikeId": report["bikeId"],
            "userId": report["userId"],
            "date": report["date"],
            "category": report["category"],
            "contents": report["contents"],
            "imageId": str(report["imageId"]) if "imageId" in report else None,
        })
    return jsonify(result)


@app.route('/reports/image/<image_id>', methods=['GET'])
def get_image(image_id):
    try:
        # GridFS에서 파일 메타데이터 가져오기
        file = db['fs.files'].find_one({"_id": ObjectId(image_id)})
        if not file:
            return jsonify({"error": "Image not found"}), 404

        # 파일 데이터 조합
        chunks = db['fs.chunks'].find({'files_id': ObjectId(image_id)}).sort('n', 1)
        file_data = b''.join(chunk['data'] for chunk in chunks)

        # MIME 타입 추정
        filename = file.get("filename", "")
        mime_type, _ = mimetypes.guess_type(filename)
        if not mime_type:
            mime_type = "application/octet-stream"

        return send_file(BytesIO(file_data), mimetype=mime_type)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# /files/<file_id> API - GridFS에서 이미지 파일 제공
@app.route('/files/<file_id>', methods=['GET'])
def get_file(file_id):
    # GridFS에서 파일 메타데이터를 가져옴
    file = db['fs.files'].find_one({'_id': ObjectId(file_id)})
    if file:
        # 파일의 chunk 데이터를 결합하여 반환
        chunks = db['fs.chunks'].find({'files_id': file['_id']}).sort('n', 1)
        file_data = b''.join([chunk['data'] for chunk in chunks])
        return file_data, 200
    else:
        return jsonify({'error': 'File not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)