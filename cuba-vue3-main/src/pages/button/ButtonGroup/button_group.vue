<template>
    <Breadcrumbs title="Button Group" main="Buttons" />
    <div class="container-fluid">
            <div class="row">
                <group/>
                <edges/>
                <flat/>
                <large/>
                <largeEdges/>
                <outline/>
                <outline2/>
                <outline3/>
                <outlineEdges/>
                <outlineFlat/>
                <radio/>
                <checkBox/>
                <nesting/>
            </div>
          </div>
</template>
<script>
import group from "./groupPage.vue"
import edges from "./edgesPage.vue"
import flat from "./flatPage.vue"
import large from "./largePage.vue"
import largeEdges from "./largeEdges.vue"
import outline from "./outlinePage.vue"
import outline2 from "./outline2Page.vue"
import outline3 from "./outline3Page.vue"
import outlineEdges from "./outlineEdges.vue"
import outlineFlat from "./outlineFlat.vue"
import radio from "./radioPage.vue"
import checkBox from "./checkBox.vue"
import nesting from "./nestingPage.vue"
export default {
    components:{
        group,
        edges,
        flat,
        large,
        largeEdges,
        outline,
        outline2,
        outline3,
        outlineEdges,
        outlineFlat,
        radio,
        checkBox,
        nesting
    }
}
</script>