import HomePage from "../views/HomePage.vue";
import ImagePage from "../views/ImagePage.vue";
import ImageDetailsPage from "../views/ImageDetailsPage.vue";
const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
    meta: {
      title: "Index",
      requiresAuth: false,
    },
  },
  {
    path: "/image/:imageName",
    name: "ImageDetail",
    component: ImageDetailsPage,
  },
  {
    path: "/gallery",
    name: "Gallery",
    component: ImagePage,
  },
];

export default routes;
