<template>
    <Breadcrumbs title="Social App" main="App" />
    <div class="container-fluid">
            <div class="user-profile social-app-profile ">
              <div class="row"> 
                 <socialHeader/> 
              </div>
            </div>
            
            <div class="tab-content" id="top-tabContent">
              
            <timLine/>
              </div>
    </div>
</template>
<script>
import timLine from "./timeline/index.vue"
import socialHeader from "./headerPage.vue"
export default {
    components:{
        socialHeader,
        timLine
    }
}
</script>