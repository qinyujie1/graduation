<template>
  <div class="container-fluid faq-section">
    <div class="row">
      <div class="col-12">
        <div class="knowledgebase-bg"><img class="bg-img-cover bg-center" src="@/assets/images/knowledgebase/bg_1.jpg" alt="Background Image1"></div>
        <div class="knowledgebase-search">
          <div>
            <h3>How Can I help you?</h3>
            <form class="form-inline" action="#" method="get">
              <div class="form-group w-100 mb-0"><i data-feather="search"></i>
                <input class="form-control-plaintext w-100" type="text" placeholder="Type question here" title="">
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="col-xl-4 xl-50 col-lg-6 box-col-6">
        <div class="card bg-primary">
          <div class="card-body">
            <div class="d-flex faq-widgets">
              <div class="flex-grow-1">
                <h2>Articles</h2>
                <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
              </div><i data-feather="book-open"></i>
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-4 xl-50 col-lg-6 box-col-6">
        <div class="card bg-primary">
          <div class="card-body">
            <div class="d-flex faq-widgets">
              <div class="flex-grow-1">
                <h2>Knowledgebase</h2>
                <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
              </div><i data-feather="aperture"></i>
            </div>
          </div>
        </div>
      </div>
      <div class="col-xl-4 col-lg-12 xl-100 box-col-12">
        <div class="card bg-primary">
          <div class="card-body">
            <div class="d-flex faq-widgets">
              <div class="flex-grow-1">
                <h2>Support</h2>
                <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
              </div><vue-feather type="file-text"></vue-feather>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-12">
        <div class="header-faq">
          <h5 class="mb-0">knowledge articles by category</h5>
        </div>
        <div class="row browse">
          <div class="col-xl-4 xl-50 col-md-6 box-col-50" v-for="index in data" :key="index">
            <div class="browse-articles">
              <h3><span><vue-feather type="file-text"></vue-feather></span>{{index}}</h3>
              <ul>
                <li><router-link to="/knowledgebase/detail">
                    <h5><vue-feather type="file-text"></vue-feather>Lorem Ipsum is simply dummy text of the printing</h5></router-link></li>
                <li><router-link to="/knowledgebase/detail">
                    <h5><vue-feather type="file-text"> </vue-feather>Lorem Ipsum has been the industry's standard dummy </h5></router-link></li>
                <li><router-link to="/knowledgebase/detail">
                    <h5><vue-feather type="file-text"></vue-feather>When an unknown printer took a galley </h5></router-link></li>
                <li><router-link to="/knowledgebase/detail">
                    <h5><vue-feather type="file-text"></vue-feather>But also the leap into electronic typesetting, </h5></router-link></li>
                <li><router-link class="f-w-600 font-primary" to="/knowledgebase/detail"><vue-feather class="me-1" type="arrow-right"></vue-feather><span>See More (40)</span></router-link></li>
              </ul>
            </div>
          </div>
         
          <div class="col-xl-4 xl-100 box-col-50">
            <div class="browse-articles browse-bottom">
              <h3><span><vue-feather type="archive"></vue-feather></span>Integrating WordPress with Your Website</h3>
              <ul>
                <li><router-link to="/knowledgebase/detail">
                    <h5><vue-feather type="file-text"></vue-feather>Lorem Ipsum passage, and going through</h5></router-link></li>
                <li><router-link to="/knowledgebase/detail">
                    <h5><vue-feather type="file-text"></vue-feather>The first line of Lorem Ipsum,  Lorem ipsum </h5></router-link></li>
                <li><router-link to="/knowledgebase/detail">
                    <h5><vue-feather type="file-text"></vue-feather>Thus comes from a line in section</h5></router-link></li>
                <li><router-link to="/knowledgebase/detail">
                    <h5><vue-feather type="file-text"></vue-feather>First true generator on the Internet</h5></router-link></li>
                <li><router-link class="f-w-600 font-primary" to="/knowledgebase/detail">                                              <i class="me-1" data-feather="arrow-right"></i><span>See More (34)</span></router-link></li>
              </ul>
            </div>
          </div>
        </div>  
      </div>
    </div>
  </div>
</template>
<script>

export default {
  data(){
    return{
    data:['Quick Questions are answered','Integrating WordPress with Your Website','WordPress Site Maintenance','Meta Tags in WordPress','WordPress in Your Language','Know Your Sources','Validating a Website','Quick Questions are answered']
  }}
   }
</script>