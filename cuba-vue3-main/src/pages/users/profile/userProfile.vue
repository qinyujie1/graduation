<template>
<Breadcrumbs title="User Profile" main="User"  />

<!-- Container-fluid starts-->
<div class="container-fluid ">
    <div class="user-profile">
      <div class="row">
        <tourProfile />
        <tourProfile2 />
        <tourProfile3 />
        <tourProfile4 />
        <tourProfile5 />

     
      </div>
    </div>
  </div>
<!-- Container-fluid Ends-->
</template>

<script>
import tourProfile from "./tourProfile.vue";
  import tourProfile2 from "./tourProfile2.vue";
  import tourProfile3 from "./tourProfile3.vue";
  import tourProfile4 from "./tourProfile4.vue";
  import tourProfile5 from "./tourProfile5.vue";

export default {
    name: 'userProfile',
    components: {
        tourProfile,
      tourProfile2,
      tourProfile3,
      tourProfile4,
      tourProfile5,
    },
    
}
</script>
