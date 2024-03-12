<template>
    <Breadcrumbs title="Ribbons" main="Bonus UI"  />
     <div class="container-fluid">
            <div class="row">
                <coloredBreadcrumb/>
            </div>
            <ribbons/>
            <ribbons2/>
            <ribbons3/>
            <ribbons4/>
            <ribbons5/>
            <ribbons6/>
            </div>
</template>
<script>
import coloredBreadcrumb from "./coloredBreadcrumb.vue"
import ribbons from "./ribbonsPage.vue"
import ribbons2 from "./ribbons2Page.vue"
import ribbons3 from "./ribbons3Page.vue"
import ribbons4 from "./ribbons4Page.vue"
import ribbons5 from "./ribbons5Page.vue"
import ribbons6 from "./ribbons6Page.vue"
export default {
    components:{
        coloredBreadcrumb,
        ribbons,
        ribbons2,
        ribbons3,
        ribbons4,
        ribbons5,
        ribbons6
    }
}
</script>