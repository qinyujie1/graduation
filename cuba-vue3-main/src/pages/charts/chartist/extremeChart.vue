<template>
     <div class="col-md-6 col-sm-12 box-col-12">
                <div class="card">
                  <div class="card-header pb-0">
                    <h5>Extreme responsive configuration</h5>
                  </div>
                  <div class="card-body">
                    <chartist
                          class="ct-12 flot-chart-container"
                          ratio="ct-major-second"
                          type="Bar"
                          :data="chart9.data"
                          :options="chart9.options"
                          :responsiveOptions="chart9.responsiveOptions">
                  </chartist>
                  </div>
                </div>
              </div>
</template>
<script>
export default {
    data(){
        return{
      chart9 : {
          data: {
            labels: ['2010-11', '2011-12', '2012-13', '2013-13', '2014-15', '2015-16', '2016-17', '2017-18'],
            series: [
              [0.9, 0.4, 1.5, 4.9, 3, 3.8, 3.8, 1.9],
              [6.4, 5.7, 7, 4.95, 3, 3.8, 3.8, 1.9],
              [4.3, 2.3, 3.6, 4.5, 5, 2.8, 3.3, 4.3],
              [3.8, 4.1, 2.8, 1.8, 2.2, 1.9, 6.7, 2.9]
            ]
          },
          options: {
            seriesBarDistance: 15,
            horizontalBars: false,
            axisY: {
              offset: 20
            },
          },
          responsiveOptions : [
            ['screen and (min-width: 1200px) and (max-width: 1366px)', {
              seriesBarDistance: 10
            }],
            ['screen and (max-width: 767px)', {
              seriesBarDistance: 10
            }],
            ['screen and (max-width: 480px)', {
              stackBars: true,
              seriesBarDistance: 6,
            }]
          ]
        },
        }
    }
}
</script>