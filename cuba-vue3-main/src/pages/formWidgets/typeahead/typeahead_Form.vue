<template>
     <Breadcrumbs main="Form Widgets" title="Typeahead" />
          <div class="container-fluid">
            <div class="typeahead">
              <div class="row">
                  <basicDemo/>
                  <preFetch/>
                  <blooDhound/>
                  <remoteView/>
                  <customTemplates/>
                  <defaultSuggestions/>
                  <rtlSupport/>
                 
              </div>
            </div>
          </div>
           
</template>
<script>
import basicDemo from "./basicDemo.vue"
import preFetch from "./preFetch.vue"
import blooDhound from "./blooDhound.vue"
import remoteView from "./remoteView.vue"
import customTemplates from "./customTemplates.vue"
import defaultSuggestions from "./defaultSuggestions.vue"
import rtlSupport from "./rtlSupport.vue"
export default {
    components:{
        basicDemo,
        preFetch,
        blooDhound,
        remoteView,
        customTemplates,
        defaultSuggestions,
        rtlSupport,
    }
}
</script>