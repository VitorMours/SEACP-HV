import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Header from './components/Header.vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.component(
  "Header", Header 
);


app.use(createPinia())
app.use(router)

app.mount('#app')
