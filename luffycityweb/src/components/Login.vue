<template>
  <div class="title">
    <span :class="{active:user.login_type==0}" @click="user.login_type=0">密码登录</span>
    <span :class="{active:user.login_type==1}" @click="user.login_type=1">短信登录</span>
  </div>
  <div class="inp" v-if="user.login_type==0">
    <input v-model="user.account" type="text" placeholder="用户名 / 手机号码" class="user">
    <input v-model="user.password" type="password" class="pwd" placeholder="密码">
    <div id="geetest1"></div>
    <div class="rember">
      <label>
        <input type="checkbox" class="no" v-model="user.remember"/>
        <span>记住密码</span>
      </label>
      <p>忘记密码</p>
    </div>
    <button class="login_btn" @click="loginhandler">登录</button>
    <p class="go_login">没有账号
      <router-link to="/register">立即注册</router-link>
    </p>
  </div>
  <div class="inp" v-show="user.login_type==1">
    <input v-model="user.mobile" type="text" placeholder="手机号码" class="user">
    <input v-model="user.code" type="text" class="code" placeholder="短信验证码">
    <el-button id="get_code" type="primary">获取验证码</el-button>
    <button class="login_btn">登录</button>
    <p class="go_login">没有账号 <span>立即注册</span></p>
  </div>
</template>

<script setup>
import {reactive} from "vue";
import {ElMessage} from "element-plus";
import user from "../api/user.js";

const emit = defineEmits(["successhandle",])

import {useStore} from "vuex";

const store = useStore();

// 登陆函数
const loginhandler = () => {
  if (user.account.length < 1 || user.password.length < 1) {
    // 错误提示
    ElMessage("用户名或密码不能为空！");
    return false;
  }

  // 发送请求
  user.login({
    "username": user.account,
    "password": user.password,
  }).then(response => {
    ElMessage("登陆成功！");

    // 保存token，并根据用户的选择，是否记住密码
    // 先删除之前存留的状态
    sessionStorage.removeItem("token");
    localStorage.removeItem("token");
    const token = response.data.access;
    if (user.remember) {
      localStorage.token = token;
    } else {
      sessionStorage.token = token;
    }

    // vuex存储用户登录信息，保存token，并根据用户的选择，是否记住密码
    let payload = response.data.access.split(".")[1]; // payload
    let payload_data = JSON.parse(atob(payload)); // 用户信息
    // console.log("payload_data:",payload_data);
    store.commit("login", payload_data);

    // 关闭登陆窗口，通知父组件
    user.account = "";
    user.password = "";
    user.mobile = "";
    user.code = "";
    user.remember = false;

    emit("successhandle");

  }).catch(error => {
    // console.log(error?.response?.data);
    ElMessage.error(error?.response?.data?.detail);
  })

}

</script>

<style scoped>
.title {
  font-size: 20px;
  color: #9b9b9b;
  letter-spacing: .32px;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  justify-content: space-around;
  padding: 0px 60px 0 60px;
  margin-bottom: 20px;
  cursor: pointer;
}

.title span.active {
  color: #4a4a4a;
  border-bottom: 2px solid #84cc39;
}

.inp {
  width: 350px;
  margin: 0 auto;
}

.inp .code {
  width: 220px;
  margin-right: 16px;
}

#get_code {
  margin-top: 6px;
}

.inp input {
  outline: 0;
  width: 100%;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp input.user {
  margin-bottom: 16px;
}

.inp .rember {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-top: 10px;
}

.inp .rember p:first-of-type {
  font-size: 12px;
  color: #4a4a4a;
  letter-spacing: .19px;
  margin-left: 22px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  /*position: relative;*/
}

.inp .rember p:nth-of-type(2) {
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .19px;
  cursor: pointer;
}

.inp .rember input {
  outline: 0;
  width: 30px;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
  vertical-align: middle;
  margin-right: 4px;
}

.inp .rember p span {
  display: inline-block;
  font-size: 12px;
  width: 100px;
}

.login_btn {
  cursor: pointer;
  width: 100%;
  height: 45px;
  background: #84cc39;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
  letter-spacing: .26px;
  margin-top: 30px;
  border: none;
  outline: none;
}

.inp .go_login {
  text-align: center;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: .26px;
  padding-top: 20px;
}

.inp .go_login span {
  color: #84cc39;
  cursor: pointer;
}
</style>