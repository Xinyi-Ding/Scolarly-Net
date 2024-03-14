<script setup>
import UserChip from "@/components/UserChip.vue";

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
      <VaListLabel class="sticky top-0 pb-4 bg-white/90 z-10">
        Results for <span class="ml-1 font-bold text-xl">{{ search }}</span>
      </VaListLabel>
      <VaListItem
          v-for="result in searchResults"
          :key="result.id"
          class="p-2 my-1 cursor-pointer hover:bg-gray-100 border-b border-gray-200 border-solid"
          @click="selectResult(result.id)"
      >
        <VaListItemSection>
          <VaListItemLabel class="mb-3">
            <span class="ml-1">{{ result.title }}</span>
          </VaListItemLabel>
          <VaListItemLabel v-if="result.authors.length > 0" caption>
            <UserChip
                v-for="author in result.authors"
                :key="author.id"
                :author="author"
            />
          </VaListItemLabel>
        </VaListItemSection>
      </VaListItem>
    </VaList>
    <template #footer>
      <VaButton @click="handleClose"> Close </VaButton>
    </template>
  </VaModal>
</template>
