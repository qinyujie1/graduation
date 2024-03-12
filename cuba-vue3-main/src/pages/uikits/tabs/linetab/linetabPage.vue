<template>
    <breadCrumbs title="Line Tabs" main="Ui Kits" title1="Line Tabs" />
    <div class="container-fluid">
        <div class="row">
            <simplePage/>
            <materialPage/>
            <colorPage/>
            </div>
        </div>
</template>
<script>
import simplePage from './simple123Page.vue';
import materialPage from './material45Page'
import colorPage from './color678Page.vue'
    export default{
        name: 'linetabPage',
        components:{
            simplePage, 
            materialPage,
            colorPage
        }
    }
</script>