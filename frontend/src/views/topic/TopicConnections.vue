<template>
  <div class="overflow-auto" style="height: 200px;">
    <!-- 假设有很多内容使得容器可滚动 -->
    <div style="height: 600px;"></div>
    <!-- 目标元素 -->
    <div ref="card" style="height: 100px; background: #ddd;">滚动到这里</div>
    <!-- 更多内容 -->
    <div style="height: 600px;"></div>
  </div>
  <button @click="scrollToCard">滚动到卡片</button>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const card = ref();

const scrollToCard = () => {
  if (card.value) {
    card.value.scrollIntoView({ behavior: 'smooth' });
  }
};

// 使用 onMounted 确保在组件挂载后再访问 ref
onMounted(() => {
  // 可以在这里进行一些组件挂载后的操作，如果需要
});
</script>

<style scoped>
.overflow-auto {
  overflow: auto;
}
</style>
