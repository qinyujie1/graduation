<template>
    <Breadcrumbs main="Form Widgets" title="touchspin"/>
         <div class="container-fluid">
            <div class="bootstrap-touchspin">
              <div class="row">
                  <defaultTouchspin/>
                  <verticalTouchspin/>
                  <touchspinPostfix/>
                  <touchspinWithPrefix/>
                  <minMax/>
                  <initialValue/>
                  <touchspinSteps/>
                  <decimalValue/>
                  <changeButton/>
                  <touchspinWithIcon/>
                  <touchspinIconButton/>
                  <touchspinDropdown/>
                  <mousewheelDisable/>
                  <largeHorizontal/>
              </div>
            </div>
         </div>
</template>
<script>
import defaultTouchspin from "./defaultTouchspin.vue"
import verticalTouchspin from "./verticalTouchspin.vue"
import touchspinPostfix from "./touchspinPostfix.vue"
import touchspinWithPrefix from "./touchspinWithPrefix.vue"
import minMax from "./minMax.vue"
import initialValue from "./initialValue.vue"
import touchspinSteps from "./touchspinSteps.vue"
import decimalValue from "./decimalValue.vue"
import changeButton from "./changeButton.vue"
import touchspinWithIcon from "./touchspinWithIcon.vue"
import touchspinIconButton from "./touchspinIconButton.vue"
import touchspinDropdown from "./touchspinDropdown.vue"
import mousewheelDisable from "./mousewheelDisable.vue"
import largeHorizontal from "./largeHorizontal.vue"
export default {
    components:{
        defaultTouchspin,
        verticalTouchspin,
        touchspinPostfix,
        touchspinWithPrefix,
        minMax,
        initialValue,
        touchspinSteps,
        decimalValue,
        changeButton,
        touchspinWithIcon,
        touchspinIconButton,
        touchspinDropdown,
        mousewheelDisable,
        largeHorizontal
    }
}
</script>