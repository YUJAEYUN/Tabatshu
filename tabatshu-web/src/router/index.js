import { createRouter, createWebHistory } from 'vue-router';
//import AdminPage from '../components/AdminPage.vue';
import BicyclesPage from '../components/BicyclesPage.vue';
import HomePage from '../components/HomePage.vue'; // HomePage 추가
import LoginPage from '../components/LoginPage.vue'; // LoginPage 추가
import ReportsPage from '../components/ReportsPage.vue'; // ReportsPage 추가
import UsersPage from '../components/UsersPage.vue'; // UsersPage 추가

const routes = [
  { path: '/', redirect: '/bicycles' },
  { path: '/bicycles', name: 'bicycles', component: BicyclesPage },
  { path: '/home', name: 'home', component: HomePage },
  { path: '/login', name: 'login', component: LoginPage },
  { path: '/reports', name: 'reports', component: ReportsPage },
  { path: '/users', name: 'users', component: UsersPage },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
