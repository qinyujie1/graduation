<script lang="ts">
import {defineComponent} from 'vue';
import NavigationBar from "@/components/NavigationBar.vue";
import axios from "axios";
import {ElMessage, ElNotification} from 'element-plus';

export default defineComponent({
  name: "MyLove",
  components: {NavigationBar},
  data() {
    return {
      filterTableData: [] as any[],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios
          .get("http://127.0.0.1:8000/api/mylove/")
          .then(response => {
            this.filterTableData = response.data.map((item: any, index: number) => {
              return {
                ...item,
                id: index + 1
              };
            });
          })
          .catch(error => {
            console.log(error);
          });
    },
    // 其他方法
    open1() {
      ElNotification({
        title: 'Success',
        message: '生成推荐报告成功哦~',
        type: 'success',
      });
    },
    open2() {
      ElMessage({
        message: '生成推荐成功~',
        type: 'success',
        onClose: () => {
          // 在消息关闭后进行页面跳转
          this.$router.push('/recommend');
        },
      });
    },
  },
});

</script>


<template>
  <NavigationBar></NavigationBar>
  <el-breadcrumb separator="/">
    <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
    <el-breadcrumb-item>
      <a href="/mylove/">我的喜欢</a>
    </el-breadcrumb-item>
  </el-breadcrumb>
  <el-table :data="filterTableData">
    <el-table-column label="ID" prop="id" :align="'center'">
      <template #header="{column}">
        <div class="table-header">
          {{ column.label }}
        </div>
      </template>
    </el-table-column>
    <el-table-column label="名字" prop="name" :align="'center'">
      <template #default="{ row }">
        <el-tag type="success" >
          {{ row.name }}
        </el-tag>
      </template>
    </el-table-column>
    <el-table-column label="类型" prop="type" :align="'center'">
      <template #default="{ row }">
        <el-tag type="danger" v-if="row.type" >
          {{ row.type }}
        </el-tag>
      </template>
    </el-table-column>
    <el-table-column label="购买人数" prop="real_sales" :align="'center'">
      <template #default="{ row }">
        <el-tag v-if="row.real_sales" type="info" style="width:78px">
          {{ row.real_sales }}
        </el-tag>
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
        <el-tag v-if="row.season" type="warning"  style="width:74px;">
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

    <el-table-column label="图片" prop="img" class="column" :align="'center'">
      <template #default="{ row }">
        <div class="table-cell">
          <img :src="row.img" alt="Product Image" width="100" height="100"/>
        </div>
      </template>
    </el-table-column>
    <el-table-column label="喜欢" prop="isLiked" :align="'center'">
      <template #default="{ row }">
        <div class="table-cell">
          <img class="redLove" src="../assets/img/红爱心1.png">
        </div>
      </template>
    </el-table-column>
  </el-table>
  <router-link to="/recommend">
    <div class="recommend">
      <p>
        <el-button :plain="true" @click="open2">
          生成报告
        </el-button>
      </p>
      <img src="../assets/img/点击.png">
    </div>
  </router-link>
</template>

<style scoped>
.el-breadcrumb {
  position: absolute;
  top: 85px;
  left: 250px;
  font-size: 16px;
}

.el-table {
  position: absolute;
  top: 120px;
  left: 250px;
  width: 980px;
  font-size: 12px;
  color: #333333;
  border: 1px solid #ccc;
  border-collapse: collapse;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  border-radius: 20px;
}

.el-table th {
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  padding: 8px;
}

.el-table td {
  border: 1px solid #ccc;
  padding: 8px;
}

.table-header {
  text-align: center;
  font-size: 14px;
  color: #333333;
}

.table-cell {
  text-align: center;
  font-size: 14px;
  color: #333333;
}

.table-cell-price {
  text-align: center;
  font-size: 16px;
  color: red;
}

.table-cell-wide {
  text-align: center;
  font-size: 14px;
  color: #333333;
  width: 82px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.redLove {
  width: 30px;
}

.recommend {
  position: fixed;
  bottom: 20px;
  right: 10px;
  z-index:999;
}

.recommend .el-button {
  width: 150px;
  height: 40px;
  font-size: 16px;
  border: 1px solid #313743;
  background-color: #f5f5f5;
}

.recommend img {
  width: 40px;
  position: absolute;
  bottom: 0;
  right: 0;
}


.table-header {
    text-align: center;
    font-size: 12px;
    color: #333333;
    font-weight: bold;
}


</style>

