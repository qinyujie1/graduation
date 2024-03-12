<template>
  <Breadcrumbs title="Edge Button" main="Buttons"  />

          <div class="container-fluid">
            <div class="row">
              <div class="col-sm-12 ">
                  <edge/>
                  <edge2/>
                  <edge3/>
              </div>
            </div>
          </div>
</template>
<script>
import edge from "./edgePage.vue"
import edge2 from "./edge2Page.vue"
import edge3 from "./edge3Page.vue"
export default {
    components:{
        edge,
        edge2,
        edge3
    }
}
</script>