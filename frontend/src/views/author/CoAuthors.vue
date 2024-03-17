<script setup>
import { ref } from 'vue';
import { useRoute } from "vue-router";
import { DataSet, Network } from 'vis-network/standalone';
import Net from "@/layouts/NetLayout.vue";
import SearchResult from "@/components/SearchResult.vue";
import searchResultExample from "@/lib/searchResults.json";
import topicConnectionExample from "@/lib/exampleCoAuthor.json";
import { authors2Str, generateOptions } from "@/utils/network.js";
import PaperList from "@/components/PaperList.vue";

// search related variables
const search = ref('');
const searchLoading = ref(false);
const resultModal = ref(false);
const searchResults = ref(null);

// network related variables
const netResults = ref(null);
const networkContainer = ref(null);
let nodes = new DataSet([]);
let edges = new DataSet([]);
let network = null;
const originalPaper = ref({});
const selectedNodeId = ref(null);

// loading related variables
const generateLoading = ref(false);

const handleSearch = () => {
  searchLoading.value = true;
  setTimeout(() => {
    if (search.value !== '') {
      // searchResults.value = searchResultExample.data.map(item => ({
      //   id: item.id,
      //   title: item.name,
      //   subtitle: item.count + ' papers related',
      // }));
      searchResults.value = searchResultExample.data;
      resultModal.value = true; // open the search result modal
    }
    searchLoading.value = false;
  }, 1000);
};

const handleResultSelect = (id) => {
  originalPaper.value.articleId = id;
  netResults.value = null; // clear the previous network data
  resultModal.value = false;
  generateLoading.value = true;
  nodes.clear();
  edges.clear();
  setTimeout(() => {
    generateLoading.value = false;
    const data = topicConnectionExample.data;
    originalPaper.value = data.papers.find(paper => paper.articleId === originalPaper.value.articleId);
    netResults.value = data;
    search.value = '';
    initializeNetwork();
  }, 1000);
};

// check if the paperId is in the query, if so, generate the network
const route = useRoute();
if (route.query.paperId) {
  handleResultSelect(+route.query.paperId);
}

const initializeNetwork = () => {
  if (networkContainer.value) {
    const authors = netResults.value.authors;
    const papers = netResults.value.papers;
    const connections = netResults.value.connections;

    // convert authors to nodes
    const authorNodes = authors.map(author => ({
      id: `author-${author.id}`,
      label: author.name,
      shape: 'triangle',
      color: '#4ade80',
    }));

    // convert papers to nodes
    const paperNodes = papers.map(paper => ({
      id: paper.articleId,
      label: paper.title,
      title: authors2Str(paper.authors),
      color: paper.articleId === originalPaper.value.articleId ? '#F39C12' : null,
    }));

    // convert connections to edges
    const edgesArray = connections.flatMap(connection =>
        connection.papers.map(paperId => ({
          from: `author-${connection.author}`,
          to: paperId,
        }))
    );

    // create DataSet instances for nodes and edges
    const nodes = new DataSet([...authorNodes, ...paperNodes]);
    const edges = new DataSet(edgesArray);

    // define the data and options for the network
    const data = {nodes, edges};
    const options = generateOptions();

    // initialize the network
    network = new Network(networkContainer.value, data, options);

    // event listeners for node selection (if needed)
    network.on("selectNode", (params) => {
      if (params.nodes.length > 0) {
        const selectedNodeId = params.nodes[0];
        highlightListItem(selectedNodeId); // Ensure you have this function defined or remove this listener if unnecessary
      }
    });

    network.on("deselectNode", () => {
      selectedNodeId.value = null; // Make sure this variable is reactive (e.g., a ref) or adjust accordingly
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
      <div ref="networkContainer" class="mx-auto w-full h-full"></div>
    </template>
  </Net>
</template>

<style scoped>

</style>
