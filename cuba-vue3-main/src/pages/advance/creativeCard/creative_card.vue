<template>
  <Breadcrumbs title="Creative Card" main="Card" />
  <div class="container-fluid">
      <div class="row">
          <card1/>
          <card2/>
      </div>
    </div>
</template>
<script>
import card1 from "./card1Page.vue"
import card2 from "./card2Page.vue"
export default {
    components:{
        card1,
        card2
    }
};
</script>