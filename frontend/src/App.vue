<template>
  <el-config-provider namespace="ep">
    <BaseHeader />
    <div class="flex main-container">
      <BaseSide />
    </div>
  </el-config-provider>
</template>

<style>
#app {

}

.main-container {
  /*height: calc(100vh - var(--ep-menu-item-height) - 3px);*/
  height: 100vh;
}
</style>
