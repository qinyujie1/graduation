<template>
<Breadcrumbs main="Ecommerce" title="Product Page" />
<!-- Container-fluid starts-->
<div class="container-fluid">
    <div>
        <div class="row product-page-main p-0">
            <div class="col-xxl-4 col-md-6 box-col-12">
                <div class="card">
                    <div class="card-body">
                        <swiper :slides-per-view="1" :space-between="20" :pagination="{
                                      clickable: true,
                                    }" :modules="modules" class="product-slider swiper- ">
                            <swiper-slide v-for="(product, index) in products" :key="index" class="item swiper-slide">
                                <img :src="getImgUrl(product)" :id="index" alt="index" />
                            </swiper-slide>

                        </swiper>
                        <swiper :slides-per-view="3" :spaceBetween="30" :pagination="{
                                    clickable: true,
                                  }" :modules="modules" class="swiper-wraper">
                            <swiper-slide v-for="(product, index) in products" :key="index" class="item">
                                <img :src="getImgUrl(product)" alt="index">
                            </swiper-slide>
                        </swiper>

                    </div>
                </div>
            </div>
            <div class="col-xl-5 box-col-6 proorder-xl-3 xl-100">
                <div class="card">
                    <div class="card-body">
                        <div class="pro-group pt-0 border-0">
                            <div class="product-page-details mt-0">
                                <h3>Women Pink shirt.</h3>
                                <div class="pro-review">
                                    <div class="d-flex">
                                        <select id="u-rating-fontawesome" name="rating" autocomplete="off">
                                            <option value="1">1</option>
                                            <option value="2">2</option>
                                            <option value="3">3</option>
                                            <option value="4">4</option>
                                            <option value="5">5</option>
                                        </select><span>(250 review)</span>
                                    </div>
                                </div>
                            </div>
                            <div class="product-price">$26.00
                                <del>$350.00 </del>
                            </div>
                            <div class="color-selector">
                                <ul>
                                    <li class="active white"></li>
                                    <li class="bg-primary"> </li>
                                    <li class="bg-secondary"></li>
                                    <li class="bg-success"></li>
                                    <li class="bg-warning"></li>
                                    <li class="bg-danger"></li>
                                </ul>
                            </div><a class="btn btn-secondary mt-0" href="cart.html"><i class="fa fa-shopping-cart me-2"></i>Buy Now</a>
                        </div>
                        <div class="pro-group">
                            <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that.</p>
                        </div>
                        <div class="pro-group">
                            <div class="row">
                                <div class="col-md-6">
                                    <table>
                                        <tbody>
                                            <tr>
                                                <td> <b>Availability &nbsp;: &nbsp;</b></td>
                                                <td class="txt-success">In stock</td>
                                            </tr>
                                            <tr>
                                                <td> <b>Brand &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:</b></td>
                                                <td>Pixelstrap</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                <div class="col-md-6">
                                    <table>
                                        <tbody>
                                            <tr>
                                                <td> <b>Seller &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;: &nbsp;&nbsp;&nbsp;</b></td>
                                                <td>ABC</td>
                                            </tr>
                                            <tr>
                                                <td> <b>Fabric &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;: &nbsp;&nbsp;&nbsp;</b></td>
                                                <td>Cotton </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                        <div class="pro-group">
                            <div class="row">
                                <div class="col-md-4 xl-50 box-col-30">
                                    <h4 class="product-title">share it</h4>
                                </div>
                                <div class="col-md-7 xl-50 box-col-70">
                                    <div class="product-icon">
                                        <ul class="product-social">
                                            <li class="d-inline-block"><a href="https://www.facebook.com" target="_blank"><i class="fa fa-facebook"></i></a></li>
                                            <li class="d-inline-block"><a href="https://www.google.com/" target="_blank"><i class="fa fa-google-plus"></i></a></li>
                                            <li class="d-inline-block"><a href="https://twitter.com/" target="_blank"><i class="fa fa-twitter"></i></a></li>
                                            <li class="d-inline-block"><a href="https://www.instagram.com/" target="_blank"><i class="fa fa-instagram"> </i></a></li>
                                        </ul>
                                        <form class="d-inline-block f-right"> </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="pro-group pb-0">
                            <div class="pro-shop">
                                <div class="btn btn-primary m-r-10" @click="addToCart(quickViewProduct, counter)"> <i class="fa fa-shopping-basket me-2"></i>Add To Cart</div><a class="btn btn-danger" href="list-wish.html"><i class="fa fa-heart me-2"></i>Add To WishList </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-xl-2 col-md-6 box-col-6 xl-35 proorder-lg-1">
                <div class="card">
                    <div class="card-body">
                        <!-- side-bar colleps block stat-->
                        <div class="filter-block">
                            <h4>Brand </h4>
                            <ul>
                                <li>
                                    <div class="form-check">
                                        <input class="form-check-input" id="Raymond" type="checkbox" value="">
                                        <label class="form-check-label" for="Raymond">Raymond</label>
                                    </div>
                                </li>
                                <li>
                                    <div class="form-check">
                                        <input class="form-check-input" id="Pepe-Jeans" type="checkbox" value="">
                                        <label class="form-check-label" for="Pepe-Jeans">Pepe-Jeans</label>
                                    </div>
                                </li>
                                <li>
                                    <div class="form-check">
                                        <input class="form-check-input" id="Celio" type="checkbox" value="">
                                        <label class="form-check-label" for="Celio">Celio</label>
                                    </div>
                                </li>
                                <li>
                                    <div class="form-check">
                                        <input class="form-check-input" id="aime" type="checkbox" value="">
                                        <label class="form-check-label" for="aime">aime</label>
                                    </div>
                                </li>
                                <li>
                                    <div class="form-check">
                                        <input class="form-check-input" id="aliff" type="checkbox" value="">
                                        <label class="form-check-label" for="aliff">aliff</label>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                        <div class="collection-filter-block">
                            <ul class="pro-services">
                                <li>
                                    <div class="d-flex"><i data-feather="truck"></i>
                                        <div class="flex-grow-1">
                                            <h5>Free Shipping </h5>
                                            <p>Free Shipping World Wide</p>
                                        </div>
                                    </div>
                                </li>
                                <li>
                                    <div class="d-flex"><i data-feather="clock"></i>
                                        <div class="flex-grow-1">
                                            <h5>24 X 7 Service </h5>
                                            <p>Online Service For New Customer </p>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <!-- silde-bar colleps block end here-->
                </div>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="row product-page-main">
            <div class="col-sm-12">
                <ul class="nav nav-tabs border-tab mb-0" id="top-tab" role="tablist">
                    <li class="nav-item"><a class="nav-link active" id="top-home-tab" data-bs-toggle="tab" href="#top-home" role="tab" aria-controls="top-home" aria-selected="false">Fabric</a>
                        <div class="material-border"></div>
                    </li>
                    <li class="nav-item"><a class="nav-link" id="profile-top-tab" data-bs-toggle="tab" href="#top-profile" role="tab" aria-controls="top-profile" aria-selected="false">Video</a>
                        <div class="material-border"></div>
                    </li>
                    <li class="nav-item"><a class="nav-link" id="contact-top-tab" data-bs-toggle="tab" href="#top-contact" role="tab" aria-controls="top-contact" aria-selected="true">Details</a>
                        <div class="material-border"></div>
                    </li>
                    <li class="nav-item"><a class="nav-link" id="brand-top-tab" data-bs-toggle="tab" href="#top-brand" role="tab" aria-controls="top-brand" aria-selected="true">Brand</a>
                        <div class="material-border"></div>
                    </li>
                </ul>
                <div class="tab-content" id="top-tabContent">
                    <div class="tab-pane fade active show" id="top-home" role="tabpanel" aria-labelledby="top-home-tab">
                        <p class="mb-0 m-t-20">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
                        <p class="mb-0 m-t-20">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
                    </div>
                    <div class="tab-pane fade" id="top-profile" role="tabpanel" aria-labelledby="profile-top-tab">
                        <p class="mb-0 m-t-20">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
                    </div>
                    <div class="tab-pane fade" id="top-contact" role="tabpanel" aria-labelledby="contact-top-tab">
                        <p class="mb-0 m-t-20">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
                    </div>
                    <div class="tab-pane fade" id="top-brand" role="tabpanel" aria-labelledby="brand-top-tab">
                        <p class="mb-0 m-t-20">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- Container-fluid Ends-->
</template>

<script>
import {
    mapState
} from 'vuex'
import {
    Swiper,
    SwiperSlide
} from "swiper/vue";
import "swiper/css";
import "swiper/css/pagination";
import {
    Pagination
} from "swiper";
export default {
    name: "productPage",
    data() {
        return {
            counter: 1,
            modalShow: false,
            activeTab: 'fabric',
            // products: this.$store.state.products
            products: ['02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg', '08.jpg']
        }
    },
    // computed: {
    //     ...mapState({

    //         products: (state) =>
    //              state.products.data

    //     }),
    // swiper() {
    //     return this.$refs.mySwiper;
    // },
    // },
    components: {
        Swiper,
        SwiperSlide,
    },
    setup() {
        return {
            modules: [Pagination],
        };
    },
    methods: {
        addToCart: function (product, qty) {
            product.quantity = qty ? qty : 1;
            this.$store.dispatch("product/addToCart", product);

        },
        getImgUrl(path) {
            return require('../../../assets/images/ecommerce/' + path);
        },
    }
    // },
    // methods: {
    //     getImgUrl(path) {
    //         return require('../../../assets/images/' + path);
    //     },
    //     slideTo(id) {
    //         this.slideTo(id, 1000, false);
    //     },
    //     //Add to cart
    //     addToCart: function (product, qty) {
    //         product.quantity = qty ? qty : 1;
    //         this.$store.dispatch('products/addToCart', product);
    //     },
    //     increment() {
    //         if (this.counter < this.quickViewProduct.stock) this.counter++;
    //     },
    //     decrement() {
    //         if (this.counter > 1) this.counter--;
    //     },
    //     // Detail Tab
    //     tabContent(val) {
    //         this.activeTab = val;
    //     },

}
</script>
