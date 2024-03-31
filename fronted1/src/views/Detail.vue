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
          <div class="people">已售{{ item.id }}件</div>
          <div type="info" class="sale">
            <span class="shoujia1">售价</span>
            <span class="shoujia2">¥{{ item.price }}</span>
          </div>
          <div type="warning" class="sale">
            <span class="shoujia1">生产地</span>
            <span style="font-weight: bold;">{{ item.procity }}</span>
          </div>
          <div class="sale">
            <span class="shoujia1">风格</span>
            <el-tag v-if="item.style" type="danger">{{ item.style }}</el-tag>
          </div>
          <div type="primary" class="sale">
            <span class="shoujia1">适合年龄</span>
            <span style="font-weight: bold;">{{ item.applicable_age }}</span>
          </div>
          <div class="sale">
            <span class="shoujia1">面料</span>
            <el-tag type="success">{{ item.fabric }}</el-tag>
          </div>
          <div class="sale">
            <span class="shoujia1">适合季节</span>
            <el-tag type="info">{{ item.season }}</el-tag>
          </div>
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
  top: 80px;
  left: 250px;
}

.product-list {
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  padding: 0;
}

.product-item {
  width: 400px;
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
  position: absolute;
  left: 500px;
  width: 480px;
  top: 70px;
}

.product-name {
  font-size: 20px;
  font-weight: bold;
  display: block;
  margin-bottom: 15px;
}

.people {
  position: absolute;
  right: 0px;
  color: grey;
  font-size: 12px;
}

.shoujia1 {
  font-size: 15px;
  color: grey;
  padding-right: 10px;
}

.shoujia2 {
  color: red;
  font-size: 22px;
  font-weight: bold;
}

.sale {
  margin: 15px;
}
</style>