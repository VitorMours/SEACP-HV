import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "../pages/HomePage.vue";
import UploadPage from '@/pages/UploadPage.vue';
import GalleryPage from "@/pages/GalleryPage.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name:"home",
      component: HomePage
    },
    {
      path: "/upload",
      name:"upload",
      component: UploadPage
    },
    {
      path: "/gallery",
      name: "gallery",
      component: GalleryPage

    }
  ],
})

export default router
