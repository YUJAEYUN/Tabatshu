# 자전거 대여 및 신고 관리 시스템

이 프로젝트는 Flask와 MongoDB를 기반으로 구축된 다기능 웹 및 모바일 애플리케이션 백엔드입니다. 자전거 대여, 사용자 인증, 신고 접수 및 실시간 데이터 업데이트를 관리합니다. 아래는 프로젝트의 주요 기능과 설명입니다.

---

## 주요 기능

### 1. 사용자 인증
- **관리자 로그인:**
  - `adminId`와 비밀번호를 확인합니다.
  - 로그인 성공 시 관리자 역할을 반환합니다.

- **사용자 로그인:**
  - `userId`와 비밀번호를 확인합니다.
  - 로그인 성공 시 사용자의 대여 가능 상태(`tf_rent`)를 업데이트합니다.
    
### 2. 자전거 대여 관리

- **자전거 대여:**
  - 사용자는 대여 가능 상태(`tf_rent`가 `true`)이고 자전거가 사용 가능한 경우 대여할 수 있습니다.
  - 대여 후 자전거 상태는 `unavailable`로 변경되며, 사용자의 대여 가능 상태는 `false`로 설정됩니다.

- **자전거 반납:**
  - 사용자는 대여한 자전거를 반납할 수 있습니다.
  - 반납 후 자전거 상태는 `available`로 변경되며, 사용자의 대여 가능 상태는 `true`로 설정됩니다.

- **자전거 상태 확인:**
  - QR 코드를 통해 자전거의 상태를 확인합니다.
  - 사용 가능 여부를 응답으로 반환합니다.
### 3. 신고 관리

- **신고 접수:**
  - 사용자는 자전거 관련 문제를 신고할 수 있습니다.
  - 신고 내용에는 자전거 ID, 사용자 ID, 카테고리, 내용, 선택적 이미지 업로드가 포함됩니다.
  - 신고 데이터는 MongoDB에 저장되며, 이미지는 GridFS를 통해 관리됩니다.

- **신고 조회:**
  - 관리자는 모든 신고 내용을 확인할 수 있습니다.
  - 신고에는 자전거 ID, 사용자 ID, 날짜, 카테고리, 내용 및 관련 이미지 링크가 포함됩니다.

---

### 4. 실시간 알림

- **데스크톱 알림:**
  - Python 스크립트가 MongoDB 컬렉션을 모니터링하며, 새로운 신고가 추가될 때 데스크톱 알림을 전송합니다.
### 5. 데이터 관리 API

- **관리자 데이터 조회:**
  - MongoDB에서 모든 관리자 데이터를 가져옵니다.

- **사용자 데이터 조회:**
  - 모든 사용자 데이터를 가져오며, 사용자 ID와 대여 상태를 포함합니다.

- **자전거 데이터 조회:**
  - 자전거 ID와 현재 상태(`available` / `unavailable`)를 가져옵니다.

- **신고 데이터 조회:**
  - 모든 신고 데이터를 가져오며, GridFS에 저장된 이미지를 포함합니다.

- **이미지 조회:**
  - `imageId`를 사용하여 GridFS에서 이미지를 가져옵니다.