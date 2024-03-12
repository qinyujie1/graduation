<template>
  <Breadcrumbs title="Tour" main="Bonus UI"  />
      <div class="container-fluid ">
        <div class="user-profile">
          <div class="row">
            <tourProfile />
            <tourProfile2 />
            <tourProfile3 />
            <tourProfile4 />
            <tourProfile5 />

         
            <v-tour name="myTour" :steps="steps" :options="tourOptions"></v-tour>
          </div>
        </div>
      </div>
  </template>
  <script>
  import tourProfile from "./tourProfile.vue";
  import tourProfile2 from "./tourProfile2.vue";
  import tourProfile3 from "./tourProfile3.vue";
  import tourProfile4 from "./tourProfile4.vue";
  import tourProfile5 from "./tourProfile5.vue";

  // import post1Page from "../../users/profile/post1Page.vue";
  // import post2Page from "../../users/profile/post2Page.vue";
  // import post3Page from "../../users/profile/post3Page.vue";
  export default {
    components: {
      tourProfile,
      tourProfile2,
      tourProfile3,
      tourProfile4,
      tourProfile5,

      // post1Page, post2Page, post3Page
    },
    data() {
      return {
        tourOptions: {
          useKeyboardNavigation: true,
          labels: {
            buttonSkip: "Skip",
            buttonPrevious: "Back",
            buttonNext: "Next",
            buttonStop: "Done",
          },
        },
        toogle: true,
        steps: [
          {
            target: "#profile-tour",
            content: "This is Profile image",
          },
          {
            target: "#update-profile-tour",
            content: "Change Profile image here",
          },
          {
            target: "#info-bar-tour",
            content: "This is the your details",
          },
          {
            target: "#social-bar-tour",
            content: "This is your Social details",
          },
          {
            target: "#first-post-tour",
            content: "This is the your first Post",
            params: {
              placement: "top",
            },
          },
          // {
          //   target: "#last-post-tour",
          //   content: "This is the your last Post",
          //   params: {
          //     placement: "top",
          //   },
          // },
        ],
      };
    },
    mounted: function () {
      this.$tours["myTour"].start();
    },
  };
  </script>