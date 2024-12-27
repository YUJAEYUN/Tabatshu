<template>
    <div class="home">
        <header>
            <div class="header-left">
                <img src="/logo.png" alt="Logo" />
            </div>
            <div class="header-right">
                <div class="admin-info">
                    <img src="/admin-photo.png" alt="Admin" class="admin-photo" />
                    <span class="admin-id">Admin123</span>
                </div>
            </div>
        </header>
  
        <div class="content">
            <nav>
                <button
                    v-for="button in buttons"
                    :key="button.page"
                    @click="goToPage(button.page)"
                    :class="{ active: activePage === button.page }"
                >
                    {{ button.label }}
                </button>
            </nav>


            <main>
                <router-view></router-view> <!-- 이곳에 각 페이지가 표시됩니다. -->
            </main>
        </div>
    </div>
</template>
    
<script>
export default {
    data() {
        return {
            activePage: 'bicycles', // 초기 활성화된 페이지
            buttons: [
                { label: 'Bicycles Data', page: 'bicycles' },
                { label: 'Reports Data', page: 'reports' },
                { label: 'Users Data', page: 'users' },
            ],
        };
    },
    methods: {
        goToPage(page) {
            this.activePage = page; // 활성화된 버튼 업데이트
            this.$router.push({ name: page }); // 라우터를 이용해 페이지 이동
        },
    },
};
</script>

<style scoped>
header {
    position: sticky;   /* 화면 상단에 고정 */
    top: 0;             /* 스크롤 시에도 상단 고정 */
    z-index: 10;        /* 다른 요소 위에 표시 */
    background-color: #fcd2a2;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.header-left {
    display: flex;
    align-items: center;
}

.header-left img {
    width: 140px;
    height: auto;
}

.header-right {
    display: flex;
    align-items: center; /* 세로 중앙 정렬 */
}

.admin-info {
    display: flex;
    align-items: center; /* 내부 요소를 세로 중앙 정렬 */
}

.admin-photo {
    width: 50px;
    height: 50px;
    border-radius: 50%; /* 동그랗게 */
    margin-right: 15px; /* 사진과 텍스트 사이 간격 */
}

.admin-id {
    font-size: 20px;
    color: #ffffff;
}

.content {
    display: flex;
    flex: 1;
}

/* 사이드바 */
    nav {
    width: 250px;
    background-color: #fce9cf;
    display: flex;
    flex-direction: column;
    padding: 20px;
    box-sizing: border-box;
    position: sticky; /* 스크롤 시 고정 */
    top: 0; /* 화면의 최상단에 고정 */
    height: calc(100vh - 80px); /* 화면 전체 높이에서 header 높이를 제외 */
    overflow-y: auto; /* 스크롤이 생길 경우 스크롤 가능 */
}

/* 사이드바 버튼 */
nav button {
    padding: 20px 13px;
    font-size: 18px;
    margin-bottom: 20px;
    border: none;
    background-color: #f5a55b;
    color: #ffffff;
    text-align: left;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s;
    text-align: center;
}

/* 활성화된 버튼 스타일 */
nav button.active {
    background-color: #fad66c;
    color: #ffffff;
    font-weight: bold;
    border: 2px solid #fad66c;
}

nav button:hover {
    background-color: #fad66c;
}


@keyframes fadeInOut {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  10% {
    opacity: 1;
    transform: translateY(0);
  }
  90% {
    opacity: 1;
    transform: translateY(0);
  }
  100% {
    opacity: 0;
    transform: translateY(20px);
  }
}

/* 메인 콘텐츠 영역 */
main {
    flex-grow: 1;
    padding: 0 20px 20px; /* 상단 공백 제거, 양옆과 아래만 여백 */
    background-color: #fff;
    overflow-y: auto;
}
</style>