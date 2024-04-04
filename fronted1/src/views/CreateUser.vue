<template>
  <div>
    <AdminNavigationBar></AdminNavigationBar>
    <el-form :model="newUserForm" ref="newUserForm" label-width="80px" class="main">
      <el-form-item label="Name" prop="name">
        <input type="text" v-model="newUserForm.name" class="input-field"></input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <input type="password" v-model="newUserForm.password" class="input-field"></input>
      </el-form-item>
      <el-form-item label="Role" prop="role">
        <select v-model="newUserForm.role" class="select-field">
          <option value="admin">管理员</option>
          <option value="user">用户</option>
        </select>
      </el-form-item>
      <el-form-item class="create">
        <el-button type="primary" size="large" @click="createUser">确认</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import axios from 'axios';
import AdminNavigationBar from '@/components/AdminNavigationBar.vue';
import { ElMessage } from 'element-plus';
import { useRouter } from "vue-router";

export default defineComponent({
  components: { AdminNavigationBar },
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
  top: 120px;
  left: 270px;
  right: 50px;
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
}

.main:hover {
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}

.el-form-item__label {
  font-weight: bold;
}

.input-field,
.select-field {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.select-field {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-position: right 10px top 50%;
  background-size: 1em;
}

.el-button {
  margin-top: 20px;
  font-size: 18px;
  width: 100%;
}

.create {
  text-align: center;
}
</style>
