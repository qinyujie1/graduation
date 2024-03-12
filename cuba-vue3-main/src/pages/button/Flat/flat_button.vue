<template>
    <Breadcrumbs title="Flat Style" main="Apps"  />
    <div class="container-fluid">
            <div class="row">
              <div class="col-sm-12 ">
              <flat/>
              <flat2/>
              <flat3/>
              </div>
            </div>
         </div>
</template>
<script>
import flat from "./flatPage.vue"
import flat2 from "./flat2Page.vue"
import flat3 from "./flat3Page.vue"
export default {
    components:{
        flat,
        flat2,
        flat3
    }
}
</script>