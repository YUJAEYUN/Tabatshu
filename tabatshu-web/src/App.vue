<template>
  <div id="app">
    <!-- 로그인 상태에 따라 로그인 페이지 또는 메인 페이지를 보여줌 -->
    <Login v-if="!isLoggedin" @login="handleLogin"></Login>
    <Home v-else>
      <!-- Main 내부에서 vue-router를 사용하여 다른 페이지로 이동 -->
      <router-view></router-view> <!-- 현재 활성화된 페이지가 여기에 표시됩니다. -->
    </Home>
  </div>
</template>

<script>
import Login from './components/LoginPage.vue'
import Home from './components/HomePage.vue'

export default {
  name: 'App',
  components: {
    Login,
    Home,
  },
  data() {
    return {
      isLoggedin: false,    // 로그인 상태를 추적
    };
  },
  methods: {
    handleLogin() {    // 로그인 성공 시 호출되는 메서드
      this.isLoggedin = true;
    },
  },
};
</script>