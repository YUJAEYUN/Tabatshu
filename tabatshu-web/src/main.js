import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

const app = createApp(App);

// Axios 설정
app.config.globalProperties.$axios = axios.create({
  baseURL: 'http://localhost:5000', // Flask 서버 주소
});

app.use(router);
app.mount('#app');
