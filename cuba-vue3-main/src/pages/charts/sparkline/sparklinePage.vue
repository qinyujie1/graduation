<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-xl-4 col-md-6 col-sm-12 box-col-6">
                <div class="card">
                  <div class="card-header pb-0">
                    <h3>Mouse Speed Chart</h3>
                  </div>
                  <div class="card-body chart-block">
                    <div class="flot-chart-container">
                      <div class="flot-chart-placeholder" id="mouse-speed-chart-sparkline"></div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-4 col-md-6 col-sm-12 box-col-6">
                <div class="card">
                  <div class="card-header pb-0">
                    <h3>Simple Bar Charts</h3>
                  </div>
                  <div class="card-body chart-block">
                    <div class="flot-chart-container">
                      <div class="flot-chart-placeholder" id="custom-line-chart">
                      
                        <sparklines :indicatorStyles="indicatorStyle">
                            <sparklineLine :width="200"
                              :height="60"
                              :data="data"
                              :textStyles="textStyles" />
                          </sparklines>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
        </div></div>
</template>
<script>

export default {
    data(){
        return{
            data:[5, 30, 27, 35, 30, 50, 70],
            
    }},

}

</script>