<template>
 <div class="col-md-6 col-sm-12 box-col-12">
                <div class="card">
                  <div class="card-header pb-0">
                    <h5>SVG Path animation</h5>
                  </div>
                  <div class="card-body">
                    <div class="ct-7 flot-chart-container">
                         <chartist
    class="ct-7 flot-chart-container"
    ratio="ct-major-second"
    type="Line"
    :data="chart2.data"
    :options="chart2.options"
    :event-handlers="chart2.eventHandlers"
  >
  </chartist>
                    </div>
                  </div>
                </div>
              </div>
 
</template>
<script>
 import * as Chartist from 'chartist';
export default {
    data(){
        return{
        chart2 : {
          data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
            series: [
              [1, 5, 2, 5, 4, 3],
              [2, 3, 4, 8, 1, 2],
              [5, 4, 3, 2, 1, 0.5]
            ]
          },
          options: {
            low: 0,
            showArea: true,
            showPoint: false,
            fullWidth: true,
          },
          eventHandlers : [{
            event: 'draw',
            fn(data) {
              if(data.type === 'line' || data.type === 'area') {
                data.element.animate({
                  d: {
                    begin: 2000 * data.index,
                    dur: 2000,
                    from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
                    to: data.path.clone().stringify(),
                    easing: Chartist.Svg.Easing.easeOutQuint
                  }
                });
              }
            }
          }]
        },
        }
    }
};
</script>