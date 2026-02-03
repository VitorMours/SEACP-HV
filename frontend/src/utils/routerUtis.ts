import { createRouter, createWebHistory } from 'vue-router';
import router from "../router/index";
// utils/navigation.ts (seu arquivo atual)

function navigateTo(path: string) {
    return router.push(path);
}

export { navigateTo };