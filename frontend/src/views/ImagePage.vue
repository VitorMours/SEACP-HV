<script setup lang="ts">
import Header from '../components/Header.vue';
import ImageCard from '../components/ImageCard.vue';
import { ref, onMounted } from "vue";

const processing = ref<boolean>(true);
const showErrorDialog = ref<boolean>(false);
const namesList = ref<string[]>([]);

async function fetchingImages() {

  try {
    const response = await fetch("http://localhost:8000/api/v1/images", {
      method: 'GET'
    });
    const result = await response.json();
    if (!response.ok) {
      showErrorDialog.value = true;
    }
    namesList.value = result.map((item: { name: any; })  => item.name)
  
  } catch (error) {
      console.log(error);
  } finally {
    processing.value = false;
  }

}

onMounted(() => fetchingImages());

</script>
<template>
  <Header />

  <main class="bg-base-100 min-h-screen">
    <section class="container mx-auto min-h-screen p-5 flex items-center justify-center">
      
      <!-- Loading -->
      <div v-if="processing" class="flex justify-center items-center w-full">
        <span class="loading loading-spinner"></span>
      </div>

      <!-- Cards -->
      <div
        v-else
        class="flex flex-wrap gap-6 justify-center w-full"
      >
        <ImageCard
          v-for="name in namesList"
          :key="name"
          :imageName="name"
        />
      </div>

    </section>
  </main>
</template>

<style scoped></style>
