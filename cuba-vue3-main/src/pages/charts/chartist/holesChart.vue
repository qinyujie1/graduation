<template>
     <div class="col-md-6 col-sm-12 box-col-12">
                <div class="card">
                  <div class="card-header pb-0">
                    <h5>Holes in data</h5>
                  </div>
                  <div class="card-body">
                   <chartist
                          class="ct-2 flot-chart-container"
                          ratio="ct-major-second"
                          type="Line"
                          :data="chart11.data"
                          :options="chart11.options">
                  </chartist>
                  </div>
                </div>
              </div>
</template>
<script>
export default {
    data(){
        return{
     chart11 : {
          data: {
            labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            series: [
              [5, 5, 10, 8, 7, 5, 4, null, null, null, 10, 10, 7, 8, 6, 9],
              [10, 15, null, 12, null, 10, 12, 15, null, null, 12, null, 14, null, null, null],
              [null, null, null, null, 3, 4, 1, 3, 4,  6,  7,  9, 5, null, null, null],
              [{ x:3, y: 3 },{ x: 4, y: 3 }, { x: 5, y: undefined }, { x: 6, y: 4 }, { x: 7, y: null }, { x: 8, y: 4 }, { x: 9, y: 4 }]
            ]
          },
          options: {
            fullWidth: true,
            chartPadding: {
              right: 10
            },
            low: 0
          },
        },
        }
    }
}
</script>