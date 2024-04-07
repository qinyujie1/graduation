<script>
import {defineComponent, onMounted, ref} from "vue";
import AdminNavigationBar from "@/components/AdminNavigationBar.vue";
import {useRouter} from "vue-router";
import axios from "axios";


export default defineComponent({
  components: {AdminNavigationBar},
  name:"InventoryManagement",
  setup() {
    const cloth = ref([]);
    const currentPage = ref(1); // 当前页码
    const totalPages = ref(1); // 总页数
    const $router = useRouter();
    const fetchData = (page) => {
      axios
          .get(`http://127.0.0.1:8000/api/inventory_management/?page=${page}`)
          .then(response => {
            cloth.value = response.data.results;
            totalPages.value = response.data.total_pages;
          })
          .catch(error => {
            console.error('Error:', error);
          });
    };

    const deleteUser = (clothId) => {
      axios
          .delete(`http://127.0.0.1:8000/api/inventory_management/${clothId}/`)
          .then(response => {
            fetchData(currentPage.value);
          })
          .catch(error => {
            console.error('Error:', error);
          });
    };

    const editUser = (clothId) => {
      $router.push({path: '/editinventory', query: {clothId}});
    };

    const handleSizeChange = (val) => {
      // 处理每页显示条数变化
      // 可以在这里更新每页显示的数据条数并重新请求数据
    };

    const handleCurrentChange = (val) => {
      // 处理当前页码变化
      currentPage.value = val;
      fetchData(val);
    };

    onMounted(() => {
      fetchData(currentPage.value);
    });

    return {
      cloth,
      currentPage,
      totalPages,
      deleteUser,
      editUser,
      handleSizeChange,
      handleCurrentChange
    };
  }
});
</script>
<template>
  <AdminNavigationBar></AdminNavigationBar>
  <div class="main">
    <!-- 触发新增用户对话框的按钮 -->
    <el-button type="primary" @click="$router.push('/createinventory')" style="margin-left: 40px">Create Cloth
    </el-button>

    <transition name="fade">
      <el-table :data="cloth" stripe style="width: 1000px" class="table">
        <el-table-column label="名字" prop="name" :align="'center'">
          <template #default="{ row }">
            <el-tag type="success">
              {{ row.name }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="类型" prop="type" :align="'center'">
          <template #default="{ row }">
            <el-tag type="danger" v-if="row.type">
              {{ row.type }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="图片" prop="img" class="column" :align="'center'">
          <template #default="{ row }">
            <div class="table-cell">
              <img :src="row.img" alt="Product Image" width="100" height="100"/>
            </div>
          </template>
        </el-table-column>
        <el-table-column label="生产地" prop="procity" :align="'center'">
          <template #default="{ row }">
            <el-tag type="danger" v-if="row.procity">
              {{ row.procity }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="适用年龄" prop="applicable_age" :align="'center'">
          <template #default="{ row }">
            <el-tag type="info" v-if="row.applicable_age">
              {{ row.applicable_age }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="面料" prop="fabric" :align="'center'">
          <template #default="{ row }">
            <el-tag type="danger" v-if="row.fabric">
              {{ row.fabric }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="适用季节" prop="season" :align="'center'">
          <template #default="{ row }">
            <el-tag v-if="row.season" type="warning" style="width:74px;">
              {{ row.season }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="价格" prop="price" :align="'center'">
          <template #default="{ row }">
            <div class="table-cell-price">
              ¥{{ row.price }}
            </div>
          </template>
        </el-table-column>
        <el-table-column label="Actions">
          <template #default="{ row }">
            <!-- 触发编辑用户对话框的按钮 -->
            <div class="action-buttons">
              <el-button type="success" @click="editUser(row.id)" size="small">Edit</el-button>
              <el-button type="danger" @click="deleteUser(row.id)" size="small">Delete</el-button>
            </div>
          </template>
        </el-table-column>
      </el-table>
    </transition>

    <!-- 分页按钮 -->
    <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[20]"
        :page-size="20"
        layout="total, sizes, prev, pager, next, jumper"
        :total="totalPages"
        :pager="auto"
    :page-count="totalPages"
    style="border-radius: 8px; font-size: 15px;">
    </el-pagination>
  </div>
</template>

<style scoped>
.main {
  margin-left: 186px;
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

.el-pagination {
  position: fixed;
  bottom: 10px;
  z-index: 999;
  margin-left: 150px;
  font-size: 20px;
  height: 40px;
  line-height: 40px;
}

.action-buttons {
  display: flex;
  width: 125px;
  padding-left: 0;
  margin-left: -8px;
}

.action-buttons .el-button {
  margin-right: -6px; /* 可以根据需要调整按钮之间的间距 */
}

.el-button--small {
  --el-button-size: 24px;
  height: var(--el-button-size);
  padding: 5px 9px;
  font-size: 12px;
  border-radius: calc(var(--el-border-radius-base) - 1px);
}

.table-cell-price {
  text-align: center;
  font-size: 16px;
  color: red;
}

.table {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

.el-table {
  margin-left: 60px;
  margin-top: 20px;
}

</style>
