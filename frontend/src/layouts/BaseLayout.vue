<script setup>
import { ref, watch } from "vue";
import { routesConfig } from "@/lib/routesConfig.js";
import { useRouter } from "vue-router";

const router = useRouter();
const header = ref('Null');
const accordionValue = ref(new Array(routesConfig.length).fill(true));
const activeElement = ref(null);
const activeRouteName = ref('');

const minimized = ref(false);
if (localStorage.getItem('minimized') === 'true') {
  minimized.value = true;
}

function generateActive() {
  if (router.currentRoute.value.matched.length > 2) {
    const parent = router.currentRoute.value.matched[1].name;
    const child = router.currentRoute.value.matched[2].name;
    const parentIndex = routesConfig.findIndex((route) => route.name === parent);
    accordionValue.value[parentIndex] = true;
    activeRouteName.value = child;
  } else {
    activeRouteName.value = router.currentRoute.value.matched[1].name;
  }

}

function isRouteActive(route) {
  return route.name === activeRouteName.value;
}

function setRouteActive(route) {
  if (route.children) return;
  activeRouteName.value = route.name;
  window.scrollTo(0, 0);
  router.push(route.path);
}

function toggleSidebar() {
  minimized.value = !minimized.value;
  localStorage.setItem('minimized', minimized.value.toString());
}

watch(() => router.currentRoute.value, (newRoute) => {
  const matchedRoute = newRoute.matched.slice().reverse().find(r => r.meta && r.meta.title);
  if (matchedRoute && matchedRoute.meta && matchedRoute.meta.title) {
    header.value = matchedRoute.meta.title;
  }
  generateActive();
}, { immediate: true });


</script>

<template>
  <VaLayout
      :left="{ fixed: true, order: 2 }"
      :top="{ fixed: true, order: 1 }"
  >
    <template #top>
      <VaNavbar
          class="h-[58px] py-2"
          shadowed
      >
        <template #left>
          <VaNavbarItem>
            <VaButton
                :icon="minimized ? 'menu' : 'menu_open'"
                @click="toggleSidebar"
            />
          </VaNavbarItem>
          <VaNavbarItem>
            <p class="font-black text-xl">SCHOLARLY NET</p>
          </VaNavbarItem>

        </template>
        <template #right>
          <VaNavbarItem>
            <VaAvatar
                size="small"
                class="mr-2 rounded"
                square
            >
              A
            </VaAvatar>
          </VaNavbarItem>
        </template>

      </VaNavbar>
    </template>

    <template #left>
      <VaSidebar
          :minimized="minimized"
          minimized-width="80px"
      >
        <VaAccordion
            v-model="accordionValue"
            multiple
        >
          <VaCollapse
              v-for="(route, idx) in routesConfig"
              :key="idx"
              body-color="#fff"
          >
            <template #header>
              <VaSidebarItem
                  :active="isRouteActive(route)"
                  @click="setRouteActive(route)"
              >
                <VaSidebarItemContent>
                  <VaIcon :name="route.icon" />
                  <VaSidebarItemTitle>
                    {{ route.meta.title }}
                  </VaSidebarItemTitle>
                  <VaIcon
                      v-if="route.children"
                      :name="accordionValue[idx] ? 'expand_less' : 'expand_more'"
                  />
                </VaSidebarItemContent>
              </VaSidebarItem>
            </template>
            <template #body>
              <VaSidebarItem
                  v-for="(child, index) in route.children"
                  :key="index"
                  :active="isRouteActive(child)"
                  @click="setRouteActive(child)"
              >
                <VaSidebarItemContent class="ml-3 overflow-hidden">
                  <VaIcon :name="child.icon" />
                  <VaSidebarItemTitle>
                    {{ child.meta.title }}
                  </VaSidebarItemTitle>
                </VaSidebarItemContent>
              </VaSidebarItem>
            </template>
          </VaCollapse>
        </VaAccordion>

        <VaSpacer />

        <VaSidebarItem
            :active="'Settings' === activeElement"
            @click="console.log('Settings coming soon...')"
        >
          <VaSidebarItemContent>
            <VaIcon name="settings" />
            <VaSidebarItemTitle>Settings</VaSidebarItemTitle>
          </VaSidebarItemContent>
        </VaSidebarItem>
      </VaSidebar>
    </template>

    <template #content>
      <main class="p-4">
        <h1 class="text-3xl font-black ml-2 mb-3 uppercase">{{header}}</h1>
        <div class="h-[80vh] bg-white shadow-lg overflow-auto">
          <router-view v-slot="{ Component }">
            <keep-alive>
              <component :is="Component" />
            </keep-alive>
          </router-view>
          <!--without keep-alive-->
          <!--<RouterView />-->
        </div>
      </main>
    </template>
  </VaLayout>

</template>

<style scoped>
</style>
