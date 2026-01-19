<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from "vue-router";

let menuOpen = ref(false);
const router = useRouter();

function navigateTo(path: string) {
    router.push(path)
    menuOpen.value = false // Fecha o menu após navegar
}

function toggleMenu() {
    menuOpen.value = !menuOpen.value;
}

</script>

<template>
    <div class="navbar bg-base-100 shadow-sm">
        <div class="flex-none mr-2">
            <button class="btn btn-square btn-ghost" @click="toggleMenu">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                    class="inline-block h-5 w-5 stroke-current">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        :d="menuOpen ? 'M6 18L18 6M6 6l12 12' : 'M4 6h16M4 12h16M4 18h16'">
                    </path>
                </svg>
            </button>
        </div>
        <div class="flex-1">
            <a href="/" @click.prevent="navigateTo('/')" class="font-bold text-xl hover:no-underline">
                SEACPHV
            </a>
        </div>
    </div>

    <div v-if="menuOpen" class="bg-base-200 p-4 flex">
        <ul class="menu w-full">
            <li><a href="/" @click.prevent="navigateTo('/')" class="block py-2 px-4 rounded">
                    Home
                </a>
            </li>
            <li><a href="/gallery" @click.prevent="navigateTo('/gallery')" class="block py-2 px-4 rounded">
                    Gallery
                </a>
            </li>
        </ul>
    </div>
</template>
