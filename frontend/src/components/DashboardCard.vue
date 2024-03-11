<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const props = defineProps({
  ready: Number,
  title: String,
  section: String,
  content: String,
  link: String,
  paperId: Number,
})

const getReadyIcon = () => {
  switch (props.ready) {
    case -1:
      return 'block';
    case 0:
      return 'loop';
    case 1:
      return 'check';
  }
}

const getReadyStripe = () => {
  switch (props.ready) {
    case -1:
      return 'danger';
    case 0:
      return 'info';
    case 1:
      return 'success';
  }
}

const handleClick = (link) => {
  if (link) {
    return props.paperId ? router.push({ path: link, query: { paperId: props.paperId } }) : router.push(link);
  }
}

</script>

<template>
  <VaCard
      class="flex min-h-32 cursor-pointer relative"
      :stripe="ready !== 0"
      :stripe-color="getReadyStripe()"
      @click="handleClick(link)"
  >
    <VaProgressBar v-if="ready === 0" class="absolute top-0" :size="5" indeterminate />
    <div>
      <VaCardTitle>
        <div>
          <p class="font-black text-lg">{{ title }}</p>
          <p class="text-gray-400">{{ section }}</p>
        </div>
      </VaCardTitle>
      <VaCardContent class="break-words overflow-hidden">
        <p class="text-gray-500">{{ content }}</p>
      </VaCardContent>
    </div>

    <div class="flex items-center justify-end text-end mr-4">
      <VaIcon class="icon w-auto" size="4rem" :name="getReadyIcon()" />
    </div>
  </VaCard>
</template>

<style scoped>
.icon {
  width: 4rem;
}
</style>
