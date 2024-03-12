<template>
  <div class="col-md-6 col-sm-12 box-col-12">
    <div class="card">
      <div class="card-header pb-0">
        <h5>Bi-polar bar chart</h5>
      </div>
      <div class="card-body">
        <chartist
          class="ct-9 flot-chart-container"
          ratio="ct-major-second"
          type="Bar"
          :data="chart6.data"
          :options="chart6.options">
        </chartist>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    data(){
        return{
              chart6 : {
          data: {
            labels: ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10'],
            series: [
              [1, 2, 4, 8, 6, -2, -1, -4, -6, -2]
            ]
          },
          options: {
            high: 10,
            low: -10,
            axisX: {
              labelInterpolationFnc: function(value, index) {
                return index % 2 === 0 ? value : null;
              }
            },
          },
        },
        }
    }
};
</script>