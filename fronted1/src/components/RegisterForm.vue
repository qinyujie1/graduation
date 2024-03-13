<template>
  <!-- 登录 -->
  <el-form
      :model="registerUser"
      :rules="registerRules"
      ref="registerForm"
      label-width="100px"
      class="register-form sign-up-form"
  >
    <el-form-item label="用户名" prop="name">
      <el-input v-model="registerUser.name" maxlength="20" show-word-limit name="name" placeholder="Enter Name..."/>
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input
          v-model="registerUser.password" name="password"
          type="password"
          placeholder="Enter Password..."
          show-password
      />
    </el-form-item>
    <el-form-item label="确认密码" prop="password2">
      <el-input
          v-model="registerUser.password2"
          type="password"
          placeholder="Enter Password again..."
          show-password
      />
    </el-form-item>
    <el-form-item label="角色" prop="role">
      <el-select v-model="registerUser.role">
        <el-option label="管理员" value="admin" name="role"></el-option>
        <el-option label="用户" value="user" name="role"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item>
      <el-button
          @click="handleRegister('registerForm')"
          type="primary"
          class="submit-btn"
      >提交
      </el-button
      >
    </el-form-item>
  </el-form>
</template>

<script lang="ts">
import {getCurrentInstance, ref} from 'vue'
import axios from "axios";
import { ElMessage } from 'element-plus';
import router from "../router/index";

export default {
  name: 'registerForm',
  props: {
    registerUser: {
      type: Object,
      required: true
    },
    registerRules: {
      type: Object,
      required: true
    }
  },
  setup() {
    // 通过解构getCurrentInstance，获取this，这里的this就是ctx
    // @ts-ignore
    const {ctx} = getCurrentInstance()
    // 触发登录方法
    const handleRegister = (formName: string) => {
      console.log(ctx)
      ctx.$refs[formName].validate((valid: boolean) => {
        if (valid) {
          console.log('submit!')
          axios
              .post("http://127.0.0.1:8000/api/register/", {
                name: ctx.registerUser.name,
                password: ctx.registerUser.password,
                role: ctx.registerUser.role
              })

              .then(response => {
                    console.log(response)
                    if (response.data.message == "注册成功") {
                      ElMessage({
                        message:'注册成功！小主可以登录啦~',
                        type:"success",
                      });
                    } else if (response.data.message == "该用户已存在") {
                      ElMessage.error("该用户已存在！小主请重新注册哦~")
                    }
                  }
              )
              .catch(function (error) {
                console.log(error)
              })
        } else {
          console.log('error register!')
          return false
        }
      })
    }
    return {handleRegister}
  }
}
</script>
<style scoped>
/* register */
.login-form,
.register-form {
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

.user-exist-error-message {
  color: red;
  margin-top: 8px;
}
</style>

