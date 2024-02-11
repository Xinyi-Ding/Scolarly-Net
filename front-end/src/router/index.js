import { createRouter, createWebHistory } from 'vue-router';
import { routesConfig } from '../lib/routesConfig';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'base-layout',
      component: () => import('../layouts/BaseLayout.vue'),
      children: routesConfig
    }
  ]
});

export default router;
