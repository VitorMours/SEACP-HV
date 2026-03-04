<script setup lang="ts">
  import ImageUploader from '@/components/ImageUploader.vue';
  import Header from '@/components/Header.vue';
</script>

<template>
  <div class="min-h-screen flex flex-col bg-gray-900">
    <Header />

    <main class="flex-1 flex flex-col items-center justify-center p-5">

      <div class="flex flex-col items-center justify-center w-full max-w-4xl min-h-[60vh] bg-gray-800 p-10 rounded-xl border-2 border-dashed border-gray-600 text-center shadow-2xl">
        <h1 class="text-white text-2xl font-bold mb-6">
          Insira abaixo a imagem que deseja fazer upload.
        </h1>
        <ImageUploader />
      </div>

    </main>
  </div>
</template>