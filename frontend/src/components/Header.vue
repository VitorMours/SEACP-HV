<script setup lang="ts">
    import { ref } from 'vue';
    let menuOpen = ref(false);

    function toggleMenu(){
        menuOpen.value = !menuOpen.value;
    }

</script>

<template>
    <div class="navbar bg-base-100 shadow-sm">
        <div class="flex-none mr-2">
            <button class="btn btn-square btn-ghost" @click="toggleMenu">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                    class="inline-block h-5 w-5 stroke-current">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16">
                    </path>
                </svg>
            </button>
        </div>
        <div class="flex-1">
            <a class="font-bold text-xl" href="">SEACPHV</a>
        </div>
    </div>
    <div v-if="menuOpen" class="bg-base-200 p-4 flex">
        <ul class="menu w-full">
            <li class="flex-1"><a>Menu</a></li>
            <li><a>Images</a></li>
            <li><a>Results</a></li>
        </ul>
    </div>
</template>

