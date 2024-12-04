import time
from pymongo import MongoClient
from plyer import notification

# MongoDB 연결
client = MongoClient('mongodb://localhost:27017/')
db = client['admin']  # 데이터베이스 이름
collection = db['reports']  # 컬렉션 이름

last_id = None
POLL_INTERVAL = 10  # 폴링 간격 (초)

print("MongoDB 감시를 시작합니다...")

while True:
    try:
        # MongoDB에서 데이터 확인
        latest_data = collection.find_one(sort=[('_id', -1)])  # 가장 최근 데이터 가져오기
        if latest_data and (last_id is None or latest_data['_id'] != last_id):
            last_id = latest_data['_id']
            # 알림 표시
            notification.notify(
                title="신고 데이터 접수",
                message="빠른 확인 및 조치 바랍니다",
                timeout=5  # 알림 표시 시간 (초)
            )
            print("새로운 데이터가 추가되었습니다.")
    except Exception as e:
        print(f"에러 발생: {e}")

    time.sleep(POLL_INTERVAL)