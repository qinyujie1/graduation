<template>
  <div>
    <AdminNavigationBar></AdminNavigationBar>

    <form @submit.prevent="updateUser" class="main">
      <label for="username">用户名:</label>
      <input type="text" id="username" v-model="editUserForm.username">

      <label for="password">密码:</label>
      <input type="password" id="password" v-model="editUserForm.password">

      <label for="role">角色:</label>
      <select id="role" v-model="editUserForm.role">
        <option label="管理员" value="admin"></option>
        <option label="用户" value="user"></option>
      </select>
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


function fetchData(userId: import("vue-router").LocationQueryValue | import("vue-router").LocationQueryValue[]) {
  throw new Error('Function not implemented.');
}
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid #ccc;
  width: 40%;
  margin-top: 140px;
  margin-left: 440px;
  height: 330px;
}

label {
  margin-top: 20px;
}

input {
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 5px;
  width: 200px;
}

button {
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

select{
  width: 210px;
  height: 30px;
}
</style>
