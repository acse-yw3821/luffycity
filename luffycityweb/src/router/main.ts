import {createApp} from 'vue'
import App from './App.vue'
import router from './index.js'
import 'element-plus/dist/index.css';
import store from "../store/index.js";

createApp(App).use(router).use(store).mount('#app')