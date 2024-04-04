<template>
  <div>
    <AdminNavigationBar></AdminNavigationBar>
    <div class="main">
      <!-- 触发新增用户对话框的按钮 -->
      <el-button type="primary" @click="$router.push('/createuser')" style="margin-left: 40px">Create User</el-button>

      <transition name="fade">
        <el-table :data="users" stripe style="width: 900px" class="table">
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
      </transition>
    </div>
  </div>
</template>

<script>
import { defineComponent, onMounted, ref } from "vue";
import AdminNavigationBar from "@/components/AdminNavigationBar.vue";
import axios from "axios";
import { useRouter } from "vue-router";

export default defineComponent({
  components: {
    AdminNavigationBar
  },
  name: "UserManage",
  setup() {
    const users = ref([]);

    const $router = useRouter();

    onMounted(() => {
      fetchData();
    });

    const fetchData = () => {
      axios
        .get('http://127.0.0.1:8000/api/usermanage/')
        .then(response => {
          users.value = response.data;
          console.log(users.value);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    };

    const deleteUser = (userId) => {
      axios
        .delete(`http://127.0.0.1:8000/api/usermanage/${userId}/`)
        .then(response => {
          fetchData();
        })
        .catch(error => {
          console.error('Error:', error);
        });
    };

    const editUser = (userId) => {
      $router.push({ path: '/edituser', query: { userId } });
    };

    return {
      users,
      deleteUser,
      editUser
    };
  }
});
</script>

<style scoped>
.main {
  margin-left: 220px;
  margin-top: 80px;
}

.table {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

.el-table {
    margin-left: 60px;
    margin-top: 20px;
}
</style>
