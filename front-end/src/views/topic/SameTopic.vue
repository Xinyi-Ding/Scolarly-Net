<script setup>
import { ref } from 'vue';
import { useRoute } from "vue-router";
import { DataSet, Network } from 'vis-network/standalone';
import Net from "@/layouts/NetLayout.vue";
import searchResultExample from "@/lib/searchResultExample.json";
import sameTopicExample from "@/lib/sameTopicExample.json";
import SearchResult from "@/components/SearchResult.vue";

const search = ref('');
const searchLoading = ref(false);
const resultModal = ref(false);
const searchResults = ref(null);

const netResults = ref(null);
const networkContainer = ref(null);
let nodes = new DataSet([]);
let edges = new DataSet([]);
let network = null;
const selectedNodeId = ref(null);

const generateLoading = ref(false);

const handleSearch = () => {
  searchLoading.value = true;
  setTimeout(() => {
    if (search.value !== '') {
      searchResults.value = searchResultExample.data;
      resultModal.value = true;
    }
    searchLoading.value = false;
  }, 1000);
};

const handleResultSelect = (id) => {
  console.log(id);
  netResults.value = null;
  resultModal.value = false;
  generateLoading.value = true;
  nodes.clear();
  edges.clear();
  setTimeout(() => {
    generateLoading.value = false;
    netResults.value = sameTopicExample.data;
    search.value = '';
    initializeNetwork();
  }, 3000);
};

const route = useRoute();
if (route.query.paperId) {
  handleResultSelect(route.query.paperId);
}

const initializeNetwork = () => {
  if (networkContainer.value && netResults.value) {
    const topicNodes = netResults.value.topics.map(topic => ({
      id: `topic-${topic.id}`,
      label: topic.name,
      shape: 'box',
      color: '#97C2FC',
    }));

    const paperNodes = netResults.value.papers.map(paper => ({
      id: paper.id,
      label: paper.title,
      shape: 'ellipse',
      color: '#fff',
    }));
    nodes = new DataSet([...topicNodes, ...paperNodes]);

    const edgesArray = netResults.value.connections.flatMap(connection =>
        connection.papers.map(paperId => ({
          from: `topic-${connection.topic}`, // 使用添加了前缀的主题id
          to: paperId,
        }))
    );
    edges = new DataSet(edgesArray);

    const data = {
      nodes: nodes,
      edges: edges
    };
    const options = {
      physics: {
        enabled: true,
      },
    };
    network = new Network(networkContainer.value, data, options);
    network.on("selectNode", (params) => {
      if (params.nodes.length > 0) {
        const selectedNodeId = params.nodes[0];
        highlightListItem(selectedNodeId);
      }
    });
    network.on("deselectNode", () => {
      selectedNodeId.value = null;
    });
  }
};

const highlightListItem = (nodeId) => {
  selectedNodeId.value = nodeId;
};

const highlightNode = (paperId) => {
  if (network && paperId) {
    network.selectNodes([paperId], false);
  }
};
</script>

<template>
  <SearchResult
      v-model="resultModal"
      :search="search"
      :searchResults="searchResults"
      @select="handleResultSelect"
  />
  <Net>
    <template #list>
      <div class="p-4 sticky top-0 shadow bg-white/20 backdrop-blur z-10">
        <VaInput
            v-model="search"
            class="w-full"
            label="search for a paper"
        >
          <template #append>
            <VaButton
                class="ml-2 bg-primary-500 text-white"
                :disabled="!search"
                icon="search"
                :loading="searchLoading"
                @click="handleSearch"
            />
          </template>
        </VaInput>
      </div>

      <VaList v-if="netResults" class="p-2">
        <VaListItem
            :class="{'highlight': selectedNodeId === netResults.original.id}"
            class="p-2 cursor-pointer bg-blue-50 hover:bg-gray-100">
          <VaListItemSection>
            <p class="mb-1 text-sm text-blue-600 font-bold">Origin Paper</p>
            <VaListItemLabel class="mb-1">
              {{ netResults.original.title }}
            </VaListItemLabel>
            <VaListItemLabel caption>
              {{ netResults.original.authors.toString() }}
            </VaListItemLabel>
          </VaListItemSection>
        </VaListItem>
        <template v-for="paper in netResults.papers">
          <VaListItem
              v-if="!paper.original"
              :key="paper.id"
              :class="{'highlight': paper.id === selectedNodeId}"
              class="p-2 cursor-pointer hover:bg-gray-100"
              @click="highlightNode(paper.id)"
          >
            <VaListItemSection>
              <VaListItemLabel class="mb-1">
                {{ paper.title }}
              </VaListItemLabel>
              <VaListItemLabel caption>
                {{ paper.authors.toString() }}
              </VaListItemLabel>
            </VaListItemSection>
          </VaListItem>
        </template>
      </VaList>
      <p v-else v-show="!generateLoading" class="mt-4 text-center text-gray-500">- Search for a paper first -</p>
      <div v-if="generateLoading" class="w-full text-center">
        <VaProgressCircle
            class="mx-auto mt-8 mb-2"
            :thickness="0.6"
            indeterminate
        />
        <p class="text-gray-500">Generating ...</p>
      </div>
    </template>
    <template #graph>
      <div ref="networkContainer" class="mx-auto w-full h-full"></div>
    </template>
  </Net>
</template>

<style scoped>
.highlight {
  border: 2px solid #154ec1;
}
</style>
