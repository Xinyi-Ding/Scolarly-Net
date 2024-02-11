<script setup>
import { ref } from "vue";
import { routesConfig } from "@/lib/routesConfig.js";
import { useRouter } from "vue-router";

const minimized = ref(false);

const activeElement = ref(null);

const router = useRouter();

const activeRouteName = ref('');
const accordionValue = ref(new Array(routesConfig.length).fill(false));
if (router.currentRoute.value.matched.length > 1) {
  const parent = router.currentRoute.value.matched[1].name;
  const child = router.currentRoute.value.matched[2].name;
  const parentIndex = routesConfig.findIndex((route) => route.name === parent);
  accordionValue.value[parentIndex] = true;
  activeRouteName.value = child;
}

function isRouteActive(route) {
  return route.name === activeRouteName.value;
}

function setRouteActive(route) {
  if (route.children) return;
  activeRouteName.value = route.name;
  router.push(route.path);
}

</script>

<template>
  <VaLayout
      :left="{ fixed: true, order: 2 }"
      :top="{ fixed: true, order: 1 }"
  >
    <template #top>
      <VaNavbar
          class="min-h-14 py-2"
          shadowed
      >
        <template #left>
          <VaNavbarItem>
            <VaButton
                :icon="minimized ? 'menu' : 'menu_open'"
                @click="minimized = !minimized"
            />
          </VaNavbarItem>
          <VaNavbarItem>
            <p class="font-black text-xl">SCHOLARLY NET</p>
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
                    {{ route.title }}
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
                <VaSidebarItemContent class="ml-3">
                  <VaIcon :name="child.icon" />
                  <VaSidebarItemTitle>
                    {{ child.title }}
                  </VaSidebarItemTitle>
                </VaSidebarItemContent>
              </VaSidebarItem>
            </template>
          </VaCollapse>
        </VaAccordion>


        <!--<VaAccordion>-->
        <!--  <template v-for="item in routesConfig">-->
        <!--    <VaCollapse-->
        <!--        v-if="item.children"-->
        <!--        :key="item.title + 'collapse'"-->
        <!--        body-color="#00000022"-->
        <!--    >-->
        <!--      <template #header="{ value: isCollapsed }">-->
        <!--        <VaSidebarItem :active="item.children.some((child) => child.title === activeElement)">-->
        <!--          <VaSidebarItemContent>-->
        <!--            <VaIcon :name="item.icon" />-->
        <!--            <VaSidebarItemTitle>{{ item.title }}</VaSidebarItemTitle>-->
        <!--            <VaSpacer />-->
        <!--            <VaIcon :name="isCollapsed ? 'va-arrow-up' : 'va-arrow-down'" />-->
        <!--          </VaSidebarItemContent>-->
        <!--        </VaSidebarItem>-->
        <!--      </template>-->

        <!--      <template #body>-->
        <!--        <VaSidebarItem-->
        <!--            v-for="child in item.children"-->
        <!--            :key="child.title"-->
        <!--            :active="child.title === activeElement"-->
        <!--            @click="router.push(child.path); activeElement = child.title"-->
        <!--        >-->
        <!--          <VaSidebarItemContent>-->
        <!--            <VaIcon :name="child.icon" />-->
        <!--            <VaSidebarItemTitle>{{ child.title }}</VaSidebarItemTitle>-->
        <!--          </VaSidebarItemContent>-->
        <!--        </VaSidebarItem>-->
        <!--      </template>-->
        <!--    </VaCollapse>-->

        <!--    <VaSidebarItem-->
        <!--        v-else-->
        <!--        :key="item.title + 'item'"-->
        <!--        :active="item.title === activeElement"-->
        <!--        @click="router.push(item.path); activeElement = item.title"-->
        <!--    >-->
        <!--      <VaSidebarItemContent>-->
        <!--        <VaIcon :name="item.icon" />-->
        <!--        <VaSidebarItemTitle>{{ item.title }}</VaSidebarItemTitle>-->
        <!--      </VaSidebarItemContent>-->
        <!--    </VaSidebarItem>-->
        <!--  </template>-->
        <!--</VaAccordion>-->

        <VaSpacer />

        <VaSidebarItem
            :active="'Settings' === activeElement"
            @click="console.log('Settings')"
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
        <RouterView />
      </main>
    </template>
  </VaLayout>

</template>

<style scoped>
.expanded {
  background-color: var(--va-background-primary);
}
</style>
