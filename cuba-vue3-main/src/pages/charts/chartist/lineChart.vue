<template>
    <div class="col-md-6 col-sm-12 box-col-12">
                <div class="card">
                  <div class="card-header pb-0">
                    <h5>Line chart with area</h5>
                  </div>
                  <div class="card-body">
                    <chartist
                          class="ct-4 flot-chart-container"
                          ratio="ct-major-second"
                          type="Line"
                          :data="chart5.data"
                          :options="chart5.options">
                  </chartist>
                  </div>
                </div>
              </div>
</template>
<script>
export default {
    data(){
        return{
         chart5 : {
          data: {
            labels: [1, 2, 3, 4, 5, 6, 7, 8],
            series: [
              [5, 9, 7, 8, 5, 3, 5, 4]
            ]
          },
          options: {
            low: 0,
            showArea: true,
          },
        },
        }
    }
}
</script>