<script setup lang="ts">
import { ref, onMounted } from "vue";
import ImageService from "@/services/ImageService.ts";

interface Image {
  id: number | null;
  image_name: string;
  image: string | null;
  filetype: string;
  path: string;
}

const BASE_URL = "http://localhost:8000/media/raw";

const images = ref<Image[]>([]);
const fetchingImages = ref<boolean>(true);
const errorDialog = ref<HTMLDialogElement | null>(null);

function getImageUrl(image: Image): string {
  return `${BASE_URL}/${encodeURIComponent(image.image_name)}`;
}

async function getImages() {
  try {
    images.value = await ImageService.getAllImages();
  } catch (error) {
    console.error("Erro ao buscar imagens:", error);
    errorDialog.value?.showModal();
  } finally {
    fetchingImages.value = false;
  }
}

onMounted(() => getImages());
</script>

<template>
  <div class="min-h-screen flex flex-col bg-base-300">
    <Header />
    <main class="flex flex-1 flex-col items-center p-5 gap-6">
      <span v-if="fetchingImages" class="loading loading-spinner loading-lg text-primary mt-20" />
      <template v-else>
        <h1 class="text-2xl font-bold self-start">Imagens enviadas</h1>

        <div v-if="images.length === 0" class="flex flex-col items-center justify-center flex-1 gap-3 opacity-50">
          <p class="text-lg">Nenhuma imagem encontrada.</p>
        </div>

        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full">
          <div v-for="image in images" :key="image.image_name" class="card bg-base-100 shadow-md">
            <figure class="h-48 overflow-hidden">
              <img :src="getImageUrl(image)" :alt="image.image_name" class="w-full h-full object-cover" />
            </figure>
            <div class="card-body p-4">
              <h2 class="card-title text-base">{{ image.image_name }}</h2>
            </div>
          </div>
        </div>
      </template>

      <dialog ref="errorDialog" class="modal">
        <div class="modal-box">
          <h3 class="font-bold text-xl text-error">Erro ao carregar imagens</h3>
          <p class="py-4">Não foi possível buscar as imagens. Tente novamente mais tarde.</p>
          <div class="modal-action">
            <form method="dialog">
              <button class="btn">Fechar</button>
            </form>
          </div>
        </div>
      </dialog>
    </main>
  </div>
</template>
