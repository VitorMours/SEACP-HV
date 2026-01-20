<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps<{
  imageName: string
}>()

const imageUrl = ref<string>('')

onMounted(async () => {
  const response = await fetch(
    `http://localhost:8000/api/v1/images/${props.imageName}`
  )

  if (!response.ok) {
    console.error('Erro ao carregar imagem')
    return
  }

  const blob = await response.blob()
  imageUrl.value = URL.createObjectURL(blob)
})

onUnmounted(() => {
  if (imageUrl.value) {
    URL.revokeObjectURL(imageUrl.value)
  }
})
</script>

<template>
  <div class="hover-3d my-12 mx-2 cursor-pointer">
    <div class="card bg-base-100 shadow-md border-md w-80 h-96">
      <figure class="aspect-video overflow-hidden">
        <img v-if="imageUrl" :src="imageUrl" :alt="imageName" class="h-full w-full object-cover">
        <div v-else class="flex items-center justify-center h-full bg-base-200">
          <span class="loading loading-spinner loading-lg"></span>
        </div>
      </figure>
      <div class="card-body">
        <div class="card-title">{{ imageName }}</div>
        <p>Imagem processada com sucesso</p>
        <div class="card-actions justify-end">
          <button class="btn btn-primary btn-sm">Ver Detalhes</button>
        </div>
      </div>
    </div>
  </div>
</template>