<script setup lang="ts">
import { ref } from "vue";
import ImageUploader from '@/components/ImageUploader.vue';
import ImageService from "@/services/imageService";

const imageUploader = ref<InstanceType<typeof ImageUploader> | null>(null);
const imageProcessing = ref<boolean>(false);
const alertSuccessDialog = ref<HTMLDialogElement | null>(null);

async function processarImagem() {
  const file: File | null = imageUploader.value?.selectedFile ?? null;

  if (!file) {
    window.alert("Você precisa selecionar uma imagem antes de continuar.");
    return;
  }

  try {
    imageProcessing.value = true;
    await ImageService.sendImage(file);
    alertSuccessDialog.value?.showModal();
  } catch (error) {
    console.error("Erro ao enviar imagem:", error);
    window.alert("Ocorreu um erro ao enviar a imagem. Tente novamente.");
  } finally {
    imageProcessing.value = false;
  }
}
</script>

<template>
  <div class="min-h-screen flex flex-col bg-base-300">
    <Header />
    <main class="flex-1 flex flex-col items-center justify-center p-5">
      <div
        class="flex flex-col items-center justify-center w-full max-w-4xl min-h-[60vh] p-10 rounded-xl border-2 border-dashed bg-base-100 text-center shadow-md">
        <h1 class="text-2xl font-bold mb-6">
          Insira abaixo a imagem que deseja fazer upload.
        </h1>

        <ImageUploader ref="imageUploader" />

        <span
          v-if="imageProcessing"
          class="text-success mt-5 loading loading-spinner loading-xl"
        />
        <button
          v-else
          class="btn btn-soft btn-accent mt-5"
          @click="processarImagem"
        >
          Processar Imagem
        </button>

        <!-- Dialog controlado via ref + showModal() -->
        <dialog ref="alertSuccessDialog" class="modal">
          <div class="modal-box">
            <h3 class="text-lg font-bold">Imagem enviada para processamento!</h3>
            <p class="py-4">
              Você pode verificar a imagem processada dentro do ambiente de galeria.
            </p>
            <div class="modal-action">
              <form method="dialog">
                <button class="btn">Fechar</button>
              </form>
            </div>
          </div>
        </dialog>

      </div>
    </main>
  </div>
</template>
