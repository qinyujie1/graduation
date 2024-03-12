<template>
  <Breadcrumbs main="Charts" title="ApexChart" />
    <div class="container-fluid ">
      <div class="row">
        <basicArea/>  
        <areaSpaline/>
        <barChart/>
        <columnChart/>
        <bubbleChart/>
        
        <stepline/>
        <columnChart2/>
        <pieChart/>
        <donutChart/>
        <mixedChart/>
        <candlestick/>
        <radarChart/>
        <radialBar/>
      </div>
    </div>
</template>
<script>
import basicArea from "./basicArea.vue"
import areaSpaline from "./areaSpaline.vue"
import barChart from "./barChart.vue"
import columnChart from "./columnChart.vue"
import bubbleChart from "./bubbleChart.vue"
import candlestick from "./candlestickChart.vue"
import stepline from "./steplinePage.vue"
import columnChart2 from "./columnChart2.vue"
import pieChart from "./pieChart.vue"
import donutChart from "./donutChart.vue"
import mixedChart from "./mixedChart.vue"
import radarChart from "./radarChart.vue"
import radialBar from "./radialBar.vue"
export default {
    components:{
        basicArea,
        areaSpaline,
        barChart,
        columnChart,
        bubbleChart,
        candlestick,
        stepline,
        columnChart2,
        pieChart,
        donutChart,
        mixedChart,
        radarChart,
        radialBar
    }
};
</script>