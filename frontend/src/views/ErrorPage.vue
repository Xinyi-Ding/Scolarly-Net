<script setup>
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const route = useRoute();
const message = route.query.msg;
console.log('message', message);

const handleBack = () => {
  router.push('/');
};
</script>

<template>
  <div class="m-auto w-1/2 h-[100vh] flex justify-center items-center">
    <VaAlert
        class="w-1/2"
        color="warning"
        icon="favorite"
        closeable
        center
    >
      <template #title>
        <h1 class="text-2xl font-bold mt-2">Oops!</h1>
      </template>
      <template #default>
        <div class="my-3">
          Something went wrong. Please try again later.
          {{ message }}
        </div>
      </template>
      <template #close>
        <VaButton
            icon-right="arrow_forward"
            @click="handleBack"
        >
          Back
        </VaButton>
      </template>
    </VaAlert>
  </div>
</template>

<style scoped>

</style>
