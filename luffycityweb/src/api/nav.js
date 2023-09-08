import http from "../utils/http.js";
import {reactive, ref} from "vue"

/*
* 所有于api服务端进行交互的操作代码，
* 可以单独保存在api目录下，根据数据表单独创建js文件
*
* */
const nav = reactive({
    header_nav_list: [], // 头部导航列表
    footer_nav_list: [], // 脚部导航列表
    get_header_nav() {
        // 获取头部导航
        return http.get("/home/nav/header/")
    },
    get_footer_nav() {
        // 获取脚部导航
        return http.get("/home/nav/footer/")
    },
})

export default nav;