import {reactive, ref} from "vue";
import http from "../utils/http.js";


const user = reactive({
    login_type: 0, // 登陆方式：0，密码登陆；1，短信登陆
    account: "", // 登陆账号/手机号/邮箱
    password: "",
    remember: false, // 是否记住登陆状态
    mobile: "",
    code: "",

    login(){
        return http.post("/users/login/",{
            "username": this.account,
            "password": this.password,
        })
    }
})

export default user;