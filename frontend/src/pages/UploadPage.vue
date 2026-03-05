<script setup lang="ts">
import { ref } from "vue";
import ImageUploader from '@/components/ImageUploader.vue';
import ImageService from "@/services/imageService";
const imageUploader = ref<InstanceType<typeof ImageUploader> | null>(null);
const imageProcessing = ref<boolean>(false);


async function processarImagem() {
  imageProcessing.value = true;
  const file: File | null = imageUploader.value?.selectedFile ?? null;
  if (!file) {
    console.log("Files vazio..."); 
    window.alert("Voce precisa colocar uma imagem dentro do sistema");    
    return;
  }
  const response = ImageService.sendImage(file);
  imageProcessing.value = false;
}

</script>

<template>
  <div class="min-h-screen flex flex-col bg-base-300">
    <Header />

    <main class="flex-1 flex flex-col items-center justify-center p-5">

      <div
        class="flex flex-col items-center justify-center w-full max-w-4xl min-h-[60vh] p-10 rounded-xl border-2 border-dashed bg-base-100 text-center shadow-md">
        <h1 class=" text-2xl font-bold mb-6">
          Insira abaixo a imagem que deseja fazer upload.
        </h1>
        <ImageUploader ref="imageUploader" />
        <span v-if="imageProcessing" class="text-success mt-5 loading loading-spinner loading-xl"></span>
        <button v-else class="btn btn-soft btn-accent mt-5" @click="processarImagem">Processar Imagem</button>
      </div>
    </main>
  </div>
</template>