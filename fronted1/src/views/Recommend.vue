<template>
  <div>
    <NavigationBar></NavigationBar>

    <div class="recommend">
      <ul class="clothes-list">
        <li v-for="(item, index) in data" :key="index" class="clothes-item">
          <img :src="item.pic" alt="Clothing Image" class="clothes-image">
          <div class="clothes-info">
            <div class="name" style="margin-bottom: 5px">{{ item.item_name }}</div>
            <div style="margin-bottom: 5px">
              <span style="font-size: 12px;margin-right: 10px;">风格</span>
              <el-tag v-if="item.style" type="danger">
                {{ item.style }}
              </el-tag>
            </div>
            <div style="margin-bottom: 5px">
              <span style="font-size: 12px;margin-right: 10px;">价格</span>
              <span style="font-size: 18px;color:red;">¥{{ item.price }}</span>
            </div>
            <div style="margin-bottom: 5px">
              <span style="font-size: 12px;margin-right: 10px;">购买人数</span>
              <el-tag v-if="item.real_sales" tyepe="info">{{ item.real_sales }}</el-tag>
            </div>
            <div style="margin-bottom: 5px">
              <span style="font-size: 12px;margin-right: 10px;">生产地</span>
              <el-tag v-if="item.procity" type="success">{{ item.procity }}</el-tag>
            </div>
            <div style="margin-bottom: 5px">
              <span style="font-size: 12px;margin-right: 10px;">适合年龄</span>
              <el-tag v-if="item.applicable_age" type="info">{{ item.applicable_age }}</el-tag>
            </div>
            <div style="margin-bottom: 5px">
              <span style="font-size: 12px;margin-right: 10px;">面料</span>
              <el-tag v-if="item.fabric" type="warning">{{ item.fabric }}</el-tag>
            </div>
            <div style="margin-bottom: 5px">
              <span style="font-size: 12px;margin-right: 10px;">适合季节</span>
              <el-tag v-if="item.season" type="success">{{ item.season }}</el-tag>
            </div>
            <div style="margin-bottom: 5px">
              <span style="font-size: 12px;margin-80right: 10px;margin-bottom: 8px;display: block;">
                推荐度
                <img src="../assets/img/zan.png" style="width: 30px">
              </span>
              <span style="font-size: 20px;font-weight: bold;color:red;">{{ item.average_similarity }}</span>
            </div>
          </div>
        </li>
      </ul>
    </div>


  </div>
</template>


<script>
import {defineComponent, ref, onMounted} from "vue";
import axios from "axios";
import NavigationBar from "@/components/NavigationBar.vue";

export default defineComponent({
  name: "Recommend",
  components: {
    NavigationBar
  },
  setup() {
    const data = ref([]);
    onMounted(() => {
      axios.post("http://127.0.0.1:8000/api/recommend/")
          .then(response => {
            const recommendations = response.data;
            data.value = recommendations;
            console.log(data.value)
          })
          .catch(error => {
            console.error(error);
          });
    });

    return {
      data // 将 data 变量暴露给模板
    };
  }
});

</script>


<style scoped>
.recommend {
  position: absolute;
  top: 70px;
  left: 210px;
}

.clothes-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  list-style: none;
}

.clothes-item {
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 5px;
}

.clothes-image {
  width: 100%;
  height: auto;
  border-radius: 5px;
}

.clothes-info {
  margin-top: 10px;
}

@media (max-width: 768px) {
  .clothes-list {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  }
}

.name {
  line-height: 20px;
  font-size: 12px;
  color: var(--el-color-success);
  background-color: var(--el-color-success-light-9);
  border: 1px solid var(--el-color-success-light-8);
}

</style>
