<!-- App.vue - DEVE TER router-view -->
<template>
  <!-- O router-view é ESSENCIAL -->
  <router-view />
</template>

<script setup lang="ts">
// Debug
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(() => {
  console.log('🚀 App.vue montado')
  console.log('📍 Rota inicial:', router.currentRoute.value.path)
})
</script>