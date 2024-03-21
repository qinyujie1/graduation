<template>
  <!-- 登录 -->
  <el-form
      :model="loginUser"
      :rules="rules"
      ref="loginForm"
      label-width="100px"
      class="login-form sign-in-form"
  >
    <el-form-item label="用户名" prop="name">
      <el-input v-model="loginUser.name" name="name" placeholder="Enter Name..."/>
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input
          v-model="loginUser.password" name="password"
          type="password"
          placeholder="Enter Password..."
          show-password
      />
    </el-form-item>
    <el-form-item label="角色" prop="role">
      <el-select v-model="loginUser.role">
        <el-option label="管理员" value="admin" name="role"></el-option>
        <el-option label="用户" value="user" name="role"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item>
      <el-button
          @click="handleLogin('loginForm')"
          type="primary"
          class="submit-btn"
      >提交
      </el-button
      >
    </el-form-item>
    <!-- 找回密码 -->
    <el-form-item>
      <p class="tiparea">忘记密码<a>立即找回</a></p>
    </el-form-item>
  </el-form>
</template>

<script lang="ts">
import {getCurrentInstance} from 'vue';
import {registerRules, registerUser} from "@/utils/registerValidator";
import axios from 'axios';
import {ElMessage} from 'element-plus';
import router from "../router/index";
import {loginUser} from "@/utils/loginValidators";


export default {
  name: 'LoginForm',
  computed: {
    registerUser() {
      return registerUser
    },
  },
  props: {
    loginUser: {
      type: Object,
      required: true
    },
    rules: {
      type: Object,
      required: true
    }
  },
  setup() {
    // 通过解构getCurrentInstance，获取this，这里的this就是ctx
    // @ts-ignore
    const {ctx} = getCurrentInstance()
    // 触发登录方法
    const handleLogin = (formName: string) => {
      console.log(ctx);
      ctx.$refs[formName].validate((valid: boolean) => {
        if (valid) {
          console.log('submit!');
          axios
              .post('http://127.0.0.1:8000/api/login/', {
                name: ctx.loginUser.name,
                password: ctx.loginUser.password,
                role: ctx.loginUser.role
              }, {
                headers: {
                  'Content-Type': 'application/json'
                }
              })
              .then(response => {
                if (response.data.message === "登录成功") {
                  ElMessage({
                    message: "登陆成功！小主请开始您的购物之旅哟~",
                    type: "success",
                  });

                  localStorage.setItem('userName', ctx.loginUser.name);

                  if (ctx.loginUser.role === 'user') {
                    router.push({path: '/', query: {name: ctx.loginUser.name}});
                  } else if (ctx.loginUser.role === 'admin') {
                    router.push({path: '/admindashboards'});
                  }
                } else if (response.data.message === "用户名或密码错误") {
                  ElMessage.error("登陆失败！用户名或密码错误~");
                  console.log(ctx.loginUser.name);
                }
              })
              .catch(error => {
                console.error('Error:', error);
              });
        } else {
          console.log('error submit!');
          return false;
        }
      });
    };

    return{
      handleLogin
    };

  },

}
</script>

<style scoped>
/* register */
.login-form,
.register-form {
  position: absolute;
  top: auto;
  background-color: #fff;
  padding: 50px 80px 20px 20px;
  border-radius: 5px;
  box-shadow: 0px 5px 10px #cccc;
}

.submit-btn {
  width: 100%;
}

.tiparea {
  text-align: right;
  font-size: 12px;
  color: #333;
  width: 100%;
}

.tiparea a {
  color: #409eff;
}
</style>


