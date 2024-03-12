<template>
  <Breadcrumbs title="FAQ" main="Pages"/>
        <div class="container-fluid">
            <div class="faq-wrap">
              <div class="row">
                  <faq/>
                <faq1/>
                <featured/>
                <articles/>
              </div>
            </div>
        </div>
</template>
<script>
import faq from "./faqPage.vue"
import faq1 from "./faq1Page.vue"
import featured from "./featuredPage.vue"
import articles from "./articlesPage.vue"
export default {
    components:{
          faq,
          faq1,
          featured,
          articles
    }
}
</script>