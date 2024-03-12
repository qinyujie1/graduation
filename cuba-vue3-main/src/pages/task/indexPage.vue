<template>
<Breadcrumbs title="Tasks" main="Apps"  />
<!-- Container-fluid starts-->
<div class="container-fluid">
    <div class="email-wrap bookmark-wrap">
        <div class="row">
           <addTask/>
        </div>
    </div>
</div>
<!-- Container-fluid Ends-->
</template>

<script>
import addTask from './addTask.vue'
export default {
    components:{
        addTask
    },
}
</script>
