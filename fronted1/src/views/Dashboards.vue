<template>
  <div>
    <NavigationBar></NavigationBar>
    <div class="chart-container">
      <div id="echarts" class="chart"></div>
      <div id="pie" class="chart"></div>
    </div>
  </div>
</template>

<script>
import { defineComponent, onMounted } from 'vue';
import axios from 'axios';
import * as echarts from 'echarts';
import NavigationBar from "@/components/NavigationBar.vue";

export default defineComponent({
  name: "Dashboards",
  components: { NavigationBar },
  setup() {
    onMounted(() => {
      fetchData();
      fetchData1();
    });

    const fetchData = () => {
      axios
        .get('http://127.0.0.1:8000/api/dashboards/')
        .then(response => {
          let myChart = echarts.init(document.getElementById('echarts'));

          myChart.setOption({
            title: { text: response.data.title.text },
            xAxis: response.data.xAxis,
            yAxis: response.data.yAxis,
            series: response.data.series
          });

          console.log(response);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    };

    const fetchData1 = () => {
      axios
        .get('http://127.0.0.1:8000/api/dashboards1/')
        .then(response => {
          let myChart = echarts.init(document.getElementById('pie'));

          myChart.setOption({
            series: response.data.series
          });

          console.log(response);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    };

    return { fetchData, fetchData1 };
  }
});
</script>

<style scoped>
.chart-container {
  margin-top: 80px;
}

#echarts {
  width: 500px;
  height: 460px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: absolute;
  left: 230px;
}
#pie {
  width: 500px;
  height: 460px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: absolute;
  right: 20px;
}
</style>

