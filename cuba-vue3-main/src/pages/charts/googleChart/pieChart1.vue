<template>
     <div class="col-sm-12 col-xl-4 box-col-6">
                <div class="card">
                  <div class="card-header">
                    <h5>Pie Chart <span class="digits">1</span></h5>
                  </div>
                  <div class="card-body p-0 chart-block">
                    <div class="chart-overflow" id="pie-chart4">
                        <GChart
                      class="chart-overflow" 
                      id="pie-chart4"
                      type="PieChart"
                      :data="pie_chart.chartData_3"
                      :options="pie_chart.options_3"
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
               pie_chart: {
                    chartData_3: [
            ['Language', 'Speakers (in millions)'],
            ['Assamese', 13],
            ['Bengali', 83], 
            ['Bodo', 1.4],
            ['Dogri', 2.3], 
            ['Gujarati', 46], 
            ['Hindi', 300],
            ['Kannada', 38], 
            ['Kashmiri', 5.5], 
            ['Konkani', 5],
            ['Maithili', 20], 
            ['Malayalam', 33], 
            ['Manipuri', 1.5],
            ['Marathi', 72], 
            ['Nepali', 2.9], 
            ['Oriya', 33],
            ['Punjabi', 29], 
            ['Sanskrit', 0.01], 
            ['Santhali', 6.5],
            ['Sindhi', 2.5], 
            ['Tamil', 61], 
            ['Telugu', 74], 
            ['Urdu', 52]
          ],
           options_3: { 
            title: 'Indian Language Use',
            legend: 'none',
            width:'100%',
            height: 400,
            pieSliceText: 'label',
            slices: {  4: { offset: 0.2 },
                       12: { offset: 0.3 },
                       14: { offset: 0.4 },
                       15: { offset: 0.5 },
            },
            colors: [primary,secondary, "#222222", "#717171", "#e2c636", "#d22d3d","#e6edef", primary, secondary, "#222222", "#717171", "#e2c636","#d22d3d", primary, secondary, "#222222", "#717171", "#e2c636", "#d22d3d", primary,secondary, "#222222"]
            
          },
               }
        }
    }
}
</script>