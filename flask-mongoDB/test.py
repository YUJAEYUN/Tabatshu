from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB 연결
client = MongoClient('mongodb://localhost:27017/')
db = client['test']  # db 이름

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    result = db.firstcol.insert_one(data)
    return jsonify({'id': str(result.inserted_id)}), 201

@app.route('/data', methods=['GET'])
def get_data():
    data = list(db.firstcol.find({}, {'_id': 0}).pretty())  # _id 제외
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
