<script setup>
import { ref } from 'vue';
import { useRoute } from "vue-router";
import { DataSet, Network } from 'vis-network/standalone';
import Net from "@/layouts/NetLayout.vue";
import SearchResult from "@/components/SearchResult.vue";
import searchResultExample from "@/lib/searchAuthorResults.json";
import topicConnectionExample from "@/lib/exampleCoAuthor.json";

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
const selectedNodeId = ref(null);

// loading related variables
const generateLoading = ref(false);

const handleSearch = () => {
  searchLoading.value = true;
  setTimeout(() => {
    if (search.value !== '') {
      searchResults.value = searchResultExample.data.map(item => ({
        id: item.id,
        title: item.name,
        subtitle: item.count + ' papers related',
      }));
      resultModal.value = true; // open the search result modal
    }
    searchLoading.value = false;
  }, 1000);
};

const handleResultSelect = (id) => {
  console.log(id);
  netResults.value = null; // clear the previous network data
  resultModal.value = false;
  generateLoading.value = true;
  nodes.clear();
  edges.clear();
  setTimeout(() => {
    generateLoading.value = false;
    netResults.value = topicConnectionExample.data;
    search.value = '';
    initializeNetwork();
  }, 1000);
};

// check if the paperId is in the query, if so, generate the network
const route = useRoute();
if (route.query.paperId) {
  handleResultSelect(route.query.paperId);
}

// TODO: Use groupBy to group the papers by author
const initializeNetwork = () => {
  if (networkContainer.value) {
    const authors = netResults.value.authors;
    const papers = netResults.value.papers;
    const connections = netResults.value.connections;

    // convert authors to nodes
    const authorNodes = authors.map(author => ({
      id: `author-${author.id}`,
      label: author.name,
      shape: 'circle',
      color: author.original ? '#F39C12' : '#27AE60',
    }));

    // convert papers to nodes
    const paperNodes = papers.map(paper => ({
      id: paper.id,
      label: paper.title,
      shape: 'box',
      color: '#3498DB',
      title: paper.authors
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
    const data = { nodes, edges };
    const options = {
      edges: {
        smooth: {
          type: 'cubicBezier',
          forceDirection: 'horizontal',
          roundness: 0.4,
        },
        color: {
          color: '#90CAF9',
          highlight: 'red',
        },
      },
      physics: false,
      layout: {
        randomSeed: undefined,
        improvedLayout: true
      }
    };

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


handleResultSelect(1);
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
            label="search for an author"
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
        <template v-for="paper in netResults.papers" :key="paper.id">
          <VaListItem
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
      <p v-else v-show="!generateLoading" class="mt-4 text-center text-gray-500">- Search for an author first -</p>
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
