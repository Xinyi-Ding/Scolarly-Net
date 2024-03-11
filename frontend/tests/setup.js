// setup.js
import { config } from '@vue/test-utils';
import { createRouter, createWebHistory } from 'vue-router';
import { routesConfig } from '@/lib/routesConfig';
import { createVuestic } from 'vuestic-ui'

// Configure the router
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/dashboard',
      component: () => import('@/layouts/BaseLayout.vue'),
      children: routesConfig,
    },
  ],
});

export function setupRouter() {
  router.push('/').then(); // Navigate to initial route if needed
  return router;
}

// Use the router with Vue Test Utils
config.global.plugins.push([router]);
config.global.plugins.push(createVuestic({}))
