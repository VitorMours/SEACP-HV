<script setup lang="ts">
import { ref } from "vue";

const selectedFile = ref<File | null>(null);

function onFileChange(e: Event) {
  const target = e.target as HTMLInputElement
  selectedFile.value = target.files?.[0] ?? null
}

defineExpose({ selectedFile });
</script>
<template>
  <input type="file" class="file-input" @change="onFileChange" />
</template>
<style>

</style>