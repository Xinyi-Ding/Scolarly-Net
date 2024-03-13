<script setup>
defineProps({
  author: {
    type: Object,
    required: true,
  },
});
</script>

<template>
  <VaPopover class="mr-2 mb-2">
    <template #icon>
      <VaIcon name="account_circle" size="large"/>
    </template>
    <template #title>
      <p class="mb-1">{{ author.name }}</p>
    </template>
    <template #body>
      <div v-if="author.email" class=" flex items-center justify-start text-sm">
        <VaIcon class="mr-1" name="mail" size="small"/>
        {{ author.email }}
      </div>
      <div v-if="author.affiliation" class="flex items-center justify-start text-sm">
        <VaIcon class="mr-1" name="apartment" size="small"/>
        {{ author.affiliation }}
      </div>
    </template>

    <VaChip class="mr-1 pa-0" icon="person" size="small" flat>
      {{ author.name }}
    </VaChip>
  </VaPopover>
</template>

