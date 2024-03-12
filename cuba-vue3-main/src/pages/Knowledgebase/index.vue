<template>
    <div>
      <Breadcrumbs main title="Knowledge Base" />
  
      <div class="container-fluid knowledgebase-page">
        <div class="row">
          <div class="col-12">
            <div class="knowledgebase-bg">
              <img
                class="bg-img-cover bg-center img-fluid"
                src="../../assets/images/knowledgebase/bg_1.jpg"
                alt="looginpage"
              />
            </div>
            <div class="knowledgebase-search">
              <div>
                <h3>How Can I help you?</h3>
                <form class="form-inline" action="#" method="get">
                  <div class="form-group w-100">
                    <vue-feather type="search"></vue-feather>
                    <input
                      class="form-control-plaintext w-100"
                      type="text"
                      placeholder="Type question here"
                      title=""
                    />
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div class="col-xl-4 xl-50 col-sm-6">
            <px-card class="bg-primary">
              <template v-slot:with-padding>
                <div class="media faq-widgets">
                  <div class="media-body">
                    <h5>Articles</h5>
                    <p>
                      Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                      Aenean commodo ligula eget dolor. Aenean massa. Cum sociis
                      natoque penatibus et magnis dis parturient montes, nascetur
                      ridiculus mus.
                    </p>
                  </div>
                  <i data-feather="book-open"></i>
                </div>
              </template>
            </px-card>
          </div>
          <div class="col-xl-4 xl-50 col-sm-6">
            <px-card class="bg-primary">
              <template v-slot:with-padding>
                <div class="media faq-widgets">
                  <div class="media-body">
                    <h5>Knowledgebase</h5>
                    <p>
                      Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                      Aenean commodo ligula eget dolor. Aenean massa. Cum sociis
                      natoque penatibus et magnis dis parturient montes, nascetur
                      ridiculus mus.
                    </p>
                  </div>
                  <i data-vue-feather="book-open"></i>
                </div>
            </template>
            </px-card>
          </div>
          <div class="col-xl-4 xl-100">
            <px-card class="bg-primary">
              <template v-slot:with-padding>
                <div class="media faq-widgets">
                  <div class="media-body">
                    <h5>Support</h5>
                    <p>
                      Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                      Aenean commodo ligula eget dolor. Aenean massa. Cum sociis
                      natoque penatibus et magnis dis parturient montes, nascetur
                      ridiculus mus.
                    </p>
                  </div>
                  <i data-vue-feather="book-open"></i>
                </div>
              </template>
            </px-card>
          </div>
          <div class="col-sm-12">
            <div class="header-faq">
              <h5 class="mb-0">Browse articles by category</h5>
            </div>
            <div class="row">
              <div class="col-sm-12">
                <px-card title="Browse Articles" :actions="false">
                  <template v-slot:with-padding>
                    <div class="row browse">
                      <div
                        class="col-xl-4 xl-50 col-md-6"
                        v-for="(item, index) in knowledgebasedata"
                        :key="index"
                      >
                        <div class="browse-articles">
                          <h6>
                            <span><vue-feather type="archive"></vue-feather></span
                            >{{ item.title }}
                          </h6>
                          <ul>
                            <li>
                              <a href="#"
                                ><span><vue-feather type="file-text"></vue-feather> </span
                                ><span> {{ item.text1 }} </span></a
                              >
                            </li>
                            <li>
                              <a href="#"
                                ><span><vue-feather type="file-text"></vue-feather> </span
                                ><span> {{ item.text2 }} </span>
                                <span
                                  class="badge badge-primary pull-right"
                                  v-if="item.text2_badge"
                                >
                                  {{ item.text2_badge }}
                                </span></a
                              >
                            </li>
                            <li>
                              <a href="#"
                                ><span><vue-feather type="file-text"></vue-feather> </span
                                ><span> {{ item.text3 }} </span></a
                              >
                            </li>
                            <li>
                              <a href="#"
                                ><span><vue-feather type="file-text"></vue-feather> </span
                                ><span> {{ item.text4 }} </span></a
                              >
                            </li>
                            <li>
                              <a href="#"
                                ><span
                                  ><vue-feather type="arrow-right"></vue-feather> </span
                                ><span> {{ item.text5 }} </span></a
                              >
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </template>
                </px-card>
              </div>
            </div>
          </div>
          <div class="col-lg-12">
            <div class="header-faq">
              <h5 class="mb-0">Featured Tutorials</h5>
            </div>
            <div class="row">
              <div class="col-xl-3 xl-50 col-md-6 box-col-6">
                <px-card :actions="false" class="features-faq product-box">
                  <template v-slot:headerCustom>
                    <div class="faq-image product-img">
                    <img
                      class="img-fluid"
                      src="../../assets/images/faq/1.jpg"
                      alt=""
                    />
                    <div class="product-hover">
                      <ul>
                        <li><i class="icon-link"></i></li>
                        <li><i class="icon-import"></i></li>
                      </ul>
                    </div>
                  </div>
                  </template>
                  <template v-slot:with-padding>
                    <h6>Web Design</h6>
                    <p>
                      Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                      Aenean commodo ligula eget dolor. Aenean massa. Cum sociis
                      natoque penatibus et magnis dis parturient montes, nascetur
                      ridiculus mus.
                    </p>
                  </template>
                  <template v-slot:footer>
                    <span>Dec 15, 2019</span
                    ><span class="pull-right"
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                    ></span>
                  </template>
                </px-card>
              </div>
              <div class="col-xl-3 xl-50 col-md-6 box-col-6">
                <px-card :actions="false" class="features-faq product-box">
                  <template v-slot:headerCustom>
                    <div class="faq-image product-img">
                    <img
                      class="img-fluid"
                      src="../../assets/images/faq/2.jpg"
                      alt=""
                    />
                    <div class="product-hover">
                      <ul>
                        <li><i class="icon-link"></i></li>
                        <li><i class="icon-import"></i></li>
                      </ul>
                    </div>
                  </div>
                  </template>
                  <template v-slot:with-padding>
                    <h6>Web Development</h6>
                    <p>
                      Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                      Aenean commodo ligula eget dolor. Aenean massa. Cum sociis
                      natoque penatibus et magnis dis parturient montes, nascetur
                      ridiculus mus.
                    </p>
                  </template>
                  <template v-slot:footer>
                    <span>Dec 15, 2019</span
                    ><span class="pull-right"
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                    ></span>
                  </template>
                </px-card>
              </div>
              <div class="col-xl-3 xl-50 col-md-6 box-col-6">
                <px-card :actions="false" class="features-faq product-box">
                  <template v-slot:headerCustom>
                    <div class="faq-image product-img">
                    <img
                      class="img-fluid"
                      src="../../assets/images/faq/3.jpg"
                      alt=""
                    />
                    <div class="product-hover">
                      <ul>
                        <li><i class="icon-link"></i></li>
                        <li><i class="icon-import"></i></li>
                      </ul>
                    </div>
                  </div>
                  </template>
                  <template v-slot:with-padding>
                    <h6>UI Design</h6>
                    <p>
                      Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                      Aenean commodo ligula eget dolor. Aenean massa. Cum sociis
                      natoque penatibus et magnis dis parturient montes, nascetur
                      ridiculus mus.
                    </p>
                  </template>
                  <template v-slot:footer>
                    <span>Dec 15, 2019</span
                    ><span class="pull-right"
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                    ></span>
                  </template>
                </px-card>
              </div>
              <div class="col-xl-3 xl-50 col-md-6 box-col-6">
                <px-card :actions="false" class="features-faq product-box">
                  <template v-slot:headerCustom>
                    <div class="faq-image product-img">
                    <img
                      class="img-fluid"
                      src="../../assets/images/faq/4.jpg"
                      alt=""
                    />
                    <div class="product-hover">
                      <ul>
                        <li><i class="icon-link"></i></li>
                        <li><i class="icon-import"></i></li>
                      </ul>
                    </div>
                  </div>
                  </template>
                  <template v-slot:with-padding>
                    <h6>UX Design</h6>
                    <p>
                      Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                      Aenean commodo ligula eget dolor. Aenean massa. Cum sociis
                      natoque penatibus et magnis dis parturient montes, nascetur
                      ridiculus mus.
                    </p>
                  </template>
                  <template v-slot:footer>
                    <span>Dec 15, 2019</span
                    ><span class="pull-right"
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                      ><i class="fa fa-star font-primary"></i
                    ></span>
                  </template>
                </px-card>
              </div>
            </div>
          </div>
          <div class="col-lg-12">
            <div class="header-faq">
              <h5 class="mb-0">Latest articles and videos</h5>
            </div>
            <div class="row">
              <div class="col-xl-4 col-md-6">
                <div class="row">
                  <div class="col-sm-12">
                    <px-card :actions="false" >
                      <template v-slot:with-padding>
                        <div class="media">
                          <vue-feather type="codepen" class="m-r-30"></vue-feather>
                          <div class="media-body">
                            <h6 class="f-w-600">Using Video</h6>
                            <p>
                              Cras dapibus. Vivamus elementum semper nisi. Aenean
                              vulputate eleifend tellus.
                            </p>
                          </div>
                        </div>
                      </template>
                    </px-card>
                  </div>
                  <div class="col-sm-12">
                    <px-card :actions="false" >
                      <template v-slot:with-padding>
                        <div class="media">
                          <vue-feather type="codepen" class="m-r-30"></vue-feather>
                          <div class="media-body">
                            <h6 class="f-w-600">Vel illum qu</h6>
                            <p>
                              Cras dapibus. Vivamus elementum semper nisi. Aenean
                              vulputate eleifend tellus.
                            </p>
                          </div>
                        </div>
                      </template>
                    </px-card>
                  </div>
                  <div class="col-sm-12">
                    <px-card :actions="false" >
                      <template v-slot:with-padding>
                        <div class="media">
                          <vue-feather type="codepen" class="m-r-30"></vue-feather>
                          <div class="media-body">
                            <h6 class="f-w-600">Cum sociis natoqu</h6>
                            <p>
                              Cras dapibus. Vivamus elementum semper nisi. Aenean
                              vulputate eleifend tellus.
                            </p>
                          </div>
                        </div>
                      </template>
                    </px-card>
                  </div>
                </div>
              </div>
              <div class="col-xl-4 col-md-6">
                <div class="row">
                  <div class="col-sm-12">
                    <px-card :actions="false" >
                      <template v-slot:with-padding>
                        <div class="media">
                          <vue-feather type="file-text" class="m-r-30"></vue-feather>
                          <div class="media-body">
                            <h6 class="f-w-600">Donec pede justo</h6>
                            <p>
                              Cras dapibus. Vivamus elementum semper nisi. Aenean
                              vulputate eleifend tellus.
                            </p>
                          </div>
                        </div>
                      </template>
                    </px-card>
                  </div>
                  <div class="col-sm-12">
                    <px-card :actions="false" >
                      <template v-slot:with-padding>
                        <div class="media">
                          <vue-feather type="file-text" class="m-r-30"></vue-feather>
                          <div class="media-body">
                            <h6 class="f-w-600">Nam quam nunc</h6>
                            <p>
                              Cras dapibus. Vivamus elementum semper nisi. Aenean
                              vulputate eleifend tellus.
                            </p>
                          </div>
                        </div>
                      </template>
                    </px-card>
                  </div>
                  <div class="col-sm-12">
                    <px-card :actions="false" >
                      <template v-slot:with-padding>
                        <div class="media">
                          <vue-feather type="file-text" class="m-r-30"></vue-feather>
                          <div class="media-body">
                            <h6 class="f-w-600">Using Video</h6>
                            <p>
                              Cras dapibus. Vivamus elementum semper nisi. Aenean
                              vulputate eleifend tellus.
                            </p>
                          </div>
                        </div>
                      </template>
                    </px-card>
                  </div>
                </div>
              </div>
              <div class="col-xl-4">
                <div class="row">
                  <div class="col-xl-12 col-md-6">
                    <px-card :actions="false" >
                      <template v-slot:with-padding>
                        <div class="media">
                          <vue-feather type="youtube" class="m-r-30"></vue-feather>
                          <div class="media-body">
                            <h6 class="f-w-600">Vel illum qu</h6>
                            <p>
                              Cras dapibus. Vivamus elementum semper nisi. Aenean
                              vulputate eleifend tellus.
                            </p>
                          </div>
                        </div>
                      </template>
                    </px-card>
                  </div>
                  <div class="col-xl-12 col-md-6">
                    <px-card :actions="false" >
                      <template v-slot:with-padding>
                        <div class="media">
                          <vue-feather type="youtube" class="m-r-30"></vue-feather>
                          <div class="media-body">
                            <h6 class="f-w-600">Cum sociis natoqu</h6>
                            <p>
                              Cras dapibus. Vivamus elementum semper nisi. Aenean
                              vulputate eleifend tellus.
                            </p>
                          </div>
                        </div>
                      </template>
                    </px-card>
                  </div>
                  <div class="col-xl-12">
                    <px-card :actions="false" >
                      <template v-slot:with-padding>
                        <div class="media">
                          <vue-feather type="youtube" class="m-r-30"></vue-feather>
                          <div class="media-body">
                            <h6 class="f-w-600">Donec pede justo</h6>
                            <p>
                              Cras dapibus. Vivamus elementum semper nisi. Aenean
                              vulputate eleifend tellus.
                            </p>
                          </div>
                        </div>
                      </template>
                    </px-card>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
    import { mapState } from 'vuex';
    import pxcard from '../../components/Pxcard.vue'
    export default {
        components:{
    'px-card': pxcard
  },
      data() {
        return {};
      },
      computed: {
        ...mapState({
            knowledgebasedata: (state) => state.common.knowledgebasedata,
        }),
      },
    };
  </script>
  
  <style>
  .search-form.search-knowledge .form-group {
    position: relative;
  }
  .search-form.search-knowledge .form-group:after {
    position: absolute;
    content: "\F002";
    font-family: FontAwesome;
    top: 10px;
    left: 30px;
  }
  </style>