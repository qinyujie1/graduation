<template>
  <Breadcrumbs main="Chat" title="Chat App" />

        <!-- Container-fluid starts-->
     
        <div class="container-fluid text-start">
          <div class="row">
           <searchChat/>
           <chatBody/>
        </div>
      </div>
  
  
        <!-- Container-fluid Ends-->
      
</template>
<script>
  import chatBody from "./chatBody.vue"
  import searchChat from "./searchChat.vue"
  
  export default {
      components:{
        searchChat,
        
        chatBody
      }
  }
  </script>