<template>
    <Breadcrumbs title="Sweetalert" main="Bonus UI"  />    
    <div class="container-fluid">
        <div class="row">
            <basicExample/>
            <advanceState/>
            <alertPage/>
        </div></div>
</template>
<script>
import basicExample from './basicExample.vue'
import advanceState from './advancedState.vue'
import alertPage from './alertState.vue'
export default {
    components:{
        basicExample,
        advanceState,
        alertPage
    }
}
</script>

