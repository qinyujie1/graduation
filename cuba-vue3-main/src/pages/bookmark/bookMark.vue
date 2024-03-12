<template>
<Breadcrumbs title="Bookmarks" main="Apps" />

<div class="container-fluid">
     <div class="email-wrap bookmark-wrap">
       <div class="row">
                   <addBookmark/>
              </div>
            </div>
    </div>
</template>
<script>

  
import addBookmark from "./addBookmark.vue"
export default {
   components:{
        addBookmark
   },
  
}
</script>