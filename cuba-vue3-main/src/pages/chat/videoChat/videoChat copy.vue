<template>
  <breadCrumbs title="Video Chat" main="Chat" title1="Video Chat" />
    <div class="container-fluid">
      <div class="row">
         <searchChat/>
         <chatBody/>
      </div>
    </div>
</template>
<script>
import chatBody from "./chatBody.vue"
import searchChat from "../chatApp/searchChat.vue"
export default {
    components:{
      searchChat,
      chatBody
    }
}
</script>