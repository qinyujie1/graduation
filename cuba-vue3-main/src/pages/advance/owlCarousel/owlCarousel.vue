<template>
    <Breadcrumbs title="Owl Carousel" main="Bonus UI" />
    <div class="container-fluid">
        <div class="row">
          <div class="col-sm-12">
            <owl123Page/>
            <owl456Page/>
            <owl789Page/>
            
            <owl101112Page/>
            <owl1314Page/>
          </div></div></div>
</template>
<script>
import owl1314Page from './owl1314Page.vue'
import owl101112Page from './owl101112Page.vue'
import owl123Page from './owl123Page.vue'
import owl456Page from './owl456Page.vue';
import owl789Page from './owl789Page.vue'
export default {
    components:{
    owl123Page,
    owl456Page,
    owl789Page,
    owl101112Page,
    owl1314Page
}}
</script>