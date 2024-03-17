<script setup>
import { ref } from 'vue';
import { useRoute } from "vue-router";
import { DataSet, Network } from 'vis-network/standalone';
import Net from "@/layouts/NetLayout.vue";
import SearchResult from "@/components/SearchResult.vue";
import { authors2Str, generateOptions } from "@/utils/network.js";
import PaperList from "@/components/PaperList.vue";
import req from "@/utils/req.js";

const search = ref('');
const searchLoading = ref(false);
const resultModal = ref(false);
const searchResults = ref(null);

const netResults = ref(null);
const networkContainer = ref(null);
let nodes = new DataSet([]);
let edges = new DataSet([]);
let network = null;
const originalPaper = ref({});
const selectedNodeId = ref(null);

const generateLoading = ref(false);

const handleSearch = async () => {
  if (search.value !== '') {
    searchLoading.value = true;
    const data = await req.get('/catalog/papers/search', { title: search.value });
    console.log('search', data.data)
    searchResults.value = data.data.data;
    resultModal.value = true;
    searchLoading.value = false;
  }
};

const handleResultSelect = async (id) => {
  originalPaper.value.articleId = id;
  netResults.value = null; // clear the previous network data
  resultModal.value = false;
  generateLoading.value = true;
  nodes.clear();
  edges.clear();
  let data = await req.get('/catalog/same-topi', { article_id: id });
  data = data.data.data;
  console.log('same topic', data);
  originalPaper.value = data.papers.find(paper => paper.articleId === originalPaper.value.articleId);
  netResults.value = data;
  search.value = '';
  generateLoading.value = false;
  initializeNetwork();
};

const route = useRoute();
if (route.query.paperId) {
  handleResultSelect(+route.query.paperId);
}

const initializeNetwork = () => {
  if (networkContainer.value && netResults.value) {
    // convert topics to nodes
    const topicNodes = netResults.value.topics.map(topic => ({
      id: `topic-${topic.id}`,
      label: topic.name,
      shape: 'star',
      color: '#4ade80',
    }));

    // convert papers to nodes
    const paperNodes = netResults.value.papers.map(paper => ({
      id: paper.articleId,
      label: paper.title,
      shape: 'dot',
      color: paper.articleId === originalPaper.value.articleId ? '#FFC107' : null,
      title: authors2Str(paper.authors)
    }));

    // convert connections to edges
    const edgesArray = netResults.value.connections.flatMap(connection =>
        connection.papers.map(paperId => ({
          from: `topic-${connection.topic}`,
          to: paperId,
        }))
    );

    // create DataSet instances for nodes and edges
    nodes = new DataSet([...topicNodes, ...paperNodes]);
    edges = new DataSet(edgesArray);

    // define the data and options for the network
    const data = {nodes: nodes, edges: edges};
    const options = generateOptions();

    // initialize the network
    network = new Network(networkContainer.value, data, options);

    // event listeners for node selection
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

const highlightNode = (nodeId) => {
  if (network && nodeId) {
    // select the node
    network.selectNodes([nodeId], false);
    // find and select the edges connected to the node
    const connectedEdges = network.getConnectedEdges(nodeId);
    network.selectEdges(connectedEdges);
    // highlight the list item
    highlightListItem(nodeId);
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
      <PaperList
          v-if="netResults"
          :originalPaper="originalPaper"
          :papers="netResults.papers"
          :selectedNodeId="selectedNodeId"
          @highlightNode="highlightNode"
      />
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
      <div ref="networkContainer" class="mx-auto w-full h-full"/>
    </template>
  </Net>
</template>

<style scoped>

</style>
