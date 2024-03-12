<template>
  <Breadcrumbs  title="Knowledge Base" />
       <div class="container-fluid faq-section">
            <div class="row">
                <div class="col-12 text-start">
                <div class="knowledgebase-bg">
                  <img class="bg-img-cover bg-center img-fluid" src="../../assets/images/knowledgebase/bg_1.jpg" alt="looginpage">
                  </div>
                <div class="knowledgebase-search">
                  <div>
                    <h3>How Can I help you?</h3>
                    <form class="form-inline" action="#" method="get">
                      <div class="form-group w-100 mb-0"><vue-feather type="search"></vue-feather>
                        <input class="form-control-plaintext w-100" type="text" placeholder="Type question here" title="">
                      </div>
                    </form>
                  </div>
                </div>
              </div>
              <faq/>
              <featured/>
            </div>

       </div>
</template>
<script>
import faq from "../faq/faqPage.vue"
import featured from "./featuredPage.vue"
export default {
    components:{
      faq,
      featured
    }
}
</script>