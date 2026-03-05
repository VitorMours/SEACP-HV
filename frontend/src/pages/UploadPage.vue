<script setup lang="ts">
import { ref } from "vue";
import ImageUploader from '@/components/ImageUploader.vue';

const imageUploader = ref<InstanceType<typeof ImageUploader> | null>(null);

async function processarImagem() {

  const file: File | null = imageUploader.value?.selectedFile ?? null;
  if (!file) {
    console.log("Files vazio..."); return;
  }
  console.log(`Sending the files: ${file}`);
  const formData = new FormData();
  formData.append("files", file)

  await fetch("",
    {
      method: "POST",
      body: formData
    }
  );
}

</script>

<template>
  <div class="min-h-screen flex flex-col bg-gray-900">
    <Header />

    <main class="flex-1 flex flex-col items-center justify-center p-5">

      <div
        class="flex flex-col items-center justify-center w-full max-w-4xl min-h-[60vh] bg-gray-800 p-10 rounded-xl border-2 border-dashed border-gray-600 text-center shadow-2xl">
        <h1 class="text-white text-2xl font-bold mb-6">
          Insira abaixo a imagem que deseja fazer upload.
        </h1>
        <ImageUploader ref="imageUploader" />
        <button class="btn btn-soft btn-accent mt-5" @click="processarImagem">Processar Imagem</button>
      </div>
    </main>
  </div>
</template>