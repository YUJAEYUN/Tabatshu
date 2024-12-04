<template>
    <header>
        <div class="header-left">
            <img src="/logo.png" alt="Logo" />
        </div>
    </header>
    <div class="login-container">
        <div class="login-box">
            <h1>Login</h1>
            <form @submit.prevent="login">
                <div class="form-group">
                    <label for="adminname">Admin Name</label>
                    <input v-model="adminname" id="adminname" type="text" required />
                </div>
                <div class="form-group">
                    <label for="password">Password</label>
                    <input v-model="password" id="password" type="password" required />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    </div>
</template>
  
<script>
export default {
    name: 'LoginPage',
    data() {
        return {
            adminname: '',   // 관리자의 이름을 저장
            password: '',    // 비밀번호를 저장
        };
    },
    methods: {
        login() {
            // 로그인 로직 (아이디와 비밀번호 확인)
            if (this.adminname === 'admin123' && this.password === '1234') {
                this.$emit('login');  // 로그인 성공 시 부모에게 'login' 이벤트를 전달
            } else {
                alert('아이디 또는 비밀번호가 잘못되었습니다.');
            }
        },
    },
};
</script>
  
<style scoped>
/* 상단 헤더 */
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

.login-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: calc(100vh - 115px); /* 100vh에서 헤더 높이를 제외 */
    background-color: #f9f2e8;
}
  
.login-box {
    width: 400px;
    height: 50%;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
  
h1 {
    font-size: 30px;
    margin-bottom: 45px;
    color: #f5a55b;
    text-align: center;  /* h1 텍스트를 가로 가운데로 정렬 */
}

label {
    font-size: 20px;
    color: #f5a55b;
}

input {
    margin: 15px 0;
    margin-bottom: 25px;
    padding: 10px;
    width: 100%;
    max-width: 400px;
    box-sizing: border-box;
    border-radius: 5px;
    border: 1px solid #ccc;
    font-size: 15px;
}
  
button {
    margin-top: 40px;
    padding: 15px;
    background-color: #f5a55b;
    border: none;
    color: #fff;
    cursor: pointer;
    border-radius: 5px;
    width: 100%;
    max-width: 400px;
    font-size: 18px;
}
  
button:hover {
    background-color: #fad66c;
}
</style>