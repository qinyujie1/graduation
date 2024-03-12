<template>
    <Breadcrumbs title="Calender Basic" main="Bonus UI"  />
    <div class="container-fluid">
       
        <div class="row">
            <basicPage/>
            <checkboxPage/>
            <dragPage/>
            <contextPage/>
        </div></div>
</template>
<script>
import basicPage from './basicPage.vue'
import checkboxPage from './checkboxPage.vue'
import contextPage from './contextPage.vue'
import dragPage from './dragPage.vue'
export default {
    components:{
basicPage,checkboxPage,dragPage,contextPage
    }
}
</script>
