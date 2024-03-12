<template>
     <Breadcrumbs main="Form Widgets" title="Switch"/>
       <div class="container-fluid text-start">
            <div class="row">
                <basicSwitch/>
                <switchColor/>
                <switchOutline/>
                <switchUnchecked/>
                <switchSizing/>
                <switchIcons/>
                <switchwithColor/>
            </div>
       </div>
</template>
<script>
import basicSwitch from "./basicSwitch.vue"
import switchColor from "./switchColor.vue"
import switchOutline from "./switchOutline.vue"
import switchUnchecked from "./switchUnchecked.vue"
import switchSizing from "./switchSizing.vue"
import switchIcons from "./switchIcons.vue"
import switchwithColor from "./switchwithColor.vue"
export default {
    components:{
        basicSwitch,
        switchColor,
        switchOutline,
        switchUnchecked,
        switchSizing,
        switchIcons,
        switchwithColor
    }
}
</script>