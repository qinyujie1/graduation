<template>
    <Breadcrumbs title="Raised Button" main="Button" />
    <div class="container-fluid">
            <div class="row">
              <div class="col-sm-12 ">
                  <raised/>
                  <raised2/>
                  <raised3/>
              </div>
            </div>
         </div>
</template>
<script>
import raised from "./raisedPage.vue"
import raised2 from "./raised2Page.vue"
import raised3 from "./raised3Page.vue"
export default {
    components:{
        raised,
        raised2,
        raised3
    }
}
</script>