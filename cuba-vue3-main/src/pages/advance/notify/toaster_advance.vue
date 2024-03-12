<template>
   <Breadcrumbs title="Notify" main="Bonus UI"  />

         <div class="container-fluid">
            <div class="row">
            <toastr/>
            <toastrIcon/>
            <toastrPosition/>
            </div>
         </div>
</template>
<script>
import toastr from "./toastrPage.vue"
import toastrIcon from "./toastrIcon.vue"
import toastrPosition from "./toastrPosition.vue"
export default {
   components:{
       toastr,
       toastrIcon,
       toastrPosition
   }
}
</script>