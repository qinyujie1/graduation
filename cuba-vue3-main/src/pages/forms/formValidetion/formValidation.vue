<template>
  <Breadcrumbs title="Validation Forms" main="Forms Control"  />
 
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12">
            <customStyle/>
            <browserDefaults/>
            <supportedElements/>
            <toolTips/>
        </div>
      </div>
    </div>
 
</template>
<script>
import customStyle from "./customStyle.vue"
import browserDefaults from "./browserDefaults.vue"
import supportedElements from "./supportedElements.vue"
import toolTips from "./toolTips.vue"
export default {
     components:{
         customStyle,
         browserDefaults,
         supportedElements,
         toolTips
     }
};
</script>