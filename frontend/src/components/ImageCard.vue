<script setup lang="ts">
  import { ref, onMounted } from "vue"
  const processing = ref(true);
  const showErrorDialog = ref(false);

  async function fetchingImages(){

    try{
      const response = await fetch("http://localhost:8000/api/v1/images", {
        method: 'GET'
      });
      const result = await response.json();
      console.log(result);
      if(!response.ok){
        showErrorDialog.value = true;
      }

    }catch(error){

    }finally{
      processing.value = false;
    }

  }

  onMounted(() => fetchingImages());

</script>

<template>
  <main class="bg-base-100 min-h-screen">
    <section
      class="container mx-auto min-h-screen p-5 bg-base-100 flex items-center justify-center">
      <div v-if="processing">
        <span class="loading loading-spinner loading-xl"></span>
      </div>
      <div v-else class="card bg-base-100 shadow-md border-md">
        <figure>
          <img src="" alt="">
        </figure>
        <div class="card-body">
          <div class="card-title">asd</div>
          <p>asd</p>
          <div class="card-actions">asd</div>
        </div>
      </div>

    </section>
  </main>

</template>