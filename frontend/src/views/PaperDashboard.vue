<script setup>
import { ref, watch } from "vue";
import DashboardCard from "@/components/DashboardCard.vue";
import dashboardExample from '@/lib/exampleDashboard.json';

const uploaded = ref(false);
const ready = ref({
  sameTopic: -1,
  topicConnections: -1,
  coAuthors: -1,
  affiliations: -1,
  citedTree: -1,
  citedByTree: -1,
});
const paper = ref(null);

const basic = ref([]);

const onFileAdded = async () => {
  if (basic.value.length > 0) {
    setTimeout(() => {
      uploaded.value = true;
      ready.value = {
        sameTopic: 0,
        topicConnections: 0,
        coAuthors: 0,
        affiliations: 0,
        citedTree: 0,
        citedByTree: 0,
      };
    }, 1000);
    setTimeout(() => {
      paper.value = dashboardExample;
      ready.value = {
        sameTopic: 1,
        topicConnections: 1,
        coAuthors: 1,
        affiliations: -1,
        citedTree: 1,
        citedByTree: -1,
      };
    }, 5000);
  }
};

watch(basic, (newValue, oldValue) => {
  if (newValue.length > oldValue.length) {
    onFileAdded();
  }
});

</script>

<template>
  <div class="p-4">
    <VaAlert color="info" border="left" class="mb-4 p-6">
      <template #icon>
        <VaIcon name="info" />
      </template>
      <p class="mb-3">This is the Dashboard, where you can upload your own papers for analysis and view related information.</p>
      <p>When the paper analysis is successful, clicking on the card below will redirect to the relevant page and
        automatically display the analysis results of the uploaded paper.</p>
    </VaAlert>
    <VaFileUpload
        v-model="basic"
        :disabled="basic.length > 0"
        v-if="!uploaded"
        class="mb-4"
        file-types="application/msword,application/pdf"
    >
      <div class="p-4 border-2 border-gray-300 border-dashed">
        <div class="upload">
          <VaIcon class="mr-2" size="large" name="upload" color="primary" />
          <p>
            <span>Click</span>or<span>Drag & Drop</span>a file to upload{{paper}}
          </p>
        </div>
      </div>
    </VaFileUpload>
    <VaCard
        v-else
        class="min-h-32 relative mb-4"
    >
      <div>
        <VaCardTitle>
          <div>
            <span v-if="paper !== null" class="font-black text-lg">
              {{ paper.title }}
            </span>
            <VaIcon v-else name="loop" spin />
          </div>
        </VaCardTitle>
        <VaCardContent class="paper break-words overflow-hidden -mt-2">
          <div>
            <span>Authors:</span>
            <span v-if="paper !== null">
              {{ paper.authors.toString() }}
            </span>
            <VaIcon v-else name="loop" spin />
          </div>
          <div>
            <span>Affiliations:</span>
            <span v-if="paper !== null">
              {{ paper.affiliations.length > 0 ? paper.affiliations.toString() : '-' }}
            </span>
            <VaIcon v-else name="loop" spin />
          </div>
          <div>
            <span>Date:</span>
            <span v-if="paper !== null">
              {{ paper.date }}
            </span>
            <VaIcon v-else name="loop" spin />
          </div>
          <div>
            <span>DOI:</span>
            <span v-if="paper !== null">
              {{ paper.doi }}
            </span>
            <VaIcon v-else name="loop" spin />
          </div>
          <div>
            <span>Keywords:</span>
            <span v-if="paper !== null">
              {{ paper.keywords.toString() }}
            </span>
            <VaIcon v-else name="loop" spin />
          </div>
          <div>
            <span>References:</span>
            <span v-if="paper !== null">
              {{ paper.references ? paper.references : 'None' }}
            </span>
            <VaIcon v-else name="loop" spin />
          </div>
        </VaCardContent>
      </div>
    </VaCard>
    <div class="grid grid-cols-6 gap-4">
      <DashboardCard
          class="col-span-3"
          :ready="ready.sameTopic"
          section="Topic"
          title="Same Topic"
          content="Explore the papers with same topics"
          link="/topic/same-topic"
          :paper-id="paper?.id"
      />
      <DashboardCard
          class="col-span-3"
          :ready="ready.topicConnections"
          section="Topic"
          title="Topic Connections"
          content="Explore the connections between topics"
          link="/topic/connections"
          :paper-id="paper?.id"
      />
      <DashboardCard
          class="col-span-2"
          :ready="ready.coAuthors"
          section="Author"
          title="Co-Authors"
          content="Explore the co-authors of the paper"
          link="/author/co-authors"
          :paper-id="paper?.id"
      />
      <DashboardCard
          class="col-span-2"
          :ready="ready.affiliations"
          section="Author"
          title="Affiliations"
          content="Explore the affiliations of the authors of the paper"
          link="/author/affiliations"
          :paper-id="paper?.id"
      />
      <DashboardCard
          class="col-span-2"
          :ready="ready.citedTree"
          section="Reference"
          title="Cited Tree"
          content="Explore the papers that are cited by the paper"
          link="/reference/cited"
          :paper-id="paper?.id"
      />
      <DashboardCard
          class="col-span-3"
          :ready="ready.citedByTree"
          section="Reference"
          title="Cited-By Tree"
          content="Explore the papers that cite the paper"
          link="/reference/cited-by"
          :paper-id="paper?.id"
      />

    </div>
  </div>
</template>

<style scoped>
.upload {
  @apply h-32 flex justify-center items-center mb-2 text-center;
}
.upload span {
  @apply text-lg font-black mx-2;
}
.paper div {
  @apply mb-2;
}
.paper span:nth-child(odd) {
  @apply font-bold mr-2;
}

</style>
