<template>
<Breadcrumbs main="Charts" title="Chartist Chart"/>
     <div class="container-fluid">
            <div class="row">
                <chartist/>
                <pathAnimation/>
                <donut/>
                <bipolar/>
                <linechart/>
                <barchart/>
                <stacked/>
                <horizontal/>
                <extreme/>
                <simplechart/>
                <holes/>
                <filledholes/>
            </div>
     </div>
</template>
<script>
import chartist from "./chartistChart.vue" 
import pathAnimation from "./pathAnimation.vue"
import donut from "./donutChart.vue"
import bipolar from "./bipolarChart.vue"
import linechart from "./lineChart.vue"
import barchart from "./barChart.vue"
import stacked from "./stackedChart.vue"
import horizontal from "./horizontalChart.vue"
import extreme from "./extremeChart.vue"
import simplechart from "./simpleChart.vue"
import holes from "./holesChart.vue"
import filledholes from "./filledHoles.vue"
export default {
   components:{
     chartist,
     pathAnimation,
     donut,
     bipolar,
     linechart,
     barchart,
     stacked,
     horizontal,
     extreme,
     simplechart,
     holes,
     filledholes
   }
}
</script>