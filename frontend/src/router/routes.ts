import HomePage from "../views/HomePage.vue";
import ImagePage from "../views/ImagePage.vue";
import ImageDetailsPage from "../views/ImageDetailsPage.vue";
const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
    meta: {
      title: 'Index',
      requiresAuth: false,
    }
  },
  {
    path: '/gallery',
    name: 'Gallery',
    component: ImagePage,
  },
  {
    path:'/gallery/:imageId',
    name: "Image Visualizer",
    component: ImageDetailsPage,
  }
]

export default routes;