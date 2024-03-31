<template>
  <div>
    <AdminNavigationBar></AdminNavigationBar>
    <div class="main">
      <!-- 触发新增用户对话框的按钮 -->
      <el-button type="primary" @click="$router.push('/createuser')">Create User</el-button>

      <el-table :data="users" stripe style="width: 100%">
        <el-table-column prop="name" label="Name"/>
        <el-table-column prop="password" label="Password"/>
        <el-table-column prop="role" label="Role"/>
        <el-table-column label="Actions">
          <template #default="{ row }">
            <!-- 触发编辑用户对话框的按钮 -->
            <el-button type="success" @click="editUser(row.id)">Edit</el-button>
            <el-button type="danger" @click="deleteUser(row.id)">Delete</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>


<script lang="ts">
import {defineComponent, onMounted, reactive, ref, toRef, toRefs} from "vue";
import AdminNavigationBar from "@/components/AdminNavigationBar.vue";
import {
  ElDialog,
  ElButton,
  ElTable,
  ElTableColumn,
  ElForm,
  ElFormItem,
  ElInput,
  ElSelect,
  ElOption
} from 'element-plus';
import axios from "axios";
import { useRouter } from "vue-router";

export default defineComponent({
  components: {
    AdminNavigationBar,
    ElDialog,
    ElButton,
    ElTable,
    ElTableColumn,
    ElForm,
    ElFormItem,
    ElInput,
    ElSelect,
    ElOption
  },
  name: "UserManage",
  setup() {
    const users = ref([]);
    const newUserForm = reactive({
      name: '',
      password: '',
      role: ''
    });
    const currentUser = ref(null);

    const $router = useRouter();
    const editUser = (userId:any) => {
      $router.push({ path: '/edituser', query: { userId } });
    };
     const { editUser: boundEditUser } = toRefs({ editUser });

    onMounted(() => {
      fetchData();
    });

    const fetchData = () => {
      axios
          .get('http://127.0.0.1:8000/api/usermanage/')
          .then(response => {
            users.value = response.data;
            console.log(users.value)
          })
          .catch(error => {
            console.error('Error:', error);
          });
    };


    const deleteUser = (userId:any) => {
      axios
          .delete(`http://127.0.0.1:8000/api/usermanage/${userId}/`)
          .then(response => {
            fetchData();
          })
          .catch(error => {
            console.error('Error:', error);
          });
    };

    return {
      users,
      newUserForm,
      editUser: boundEditUser,
      currentUser,
      deleteUser
    };
  }
})
</script>


<style scoped>
.main {
  margin-left: 220px;
  margin-top: 80px;
}


</style>
