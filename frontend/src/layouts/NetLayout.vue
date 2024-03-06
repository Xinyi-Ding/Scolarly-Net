<script setup>

</script>

<template>
  <div class="flex gap-2 h-full">
    <div class="w-1/3 min-w-[300px] flex-none shadow-xl overflow-auto">
      <slot name="list"></slot>
    </div>
    <div class="flex-auto">
      <slot name="graph"></slot>
    </div>
  </div>
</template>

<style scoped>

</style>
