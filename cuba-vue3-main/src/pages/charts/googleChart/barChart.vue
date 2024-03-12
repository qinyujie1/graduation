<template>
     <div class="col-sm-12 col-xl-6 box-col-12">
                <div class="card">
                  <div class="card-header">
                    <h5>bar-chart2</h5>
                  </div>
                  <div class="card-body chart-block">
                    <div id="bar-chart2">
                         <GChart
                      class="chart-overflow" 
                      id="bar-chart2"
                      type="BarChart"
                      :data="bar_chart.chartData_1"
                      :options="bar_chart.options_1"
                    />
                    </div>
                  </div>
                </div>
              </div>
</template>
<script>
var primary = localStorage.getItem('primary_color') || '#24695c';
var secondary = localStorage.getItem('secondary_color') || '#ba895d';

import { GChart } from "vue-google-charts";
export default {
    components:{
        GChart 
    },
    data(){
        return{
              chartsLib: null, 
               bar_chart: {
          chartData_1: [  
            ['Element', 'Density', { role: 'style' } ],
            ['Copper', 10, primary],
            ['Silver', 12, secondary],
            ['Gold', 14, '#222222'],
            ['Platinum', 16, 'color: #717171']
          ],
          options_1:  {
            title: 'Density of Precious Metals, in g/cm^3',
            width:'100%',
            height: 400,
            bar: { groupWidth: '95%' },
            legend: { position: 'none' },
          }
        },
        }
    }
}
</script>