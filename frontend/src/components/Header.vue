<script setup lang="ts">
</script>

<template>
  <div class="navbar bg-base-200 shadow-sm">
    <div class="flex-1">
      <ul class="menu menu-horizontal gap-1 px-3 items-center">
        <li>
          <RouterLink :to="{ name: 'home' }" class="btn btn-ghost text-xl">
            SEACP-HV
          </RouterLink>
        </li>
        <li>
          <RouterLink :to="{ name: 'gallery' }">Galeria</RouterLink>
        </li>
        <li>
          <RouterLink v-bind:to="{ name: 'upload' }">Upload Image</RouterLink>
        </li>
      </ul>
    </div>
    <div class="flex-none">
      <ul class="menu menu-horizontal gap-1 px-3">
        <li><a>Login</a></li>
        <li><a>Signin</a></li>
      </ul>
    </div>
  </div>
</template>
