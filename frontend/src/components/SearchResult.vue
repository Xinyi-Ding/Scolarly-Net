<script setup>
defineProps({
  modelValue: Boolean,
  search: String,
  searchResults: Array
});

const emit = defineEmits(['update:modelValue', 'select']);

const updateModelValue = (value) => {
  emit('update:modelValue', value);
};

const selectResult = (id) => {
  emit('select', id);
  updateModelValue(false); // close modal
};

const handleClose = () => {
  updateModelValue(false);
};
</script>

<template>
  <VaModal
      :model-value="modelValue"
      class="my-0 border-solid border"
      max-height="600px"
      hide-default-actions
      fixed-layout
      blur
      @update:model-value="updateModelValue"
  >
    <VaList>
      <VaListLabel class="sticky top-0 bg-white pb-4">
        Results for <span class="ml-1 font-bold text-xl">{{ search }}</span>
      </VaListLabel>
      <VaListItem
          v-for="result in searchResults"
          :key="result.id"
          class="p-2 cursor-pointer hover:bg-gray-100"
          @click="selectResult(result.id)"
      >
        <VaListItemSection>
          <VaListItemLabel class="mb-1">
            {{ result.title }}
          </VaListItemLabel>
          <VaListItemLabel v-if="result.subtitle" caption>
            {{ result.subtitle }}
          </VaListItemLabel>
        </VaListItemSection>
      </VaListItem>
    </VaList>
    <template #footer>
      <VaButton @click="handleClose"> Close </VaButton>
    </template>
  </VaModal>
</template>
