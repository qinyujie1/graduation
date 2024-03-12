<template>
     <div class="col-md-6 col-sm-12 box-col-12">
                <div class="card">
                  <div class="card-header pb-0">
                    <h5>Simple line chart</h5>
                  </div>
                  <div class="card-body">
                   <chartist
                          class="ct-1 flot-chart-container"
                          ratio="ct-major-second"
                          type="Line"
                          :data="chart10.data"
                          :options="chart10.options">
                  </chartist>
                  </div>
                </div>
              </div>
</template>
<script>
export default {
    data(){
        return{
      chart10 : {
          data: {
            labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            series: [
              [12, 9, 7, 8, 5],
              [2, 1, 3.5, 7, 3],
              [1, 3, 4, 5, 6]
            ]
          },
          options: {
            fullWidth: true,
            chartPadding: {
              right: 40
            }
          },
        },
        }
    }
}
</script>