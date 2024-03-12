<template>
  <Breadcrumbs title="Blog Detail" main="Blog" />
  <div class="container-fluid ">
            <div class="row">
              <div class="col-xl-6 set-col-12 box-col-12">
                <div class="card">
                  <div class="blog-box blog-shadow"><img class="img-fluid bg-img-cover" src="@/assets/images/blog/blog.jpg" alt="">
                    <div class="blog-details">
                      <p>25 July 2018</p>
                      <h4>Accusamus et iusto odio dignissimos ducimus qui blanditiis.</h4>
                      <ul class="blog-social">
                        <li><i class="icofont icofont-user"></i>Mark Jecno</li>
                        <li><i class="icofont icofont-thumbs-up"></i>02 Hits</li>
                        <li><i class="icofont icofont-ui-chat"></i>598 Comments</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
              <detail/>
              <detail1/>
            </div>
          </div>
</template>
<script>
import detail from "./detailPage.vue"
import detail1 from "./detail1Page.vue"
export default {
    components:{
      detail,
      detail1
    }
}
</script>