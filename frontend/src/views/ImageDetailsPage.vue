<script setup lang="ts">
import { useRoute } from 'vue-router';
import Header from '../components/Header.vue';

const route = useRoute();
const imageName = route.params.imageName as string;

// URL base do seu backend FastAPI
const API_BASE = "http://localhost:8000/api/v1";
</script>

<template>
  <Header />
  <main class="bg-base-100 min-h-screen">
    <section class="container mx-auto min-h-screen p-5 flex flex-col items-center justify-start">
      
      <h1 class="text-2xl font-bold mb-6">Processamento: {{ imageName }}</h1>

      <div class="tabs tabs-lifted w-full max-w-4xl">
        
        <input type="radio" name="image_tabs" class="tab" aria-label="Original" checked />
        <div class="tab-content bg-base-100 border-base-300 p-6 rounded-box">
          <div class="flex justify-center">
            <img :src="`${API_BASE}/images/${imageName}`" class="rounded-lg shadow-xl max-h-[600px]" alt="Original" />
          </div>
        </div>

        <input type="radio" name="image_tabs" class="tab" aria-label="Gray Scale" />
        <div class="tab-content bg-base-100 border-base-300 p-6 rounded-box">
          <div class="flex justify-center">
            <img :src="`${API_BASE}/gray_scale/${imageName}`" class="rounded-lg shadow-xl max-h-[600px]" alt="Gray Scale" />
          </div>
        </div>

        <input type="radio" name="image_tabs" class="tab" aria-label="Histograms" />
        <div class="tab-content bg-base-100 border-base-300 p-6 rounded-box">
          <div class="text-center">
            <p class="mb-4">Dados do Histograma (Gráfico pode ser inserido aqui)</p>
            <img :src="`${API_BASE}/histogram_plot/${imageName}`" class="mx-auto" alt="Histogram Plot" />
          </div>
        </div>
        
      </div>

    </section>
  </main>
</template>

<style scoped>
/* Garante que o conteúdo das abas tenha uma transição suave */
.tab-content {
  transition: all 0.3s ease;
}
</style>