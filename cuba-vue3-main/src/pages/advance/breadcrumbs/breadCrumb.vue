<template>
    <Breadcrumbs title="Breadcrumb" main="Bonus UI"  />
    
          <div class="container-fluid">
            <div class="row">
                <defaultBreadcrumb/>
                <navBreadcrumb/>
                <coloredBreadcrumb/>
            </div>
          </div>

</template>
<script>
import defaultBreadcrumb from "./defaultBreadcrumb.vue"
import navBreadcrumb from "./navBreadcrumb.vue"
import coloredBreadcrumb from "./coloredBreadcrumb.vue"
export default {
    components:{
        defaultBreadcrumb,
        navBreadcrumb,
        coloredBreadcrumb
    }
}
</script>