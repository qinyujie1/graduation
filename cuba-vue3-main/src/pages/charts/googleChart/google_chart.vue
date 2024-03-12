<template>
    <Breadcrumbs main="Charts" title="Google Chart"/>
         <div class="container-fluid">
            <div class="row">
                <areaChart1/>
                <columnChart/>
                <ganttChart/>
                <lineChart/>
                <comboChart/>
                <barChart/>
                <wordTree/>
                <pieChart1/>
                <pieChart2/>
                <pieChart3/>
  
            </div>
         </div>
</template>
<script>
import pieChart1 from "./pieChart1.vue"
import areaChart1 from "./areaChart1.vue"
import pieChart2 from "./pieChart2.vue"
import pieChart3 from "./pieChart3.vue"
import columnChart from "./columnChart.vue"
import ganttChart from "./ganttChart.vue"
import lineChart from "./lineChart.vue"
import comboChart from "./comboChart.vue"
import barChart from "./barChart.vue"
import wordTree from "./wordTree.vue"
export default {
    components:{
        pieChart1,
        areaChart1,
        pieChart2,
        pieChart3,
        columnChart,
        ganttChart,
        lineChart,
        comboChart,
        barChart,
        wordTree
    }
}
</script>