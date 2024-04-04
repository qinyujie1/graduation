<template>
  <div>
    <AdminNavigationBar></AdminNavigationBar>

    <form @submit.prevent="updateUser" class="main">
      <div class="form-row">
        <label for="username">用户名:</label>
        <input type="text" id="username" v-model="editUserForm.username">
      </div>

      <div class="form-row">
        <label for="password">密码:</label>
        <input type="password" id="password" v-model="editUserForm.password">
      </div>

      <div class="form-row">
        <label for="role">角色:</label>
        <select id="role" v-model="editUserForm.role">
          <option label="管理员" value="admin"></option>
          <option label="用户" value="user"></option>
        </select>
      </div>

      <button type="submit">更新用户信息</button>
    </form>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref, onMounted} from 'vue';
import {useRouter} from 'vue-router';
import AdminNavigationBar from "@/components/AdminNavigationBar.vue";
import axios from "axios";
import {ElMessage} from "element-plus";

export default defineComponent({
  components: {AdminNavigationBar},
  name: "EditUser",
  setup() {
    const $router = useRouter();
    const editUserForm = ref({
      username: "",
      password: "",
      role: ""
    });
    const router = useRouter();
    const updateUser = () => {
      const userId = $router.currentRoute.value.query.userId;
      const userData = {
        name: editUserForm.value.username,
        password: editUserForm.value.password,
        role: editUserForm.value.role
      };

      axios
          .put(`http://127.0.0.1:8000/api/usermanage/${userId}/`, userData)
          .then(response => {
            // 更新表单数据
            editUserForm.value.username = response.data.name;
            editUserForm.value.password = response.data.password;
            editUserForm.value.role = response.data.role;
            ElMessage.success('您已成功更新用户信息！');
            router.push('/usermanage');
          })
          .catch(error => {
            console.error('Error:', error);
          });
    };

    onMounted(() => {
      const userId = $router.currentRoute.value.query.userId;
      axios
          .get(`http://127.0.0.1:8000/api/usermanage/${userId}/`)
          .then(response => {
            editUserForm.value.username = response.data.name;
            editUserForm.value.password = response.data.password;
            editUserForm.value.role = response.data.role;
          })
          .catch(error => {
            console.error('Error fetching user data:', error);
          });
    });

    return {
      editUserForm,
      updateUser
    };
  }
});
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border: 1px solid #ccc;
  width: 40%;
  margin-top: 100px;
  margin-left: 440px;
  height: 330px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
  padding: 20px;
  border-radius: 8px;
  align-content: space-around;
  flex-wrap: wrap;
  justify-content: space-evenly;
}

.main:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.form-row {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

label {
  margin-right: 10px;
  width: 86px;
}

input, select {
  padding: 8px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
}

input:focus, select:focus {
  outline: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #0056b3;
}
</style>
