import HomePage from "../views/HomePage.vue";
import ImagePage from "../views/ImagePage.vue";
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
]

export default routes;