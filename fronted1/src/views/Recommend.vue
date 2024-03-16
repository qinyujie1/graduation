<template>
  <div>
    <NavigationBar></NavigationBar>

    <div class="recommend">
      <ul class="clothes-list">
        <li v-for="(item, index) in data" :key="index" class="clothes-item">
          <img :src="item.pic" alt="Clothing Image" class="clothes-image">
          <div class="clothes-info">
            <h3>{{ item.item_name }}</h3>
            <p>Style: {{ item.style }}</p>
            <p>Price: {{ item.price }}</p>
            <p>Real Sales: {{ item.real_sales }}</p>
            <p>Procity: {{ item.procity }}</p>
            <p>Applicable Age: {{ item.applicable_age }}</p>
            <p>Fabric: {{ item.fabric }}</p>
            <p>Season: {{ item.season }}</p>
            <p>推荐度: {{ item.average_similarity }}</p>
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
  top: 180px;
  left: 300px;
}

.recommend {
  padding: 20px;
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
</style>
