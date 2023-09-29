import {reactive, ref} from "vue";
import http from "../utils/http.js";


const user = reactive({
    login_type: 0, // 登陆方式：0，密码登陆；1，短信登陆
    account: "", // 登陆账号/手机号/邮箱
    password: "",
    re_password: "",
    remember: false, // 是否记住登陆状态
    mobile: "",
    code: "",
    sms_btn_text: "点击获取验证码", // 短信按钮提示
    is_send: false,  // 短信发送的标记
    sms_interval: 60,// 间隔时间
    interval: null,  // 定时器的标记
    login() {
        return http.post("/users/login/", {
            "username": this.account,
            "password": this.password,
        })
    },
    check_mobile() {
        // 验证手机号
        return http.get(`/users/mobile/${this.mobile}/`)
    },
    register() {
        // 用户注册请求
        console.log(this.mobile, this.code, this.password, this.re_password);
        return http.post("/users/register/", {
            "mobile": this.mobile,
            "sms_code": this.code,
            "password": this.password,
            "re_password": this.re_password,
        })
    },
    get_sms_code(){
        return http.get(`users/sms/${this.mobile}`)
    }
})

export default user;