<template>
    <Breadcrumbs title="Mega Options" main="Forms Control" />
    <div class="container-fluid">
            <div class="row">
                <defaultStyle/>
                <noBorder/>
                <solidBorder/>
                <offerStyle/>
                <inlineStyle/>
                <verticalStyle/>
                <horizontalStyle/>
            </div>
         </div>
</template>
<script>
import defaultStyle from "./defaultStyle.vue"
import noBorder from "./noBorder.vue"
import solidBorder from "./solidBorder.vue"
import offerStyle from "./offerStyle.vue"
import inlineStyle from "./inlineStyle.vue"
import verticalStyle from "./verticalStyle.vue"
import horizontalStyle from "./horizontalStyle.vue"
export default {
    components:{
        defaultStyle,
        noBorder,
        solidBorder,
        offerStyle,
        inlineStyle,
        verticalStyle,
        horizontalStyle
    }
}
</script>