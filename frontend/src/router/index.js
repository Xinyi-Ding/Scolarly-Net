import { createRouter, createWebHistory } from 'vue-router';
import { routesConfig } from '../lib/routesConfig';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // {
    //   path: '/',
    //   redirect: '/dashboard'
    // },
    {
      path: '/',
      redirect: '/dashboard',
      component: () => import('../layouts/BaseLayout.vue'),
      children: routesConfig
    },
    {
      path: '/error',
      component: () => import('../views/ErrorPage.vue')
    }
  ]
});

export default router;
