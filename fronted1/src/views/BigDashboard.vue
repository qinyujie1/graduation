<template>
  <header>
  <router-link to="/usermanage">
    <span style="color: #FFFFFF;font-size: 15px;"><-返回</span>
  </router-link>
    <h1>服装数据分析可视化大屏</h1>
  </header>
  <section class="mainbox">
    <div class='column'>
      <div class="panel bar">
        <h2>不同风格的购买人数TOP5</h2>
        <div class="chart" id="left1" v-loading="loading4"></div>
        <div class="panel-footer"></div>
      </div>
      <div class="panel bar">
        <h2>适合年龄服装矩树图</h2>
        <div class="chart" id="left2" v-loading="loading6"></div>
        <div class="panel-footer"></div>
      </div>
      <div class="panel bar">
        <h2>不同季节购买人数雷达图</h2>
        <div class="chart" id="left3" v-loading="loading8"></div>
        <div class="panel-footer"></div>
      </div>

    </div>

    <div class='column'>
      <div class="no">
        <div class="no-hd">
          <ul>
            <li v-loading="loading1">{{ totalSales }}</li>
            <li v-loading="loading2">{{ totalPeople }}</li>
          </ul>
        </div>
        <div class="no-bd">
          <ul>
            <li>销售总额</li>
            <li>销售人数</li>
          </ul>
          <h2>地区销售金额</h2>
        </div>
      </div>
      <div class="map">
        <div class="chart" id="echarts" v-loading="loading"></div>
        <div class="chart-footer" id="echarts"></div>
      </div>
      <div class="run">
        <h2>不同风格服装占比</h2>
        <div class="run1" id="run11" v-loading="loading3" style="height: 500px"></div>
        <div class="run1-footer" id="run11"></div>
      </div>
    </div>
    <div class='column'>
      <div class="panel bar">
        <h2>服装价格TOP5</h2>
        <div class="chart" id="right1" v-loading="loading5"></div>
        <div class="panel-footer"></div>
      </div>

      <div class="panel bar">
        <h2>用户喜欢服装面料</h2>
        <div class="chart" id="right2" v-loading="loading7"></div>
        <div class="panel-footer"></div>
      </div>
      <div class="panel bar">
        <h2>用户喜欢风格占比</h2>
        <div class="chart" id="right3" v-loading="loading9"></div>
        <div class="panel-footer"></div>
      </div>
    </div>
  </section>

</template>

<script lang="ts">
import {defineComponent, onMounted, ref} from "vue";
import AdminNavigationBar from "@/components/AdminNavigationBar.vue";
import {useRouter} from "vue-router";
import axios from "axios";
import {ElMessage} from "element-plus";
import * as echarts from "echarts";
import 'echarts-wordcloud'; // 引入 echarts-wordcloud 插件

export default defineComponent({
      components: {AdminNavigationBar},
      name: "BigDashboard",
      setup() {
        const totalSales = ref(0);
        const totalPeople = ref(0);
        const loading = ref(true)
        const loading1 = ref(true);
        const loading2 = ref(true);
        const loading3 = ref(true);
        const loading4 = ref(true);
        const loading5 = ref(true);
        const loading6 = ref(true);
        const loading7 = ref(true);
        const loading8 = ref(true);
        const loading9 = ref(true);


        onMounted(() => {
          fetchData();
          fetchData1();
          fetchData2();
          fetchData3();
          fetchData4();
          fetchData5();
          fetchData6();
          fetchData7();
          fetchData8();
          fetchData9();
        });

        const fetchData = () => {
          axios.get('http://127.0.0.1:8000/api/dashboards2/')
              .then(response => {
                let myChart = echarts.init(document.getElementById('echarts'));

                var option = {
                  tooltip: {
                    trigger: "axis",
                    axisPointer: {
                      type: "shadow",
                    },
                  },
                  grid: {
                    top: "10%",
                    right: "5%",
                    left: "5%",
                    bottom: "10%",
                  },
                  xAxis: [
                    {
                      type: "category",
                      data: response.data.xAxis,
                      axisLine: {
                        lineStyle: {
                          color: "rgba(66, 192, 255, .3)",
                        },
                      },
                      axisLabel: {
                        interval: 0,
                        margin: 10,
                        color: "#05D5FF",
                        textStyle: {
                          fontSize: 11,
                        },
                      },
                      axisTick: {
                        show: false,
                      },
                    },
                  ],
                  yAxis: [
                    {
                      axisLabel: {
                        padding: [3, 0, 0, 0],
                        formatter: "{value}",
                        color: "rgba(95, 187, 235, 1)",
                        textStyle: {
                          fontSize: 11,
                        },
                      },
                      axisTick: {
                        show: true,
                      },
                      axisLine: {
                        lineStyle: {
                          color: "rgba(66, 192, 255, .3)",
                        },
                      },
                      splitLine: {
                        lineStyle: {
                          color: "rgba(255,255,255,0)",
                        },
                      },
                    },
                  ],
                  dataZoom: [
                    {
                      show: true,
                      type: "slider",
                      realtime: true,
                      startValue: 0,
                      endValue: 14,
                      xAxisIndex: [0],
                      bottom: "10",
                      left: "30",
                      height: 10,
                      borderColor: "rgba(0,0,0,0)",
                      textStyle: {
                        color: "#05D5FF",
                      },
                    },
                  ],
                  series: [
                    {
                      name: "销售额",
                      type: "bar",
                      data: response.data.series[0].data,
                      barWidth: "10",
                      itemStyle: {
                        normal: {
                          color: new echarts.graphic.LinearGradient(
                              0,
                              0,
                              0,
                              1,
                              [
                                {
                                  offset: 0,
                                  color: "rgba(5, 213, 255, 1)",
                                },
                                {
                                  offset: 0.98,
                                  color: "rgba(5, 213, 255, 0)",
                                },
                              ],
                              false
                          ),
                          shadowColor: "rgba(5, 213, 255, 1)",
                          shadowBlur: 4,
                        },
                      },
                      label: {
                        normal: {
                          show: true,
                          lineHeight: 10,
                          formatter: "{c}",
                          position: "top",
                          textStyle: {
                            color: "#fff",
                            fontSize: 10,
                          },
                        },
                      },
                    },
                  ],
                };

                myChart.setOption(option);
                loading.value = false;
                console.log(response);
              })
              .catch(error => {
                console.error('Error:', error);
                loading.value = false;
              });
        };


        const fetchData1 = () => {
          axios.get('http://127.0.0.1:8000/api/dashboards3/')
              .then(response => {
                totalSales.value = response.data.total_sales;
                console.log(response);
                loading1.value = false;
              })
              .catch(error => {
                console.error('Error:', error);
                loading1.value = false;
              });
        };

        const fetchData2 = () => {
          axios.get('http://127.0.0.1:8000/api/dashboards4/')
              .then(response => {
                totalPeople.value = response.data.total_people;
                console.log(response);
                loading2.value = false;
              })
              .catch(error => {
                console.error('Error:', error);
                loading2.value = false;
              });
        };

        const fetchData3 = () => {
          axios
              .get('http://127.0.0.1:8000/api/dashboards/')
              .then(response => {
                let myChart = echarts.init(document.getElementById('left1'));

                myChart.setOption({
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
        const fetchData5 = () => {
          axios
              .get('http://127.0.0.1:8000/api/dashboards6/')
              .then(response => {
                let myChart = echarts.init(document.getElementById('right1'));

                myChart.setOption({
                  xAxis: response.data.xAxis,
                  yAxis: response.data.yAxis,
                  series: response.data.series
                });

                console.log(response);
                loading5.value = false;
              })
              .catch(error => {
                console.error('Error:', error);
                loading5.value = false;
              });
        };


        const fetchData4 = () => {
          axios.get('http://127.0.0.1:8000/api/dashboards1/')
              .then(response => {
                let myChart = echarts.init(document.getElementById('run11'));

                var option = {
                  color: [
                    "#37a2da",
                    "#32c5e9",
                    "#9fe6b8",
                    "#ffdb5c",
                    "#ff9f7f",
                    "#fb7293",
                    "#e7bcf3",
                    "#8378ea",
                  ],
                  tooltip: {
                    trigger: "item",
                    formatter: "{a} <br/>{b} : {c} ({d}%)",
                  },
                  toolbox: {
                    show: true,
                  },
                  legend: {
                    type: "scroll",
                    orient: "vertical",
                    right: "-3%",
                    align: "left",
                    top: "middle",
                    textStyle: {
                      color: "#8C8C8C",
                    },
                    height: 150,
                  },
                  series: [
                    {
                      name: "风格",
                      type: "pie",
                      radius: [0, 80],
                      data: response.data.series[0].data,
                    },
                  ],
                };

                myChart.setOption(option);
                loading4.value = false;
                console.log(response);
              })
              .catch(error => {
                console.error('Error:', error);
                loading4.value = false;
              });
        };

        const fetchData6 = () => {
          axios.get('http://127.0.0.1:8000/api/dashboards7/')
              .then(response => {
                let myChart = echarts.init(document.getElementById('right3'));

                var option = {
                  color: [
                    "#37a2da",
                    "#32c5e9",
                    "#9fe6b8",
                    "#ffdb5c",
                    "#ff9f7f",
                    "#fb7293",
                    "#e7bcf3",
                    "#8378ea",
                  ],
                  tooltip: {
                    trigger: "item",
                    formatter: "{a} <br/>{b} : {c} ({d}%)",
                  },
                  toolbox: {
                    show: true,
                  },
                  legend: {
                    type: "scroll",
                    orient: "vertical",
                    right: "-3%",
                    align: "left",
                    top: "middle",
                    textStyle: {
                      color: "#8C8C8C",
                    },
                    height: 150,
                  },
                  series: [
                    {
                      name: "风格",
                      type: "pie",
                      radius: [0, 80],
                      data: response.data.series[0].data,
                    },
                  ],
                };

                myChart.setOption(option);
                loading6.value = false;
                console.log(response);
              })
              .catch(error => {
                console.error('Error:', error);
                loading6.value = false;
              });
        };

        const fetchData7 = () => {
          axios.get('http://127.0.0.1:8000/api/dashboards8/')
              .then(response => {
                let myChart = echarts.init(document.getElementById('right2'));

                var option = {
                  color: [
                    "#37a2da",
                    "#32c5e9",
                    "#9fe6b8",
                    "#ff9f7f",
                    "#ffdb5c",
                    "#fb7293",
                    "#e7bcf3",
                    "#8378ea",
                  ],
                  tooltip: {
                    trigger: "item",
                    formatter: "{a} <br/>{b} : {c} ({d}%)",
                  },
                  toolbox: {
                    show: true,
                  },
                  legend: {
                    type: "scroll",
                    orient: "vertical",
                    right: "-3%",
                    align: "left",
                    top: "middle",
                    textStyle: {
                      color: "#8C8C8C",
                    },
                    height: 150,
                  },
                  series: [
                    {
                      name: "面料",
                      type: "pie",
                      radius: [0, 80],
                      data: response.data.series[0].data,
                    },
                  ],
                };

                myChart.setOption(option);
                loading6.value = false;
                console.log(response);
              })
              .catch(error => {
                console.error('Error:', error);
                loading6.value = false;
              });
        };

        const fetchData8 = () => {
          axios.get('http://127.0.0.1:8000/api/dashboards9/')
              .then(response => {
                let data = response.data.data; // 假设后端返回的数据中有一个'data'字段，存储年龄数据的统计信息

                // 创建echarts实例
                let myChart = echarts.init(document.getElementById('left2'));

                // 使用矩阵图展示年龄数据
                myChart.setOption({
                  tooltip: {},
                  visualMap: {
                    min: 0,
                    max: 100, // 根据实际情况设置最大值
                    calculable: true,
                    orient: 'horizontal',
                    left: 'center',
                    top: 'top'
                  },
                  series: [{
                    type: 'treemap',
                    data: data
                  }]
                });
              })
              .catch(error => {
                console.error('Error fetching data:', error);
              });
        };

        const fetchData9 = () => {
          axios.get('http://127.0.0.1:8000/api/dashboards10/')
              .then(response => {
                let data = response.data.data; // 假设后端返回的数据中有一个'data'字段，存储季节数据的统计信息

                // 创建echarts实例
                let myChart = echarts.init(document.getElementById('left3'));

                // 使用雷达图展示季节数据
                myChart.setOption({
                  radar: {
                    indicator: data.labels.map(label => ({name: label})),
                  },
                  series: [{
                    type: 'radar',
                    data: [{
                      value: data.values,
                      name: '服装件数'
                    }]
                  }]
                });
              })
              .catch(error => {
                console.error('Error fetching data:', error);
              });
        };


        return {
          totalSales,
          totalPeople,
          loading1,
          loading2,
          loading,
          loading3,
          loading4,
          loading5,
          loading6,
          loading7,
          loading8,
          loading9,
        };

      }
    }
)
;
</script>


<style scoped>
/* 声明字体*/
@font-face {
  font-family: electronicFont;
  src: url(../assets/font/DS-DIGIT.TTF);
}

section {
  //background: url(../assets/img/bg.jpg) top center;
  line-height: 1.15;
  background-color: #101736;
}

header {
  position: relative;
  height: 70px;
  background: url(data:image/png;base64,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) no-repeat;
  background-size: 100% 100%;
  background-color: #101736;
}

header h1 {
  font-size: 24px;
  color: #FFFFFF;
  text-align: center;
  line-height: 30px;
  font-weight: bold;
}

.mainbox {
  min-width: 1024px;
  max-width: 1920px;
  padding: 0.125rem 0.125rem 0;
  display: flex;
}

.mainbox .column {
  flex: 3;
}

.mainbox .column:nth-child(2) {
  flex: 5;
  margin: 0 0.125rem 0.1875rem;
  overflow: hidden;
}

.panel {
  /* margin-top: 40px; */
  position: relative;
  //height: 440px;
  border: 1px solid rgba(25, 186, 139, 0.17);
  background: rgba(255, 255, 255, 0.04) url(../assets/img/line1.png);
  padding: 0 0.1875rem 0.5rem;
}

.panel::before {
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-top: 2px solid #02a6b5;
  border-left: 2px solid #02a6b5;
}

.panel::after {
  position: absolute;
  top: 0;
  right: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-top: 2px solid #02a6b5;
  border-right: 2px solid #02a6b5;
}

.run {
  margin-top: 40px;
  position: relative;
  height: 342px;
  border: 1px solid rgba(25, 186, 139, 0.17);
  background: rgba(255, 255, 255, 0.04) url(../assets/img/line1.png);
  padding: 0 0.1875rem 0.5rem;
}

.run .run1-footer {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
}

.run::before {
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-top: 2px solid #02a6b5;
  border-left: 2px solid #02a6b5;
}

.run::after {
  position: absolute;
  top: 0;
  right: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-top: 2px solid #02a6b5;
  border-right: 2px solid #02a6b5;
}

.run .run1-footer::before {
  position: absolute;
  bottom: 0;
  left: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-bottom: 2px solid #02a6b5;
  border-left: 2px solid #02a6b5;
}

.run .run1-footer::after {
  position: absolute;
  bottom: 0;
  right: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-bottom: 2px solid #02a6b5;
  border-right: 2px solid #02a6b5;
}

.panel .panel-footer {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
}

.panel .panel-footer::before {
  position: absolute;
  bottom: 0;
  left: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-bottom: 2px solid #02a6b5;
  border-left: 2px solid #02a6b5;
}

.panel .panel-footer::after {
  position: absolute;
  bottom: 0;
  right: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-bottom: 2px solid #02a6b5;
  border-right: 2px solid #02a6b5;
}

.panel h2[data-v-364b76a4] {
  height: 50px;
  line-height: 50px;
  text-align: center;
  color: #fff;
  /* font-size: 15px; */
  font-weight: 400;
}

.panel h2 a {
  margin: 0 0.1875rem;
  color: #fff;
  text-decoration: underline;
}

.no-bd h2[data-v-364b76a4] {
  height: 50px;
  line-height: 50px;
  text-align: center;
  color: #fff;
  font-weight: 400;
}

.no-bd h2 a {
  margin: 0 0.1875rem;
  color: #fff;
  text-decoration: underline;
}

.run h2 {
  height: 50px;
  line-height: 50px;
  text-align: center;
  color: #fff;
  font-weight: 400;
}

.run h2 a {
  margin: 0 0.1875rem;
  color: #fff;
  text-decoration: underline;
}

.panel .chart {
  height: 286px;
}

.panel .run1 {
  height: 500px;
}

.run {
    position: relative;
    height: 336px;
    top: -39px;
}

.run .run1 {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 5;
  height: 100%;
  width: 100%;
}

.no {
  background: rgba(101, 132, 226, 0.1);
  padding: 0.1875rem;
}

.no .no-hd {
  position: relative;
  border: 1px solid rgba(25, 186, 139, 0.17);
}

.no .no-hd::before {
  content: "";
  position: absolute;
  width: 30px;
  height: 10px;
  border-top: 2px solid #02a6b5;
  border-left: 2px solid #02a6b5;
  top: 0;
  left: 0;
}

.no .no-hd::after {
  content: "";
  position: absolute;
  width: 30px;
  height: 10px;
  border-bottom: 2px solid #02a6b5;
  border-right: 2px solid #02a6b5;
  right: 0;
  bottom: 0;
}

.no .no-hd ul {
  display: flex;
}

.no .no-hd ul li {
  list-style: none;
  position: relative;
  flex: 1;
  text-align: center;
  height: 50px;
  line-height: 50px;
  font-size: 28px;
  color: rgba(5, 213, 255, 1);
  padding: 10px;
  font-family: electronicFont;
  font-weight: bold;
}

.no .no-hd ul li:first-child::after {
  content: "";
  position: absolute;
  height: 50%;
  width: 1px;
  background: rgba(255, 255, 255, 0.2);
  right: 0;
  top: 25%;
}

.no .no-bd ul {
  display: flex;
}

.no .no-bd ul li {
  flex: 1;
  height: 20px;
  line-height: 20px;
  text-align: center;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.7);
  padding-top: 10px;
}

.map[data-v-364b76a4] {
  position: relative;
  height: 533px;
  top: 0px;
}

.map .chart {
  position: absolute;
  top: 0px;
  left: 0;
  height: 500px;
  z-index: 5;

  width: 100%;
}

.map .chart-footer {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
}

.map::before {
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-top: 2px solid #02a6b5;
  border-left: 2px solid #02a6b5;
}

.map::after {
  position: absolute;
  top: 0;
  right: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-top: 2px solid #02a6b5;
  border-right: 2px solid #02a6b5;
}

.map .chart-footer::before {
  position: absolute;
  bottom: 0;
  left: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-bottom: 2px solid #02a6b5;
  border-left: 2px solid #02a6b5;
}

.map .chart-footer::after {
  position: absolute;
  bottom: 0;
  right: 0;
  content: "";
  width: 10px;
  height: 10px;
  border-bottom: 2px solid #02a6b5;
  border-right: 2px solid #02a6b5;
}
</style>