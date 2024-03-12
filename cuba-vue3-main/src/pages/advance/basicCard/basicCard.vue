<template>
    <Breadcrumbs title="Basic Cards" main="Bonus UI"  />

    <div class="container-fluid">
        <div class="row">
            <basic6Page/>
            <basicRest/>
            </div>
    </div>
</template>
<script>
import basic6Page from './basic6Page.vue';
import basicRest from './basicRest.vue'
export default{
    components:{
        basic6Page,
        basicRest
    }
}
</script>