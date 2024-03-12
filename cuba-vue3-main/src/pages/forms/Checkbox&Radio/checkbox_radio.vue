<template>
    <Breadcrumbs title="Checkbox & Radio" main="Forms Control"  />
         <div class="container-fluid">
            <div class="row">
              <customRadio/>
              <customCheckbox/>
              <animatedRadio/>
              <animatedCheckbox/>
            </div>
         </div>
</template>
<script>
import customRadio from "./customRadio.vue"
import animatedRadio from "./animatedRadio.vue"
import animatedCheckbox from "./animatedCheckbox.vue"
import customCheckbox from "./customCheckbox.vue"
export default {
    components:{
        customRadio,
        animatedRadio,
        animatedCheckbox,
        customCheckbox
    }
}
</script>