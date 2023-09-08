import {createApp} from 'vue'
import App from './App.vue'
import router from './index.js'
import 'element-plus/dist/index.css';

createApp(App).use(router).mount('#app')