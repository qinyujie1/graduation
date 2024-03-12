<template>
     <div class="row">
                    <div class="col-xl-3 xl-40 col-md-5 box-col-4">
                      <div class="default-according style-1 faq-accordion job-accordion" id="accordionoc4">
                        <div class="row">
                        <myProfile/>
                        </div>
                      </div>
                    </div>
                    <div class="col-xl-6 xl-60 col-lg-12 col-md-7 box-col-8">
                      <div class="row">
                        <pepoleView/>
                        <hobbies/>
                        <education/>
                        <viewed/>
                      </div>
                    </div>
                    <profileIntro/>
     </div>
</template>
<script>
import pepoleView from "../about/pepoleView.vue"
import myProfile from "../about/myProfile.vue"
import hobbies from "../about/hobbiesPage.vue"
import education from "./educationPage.vue"
import viewed from "../about/viewedPage.vue" 
import profileIntro from "../timeline/profileIntro.vue"
export default {
    components:{
        myProfile,
        pepoleView,
        hobbies,
        education,
        viewed,
        profileIntro
    }
}
</script>