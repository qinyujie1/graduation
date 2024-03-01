<template>
  <navigation-bar></navigation-bar>
  <div v-if="filterTableData.length === 0" class="data">
    <p>Loading data...</p>
  </div>

  <div v-else class="data">
    <ul class="product-list">
    <li v-for="item in filterTableData" :key="item.id" class="product-item">
      <el-image :src="item.img" :fit="fit" class="product-image"></el-image>
      <div class="product-details">
        <p class="product-name">{{ item.name }}</p>
        <el-tag type="success">已有{{ item.id }}人购买</el-tag>
        <el-tag type="info">Price: {{ item.price }}</el-tag>
        <el-tag type="warning">生产地: {{ item.procity }}</el-tag>
        <el-tag type="danger">风格: {{ item.style }}</el-tag>
        <el-tag type="primary">适合年龄: {{ item.applicable_age }}</el-tag>
        <el-tag type="success">面料: {{ item.fabric }}</el-tag>
        <el-tag type="info">适合季节: {{ item.season }}</el-tag>
      </div>
    </li>
  </ul>
  </div>


</template>

<script lang="ts">

import NavigationBar from "@/components/NavigationBar.vue";
import {defineComponent} from "vue";
import axios from "axios";

export default defineComponent({
  name: 'Detail',
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
      // 获取服装 ID，这里假设服装 ID 是从 URL 参数中获取的
      const nid = this.$route.query.nid;
      console.log("nid=" + nid);

      axios
          .post(`http://127.0.0.1:8000/api/detail/${nid}/`)
          .then(response => {
            console.log("Response data:", response.data);

            // 将单个对象放入数组中
            this.filterTableData = [response.data];
          })
          .catch(error => {
            console.log("Error fetching data:", error);
          });


    }
  }
})

</script>


<style scoped>

.data {
  position: absolute;
  top: 100px;
  left: 300px;
}

.product-list {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  padding: 0;
}

.product-item {
  width: 600px;
  margin: 20px;
  padding: 20px;
  border-radius: 10px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.product-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}

.product-image {
  width: 100%;
  height: 400px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 15px;
}

.product-details {
  text-align: left;
}

.product-name {
  font-size: 20px;
  font-weight: bold;
}






</style>