import { createRouter, createWebHistory, type Router } from "vue-router";
import routes from "./routes";

const router: Router = createRouter({
  routes,
  history: createWebHistory(import.meta.env.BASE_URL),
});


router.afterEach((to, from) => {
  console.log(`Navegando de ${from.path} para ${to.path}`)
})
export default router;