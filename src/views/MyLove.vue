<script lang="ts">
import { defineComponent } from 'vue';
import NavigationBar from "@/components/NavigationBar.vue";
import axios from "axios";
import { ElNotification } from 'element-plus';

export default defineComponent({
  name: "MyLove",
  components: { NavigationBar },
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
  },
});
</script>


<template>
  <NavigationBar></NavigationBar>

  <el-table :data="filterTableData">
      <el-table-column label="ID" prop="id" :align="'center'">
        <template #header="{column}">
          <div style="text-align: center;font-size: 17px;color: #333333;">
            {{ column.label }}
          </div>
        </template>
      </el-table-column>
      <el-table-column label="名字" prop="name" :align="'center'">
        <template #header="{column}">
          <div style="text-align: center;font-size: 17px;color: #333333;">
            {{ column.label }}
          </div>
        </template>
      </el-table-column>
      <el-table-column label="类型" prop="type" :align="'center'">
        <template #header="{column}">
          <div style="text-align: center;font-size: 17px;color: #333333;">
            {{ column.label }}
          </div>
        </template>
      </el-table-column>
      <el-table-column label="详情" prop="detail" :align="'center'">
        <template #header="{column}">
          <div style="text-align: center;font-size: 17px;color: #333333;">
            {{ column.label }}
          </div>
        </template>
      </el-table-column>
      <el-table-column label="图片" prop="img" class="column" :align="'center'">
        <template #header="{column}">
          <div style="text-align: center;font-size: 17px;color: #333333;">
            {{ column.label }}
          </div>
        </template>
        <template #default="{ row }" :align="'center'">
          <img :src="row.img" alt="Product Image" width="100" height="100"/>
        </template>
      </el-table-column>
      <el-table-column label="喜欢" prop="isLiked" :align="'center'">
        <template #header="{column}">
          <div style="text-align: center;font-size: 15px;font-size: 17px;color: #333333;">
            {{ column.label }}
          </div>
        </template>
        <template #default="{ row }">
          <img class="redLove" src="../assets/img/红爱心1.png">
        </template>
      </el-table-column>
  </el-table>
  <div class="recommend">
    <el-button plain @click="open1">
      生成报告
    <img src="../assets/img/点击.png">
    </el-button>
  </div>
</template>


<style scoped>

.el-table {
  position: absolute;
  top: 100px;
  left: 250px;
  width: 900px;
  text-align: center;
  font-size: 14px;
  color:#333333;
}

.redLove {
  width: 30px;

}

.column {
  text-align: center;
}
.recommend {
  position: fixed;
  bottom: 0px;
  right: 10px;
  width: 150px;
  z-index: 2;
  height: 40px;
}
.recommend .el-button {
  width: 150px;
  height: 40px;
  font-size: 15px;
}

.recommend img {
  width: 40px;

}
</style>