<template>
     <div class="col-md-6 col-sm-12 box-col-12">
                <div class="card">
                  <div class="card-header pb-0">
                    <h5>Stacked bar chart</h5>
                  </div>
                  <div class="card-body">
                   <chartist
                     class="ct-10 flot-chart-container"
                     ratio="ct-major-second"
                     type="Bar"
                     :data="chart7.data"
                     :options="chart7.options">
                  </chartist>
                  </div>
                </div>
              </div>
</template>
<script>
export default {
    data(){
        return{
       chart7 : {
          data: {
            labels: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q13', 'Q14'],
            series: [
              [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300],
              [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300],
              [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300]
            ]
          },
          options: {
            stackBars: true,
            axisY: {
              labelInterpolationFnc: function(value) {
                return (value / 1000) + 'k';
              }
            },
          },
        },
        }
    }
}
</script>