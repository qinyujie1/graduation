<template>
    <Breadcrumbs title="Scrollbar" main="Bonus UI" />
    <div class="container-fluid">
            <div class="row">
                <clickDrag/>
                <smallSize/>
                <bothSide/>
                <horizontalScroll/>
                <alwaysVisible/>  
                <verticalScroll/> 
            </div>
        </div>
</template>
<script>
import clickDrag from "./clickDrag.vue"
import smallSize from "./smallSize.vue"
import alwaysVisible from "./alwaysVisible.vue"
import bothSide from "./bothSide.vue"
import horizontalScroll from "./horizontalScroll.vue"
import verticalScroll from "./verticalScroll.vue"
export default {
    components:{
        clickDrag,
        smallSize,
        alwaysVisible,
        bothSide,
        horizontalScroll,
        verticalScroll
    }
}
</script>