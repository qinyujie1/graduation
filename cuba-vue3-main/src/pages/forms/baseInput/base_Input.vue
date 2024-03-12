<template>
    <Breadcrumbs title="Base Input" main="Forms Control" />
    
        <div class="container-fluid">
            <div class="row">
              <div class="col-sm-12">
                  <basicForm/>
                  <basicHTML/>
                  <edgesInput/>
                  <flatInput/>
                  <raiseInput/>
                  <solidInput/>
                  <inputSizing/>
                  <customControls/>
              </div>
            </div>
        </div>
   
</template>
<script>
import basicForm from "./basicForm.vue"
import basicHTML from "./basicHTML.vue"
import edgesInput from "./edgesInput.vue"
import flatInput from "./flatInput.vue"
import raiseInput from "./raiseInput.vue"
import solidInput from "./solidInput.vue"
import inputSizing from "./inputSizing.vue"
import customControls from "./customControls.vue"
export default {
    components:{
        basicForm,
        basicHTML,
        edgesInput,
        flatInput,
        raiseInput,
        solidInput,
        inputSizing,
        customControls
    }
}
</script>