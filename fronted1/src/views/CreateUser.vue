<template>
  <div>
    <AdminNavigationBar></AdminNavigationBar>
    <el-form :model="newUserForm" ref="newUserForm" label-width="80px" class="main">
      <el-form-item label="Name" prop="name">
        <input type="text" v-model="newUserForm.name"></input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <input type="password" v-model="newUserForm.password"></input>
      </el-form-item>
      <el-form-item label="Role" prop="role">
        <select v-model="newUserForm.role" placeholder="Select role">
          <option label="管理员" value="admin"></option>
          <option label="用户" value="user"></option>
        </select>
      </el-form-item>
      <el-form-item class="create">
        <el-button type="primary" size="large" @click="createUser">确认</el-button>
      </el-form-item>

    </el-form>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue';
import axios from 'axios';
import AdminNavigationBar from '@/components/AdminNavigationBar.vue';
import {ElMessage} from 'element-plus';
import {useRouter} from "vue-router";

export default defineComponent({
  components: {AdminNavigationBar},
  name: "CreateUser",
  setup() {
    const newUserForm = ref({
      name: '',
      password: '',
      role: ''
    });

    const router = useRouter();

    const createUser = () => {
      axios
          .post('http://127.0.0.1:8000/api/usermanage/', newUserForm.value)
          .then(response => {
            console.log('User created successfully:', response.data);
            ElMessage.success('您已成功创建新用户！');
            router.push('/usermanage');
          })
          .catch(error => {
            console.error('Error creating user:', error);
          });
    };


    return {
      newUserForm,
      createUser,
    };
  }
});

</script>

<style scoped>
.main {
  width: 70%;
  position: absolute;
  top: 80px;
  left: 270px;
  right: 50px;
  border: 1px solid #ccc; /* 添加边框 */
  padding: 20px; /* 添加内边距 */
}

/* 标签样式 */
.el-form-item__label {
  font-weight: bold;
}

/* 输入框样式 */
input[type="text"],
input[type="password"] {
  width: 88%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

select {
  width: 90%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

/* 按钮样式 */
.el-button {
  margin-top: 10px;
  font-size: 18px;
}


.create {
  margin-left: 30%;
}
</style>
