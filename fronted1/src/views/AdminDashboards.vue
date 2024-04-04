<template>
  <AdminNavigationBar></AdminNavigationBar>
  <div class="dashboard-container">
    <div class="dashboard-info">
      <div class="info-item">
        <div class="info-label">Total Sales:</div>
        <div class="info-value" v-loading="loading1">{{ totalSales }}</div>
      </div>
      <div class="info-item">
        <div class="info-label">Total People:</div>
        <div class="info-value" v-loading="loading2">{{ totalPeople }}</div>
      </div>
      <div class="info-item">
        <div class="info-label">Total Cloth:</div>
        <div class="info-value" v-loading="loading3">{{ totalCloth }}</div>
      </div>
    </div>
    <div id="echarts" class="chart" v-loading="loading"></div>
  </div>
</template>

<script setup lang="ts">
import {onMounted, ref} from 'vue'
import axios from 'axios'
import * as echarts from 'echarts'
import AdminNavigationBar from "@/components/AdminNavigationBar.vue";

const totalSales = ref(0)
const totalPeople = ref(0)
const totalCloth = ref(0)
const loading = ref(true)
const loading1 = ref(true);
const loading2 = ref(true);
const loading3 = ref(true);


onMounted(() => {
  fetchData()
  fetchData1()
  fetchData2()
  fetchData3()
})

const fetchData = () => {
  axios.get('http://127.0.0.1:8000/api/dashboards2/')
    .then(response => {
      let myChart = echarts.init(document.getElementById('echarts'))

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
              color: '#007bff' // 设置柱状图颜色为蓝色
            },
          }
        ],
        dataZoom: [
          {
            type: 'slider',
            start: 0,
            end: 100
          }
        ],
        title: response.data.title
      })
      loading.value=false;
      console.log(response)
    })
    .catch(error => {
      console.error('Error:', error);
      loading.value=false;
    })
}

const fetchData1 = () => {
  axios.get('http://127.0.0.1:8000/api/dashboards3/')
    .then(response => {
      totalSales.value = response.data.total_sales
      console.log(response);
      loading1.value=false;
    })
    .catch(error => {
      console.error('Error:', error);
      loading1.value=false;
    })
}

const fetchData2 = () => {
  axios.get('http://127.0.0.1:8000/api/dashboards4/')
    .then(response => {
      totalPeople.value = response.data.total_people
      console.log(response);
      loading2.value=false;
    })
    .catch(error => {
      console.error('Error:', error);
      loading2.value=false;
    })
}

const fetchData3 = () => {
  axios.get('http://127.0.0.1:8000/api/dashboards5/')
    .then(response => {
      totalCloth.value = response.data.total_cloth;
      console.log(response);
      loading3.value=false;
    })
    .catch(error => {
      console.error('Error:', error);
      loading3.value=false;
    })
}

</script>

<style scoped>
.dashboard-container {
  padding: 20px;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-top: 80px;
  margin-left: 200px;
  margin-right: 20px;
}

.dashboard-info {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.info-item {
  text-align: center;
}

.info-label {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.info-value {
  font-size: 24px;
  color: #007bff; /* 蓝色字体 */
  font-weight: bold;
}

.chart {
  width: 90%;
  height: 400px;
  margin: 20px auto;
  background-color: #f9f9f9; /* 与容器背景色一致 */
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.el-table {
  margin-top: 20px;
}
</style>
