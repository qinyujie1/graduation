<template>
    <div class="col-md-6 col-sm-12 box-col-12">
                <div class="card">
                  <div class="card-header pb-0">
                    <h5>Horizontal bar chart</h5>
                  </div>
                  <div class="card-body">
                    <chartist
                          class="ct-11 flot-chart-container"
                          ratio="ct-major-second"
                          type="Bar"
                          :data="chart8.data"
                          :options="chart8.options">
                  </chartist>
                  </div>
                </div>
              </div>
</template>
<script>
export default {
    data(){
        return{
     chart8 : {
          data: {
            labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            series: [
              [5, 4, 3, 7, 5, 10, 3],
              [3, 2, 9, 5, 4, 6, 4]
            ]
          },
          options: {
            seriesBarDistance: 10,
            reverseData: true,
            horizontalBars: true,
            axisY: {
              offset: 70
            },
          },
        },
        }
    }
}
</script>