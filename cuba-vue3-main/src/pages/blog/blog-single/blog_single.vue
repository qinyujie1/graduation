<template>
  <Breadcrumbs title="Blog Single" main="Blog"  />
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <div class="blog-single">
          <div class="blog-box blog-details"><img class="img-fluid w-100" src="@/assets/images/blog/blog-single.jpg" alt="blog-main">
            <div class="blog-details">
              <ul class="blog-social">
                <li>25 July 2018</li>
                <li><i class="icofont icofont-user"></i>Mark <span>Jecno </span></li>
                <li><i class="icofont icofont-thumbs-up"></i>02<span>Hits</span></li>
                <li><i class="icofont icofont-ui-chat"></i>598 Comments</li>
              </ul>
              <h4>
                All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the
                Internet.
              </h4>
              <div class="single-blog-content-top">
                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
                <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like</p>
              </div>
            </div>
          </div>
                  <comment/>
                </div>
              </div>
            </div>
           </div>
</template>
<script>
import comment from "./commentPage.vue"
export default {
    components:{
        comment
    }
}
</script>