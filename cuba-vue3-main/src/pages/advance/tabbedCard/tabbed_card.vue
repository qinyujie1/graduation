<template>
     <Breadcrumbs main="Cards" title="Tabbed Card"/>
          <div class="container-fluid">
            <div class="row">
            <simpleTab/>
            <tabIcon/>
            <colorTab/>
            <colorOption/>
            <materialTab/>
            <materialIcon/>
            <materialIcon2/>
            <materialIcon3/>
            </div>
          </div>
</template>
<script>
import simpleTab from "./simpleTab.vue"
import tabIcon from "./tabIcon.vue"
import colorTab from "./colorTab.vue"
import colorOption from "./colorOption.vue"
import materialTab from "./materialTab.vue"
import materialIcon from "./materialIcon.vue"
import materialIcon2 from "./materialIcon2.vue"
import materialIcon3 from "./materialIcon3.vue"
export default {
    components:{
        simpleTab,
        tabIcon,
        colorTab,
        colorOption,
        materialTab,
        materialIcon,
        materialIcon2,
        materialIcon3
    }
}
</script>