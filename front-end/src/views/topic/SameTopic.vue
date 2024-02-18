<template>
  <div>
    <div ref="networkContainer" class="mx-auto border-solid border-2 w-2/3 h-[50vh]"></div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { DataSet, Network } from 'vis-network/standalone';

const networkContainer = ref(null);

const nodes = new DataSet([
  { id: 1, label: 'Node 1' },
  { id: 2, label: 'Node 2' },
  { id: 3, label: 'Node 3' },
  { id: 4, label: 'Node 4' },
  { id: 5, label: 'Node 5' }
]);

const edges = new DataSet([
  { from: 1, to: 3 },
  { from: 1, to: 2 },
  { from: 1, to: 4 },
  { from: 1, to: 5 }
]);

onMounted(() => {
  if (networkContainer.value) {
    const data = {
      nodes: nodes,
      edges: edges
    };
    const options = {};
    new Network(networkContainer.value, data, options);
  }
});
</script>
