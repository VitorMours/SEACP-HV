import { createRouter, createWebHistory } from 'vue-router'
import HomePage from "../pages/HomePage.vue";
import UploadPage from '@/pages/UploadPage.vue';

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
  ],
})

export default router
