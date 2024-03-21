<script lang="ts">
import {defineComponent, onMounted, ref} from "vue";
import AdminNavigationBar from "@/components/AdminNavigationBar.vue";
import axios from "axios";
import * as echarts from "echarts";

export default defineComponent({
  name: "AdminDashboards",
  components: {AdminNavigationBar},
  setup() {
    const totalSales = ref(0);
    const totalPeople = ref(0);
    const totalCloth = ref(0);
    onMounted(() => {
      fetchData();
      fetchData1();
      fetchData2();
      fetchData3();
    });

    const fetchData = () => {
      axios
          .get('http://127.0.0.1:8000/api/dashboards2/')
          .then(response => {
            let myChart = echarts.init(document.getElementById('echarts'));

            myChart.setOption({
              xAxis: {
                type: 'category',
                data: response.data.xAxis,
                axisLabel: {
                  interval: 0,
                  rotate: 45
                },
                axisPointer: {
                  type: 'shadow'
                }
              },
              yAxis: {
                type: 'value'
              },
              series: [
                {
                  data: response.data.series[0].data,
                  type: 'bar',
                  itemStyle: {
                    color: '#313743' // 设置柱状图颜色为 #313743
                  }
                }
              ],
              dataZoom: [
                {
                  type: 'slider',
                  start: 0,
                  end: 100
                }
              ]
            });
            console.log(response);
          })
          .catch(error => {
            console.error('Error:', error);
          });
    };
    const fetchData1 = () => {
      axios
          .get('http://127.0.0.1:8000/api/dashboards3/')
          .then(response => {
            totalSales.value = response.data.total_sales;
            // 在这里可以调用函数或者更新页面其他内容，使用接收到的 totalSales 数据
            console.log(response);
          })
          .catch(error => {
            console.error('Error:', error);
          });
    };
    const fetchData2 = () => {
      axios
          .get('http://127.0.0.1:8000/api/dashboards4/')
          .then(response => {
            totalPeople.value = response.data.total_people;
            // 在这里可以调用函数或者更新页面其他内容，使用接收到的 totalSales 数据
            console.log(response);
          })
          .catch(error => {
            console.error('Error:', error);
          });
    };
    const fetchData3 = () => {
      axios
          .get('http://127.0.0.1:8000/api/dashboards5/')
          .then(response => {
            totalCloth.value = response.data.total_cloth;
            // 在这里可以调用函数或者更新页面其他内容，使用接收到的 totalSales 数据
            console.log(response);
          })
          .catch(error => {
            console.error('Error:', error);
          });
    };

    return {
      totalSales, totalPeople, totalCloth
    };
  }
})
</script>

<template>
  <AdminNavigationBar></AdminNavigationBar>
  <div class="dashboard-container">
    <div class="totalsales">Total Sales: {{ totalSales }}</div>
    <div class="totalpeople">Total People: {{ totalPeople }}</div>
    <div class="totalcloth">Total People: {{ totalCloth }}</div>
    <div id="echarts" class="chart"></div>
  </div>
</template>

<style scoped>
.dashboard-container {
  margin: 20px;
  padding: 20px;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.totalsales {
  margin-top: 40px;
  font-size: 24px;
  margin-left: 220px;
}

.totalpeople {
  margin-top: -24px;
  font-size: 24px;
  margin-left: 550px;
}
.totalcloth {
  margin-top: -24px;
  font-size: 24px;
  margin-left: 870px;
}

.chart {
  margin-top: 20px;
  width: 80%;
  height: 400px;
  margin-left: 220px;

}
</style>
