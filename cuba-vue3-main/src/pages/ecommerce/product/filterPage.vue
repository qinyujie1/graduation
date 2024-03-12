<template>
<div class="left-filter">
    <div class="card-body filter-cards-view animate-chk">
        <div class="product-filter" v-for="(item,index) in category" :key="index">
            <h6 class="f-w-600">{{item.title}}</h6>
            <div class="checkbox-animated mt-0" v-for="(child,index) in item.children" :key="index">
                <label class="d-block" :for=child.id >
                    <input class="checkbox_animated" @change="addfilter()" :value="child.name" v-model="applyFilter" :id=child.id type="checkbox" data-original-title="" title="">{{child.name}}
                </label>

            </div>
        </div>

        <div class="product-filter slider-product">
            <h6 class="f-w-600">Colors</h6>
            <div class="color-selector">
                <ul>
                    <li class="active white"></li>
                    <li class="bg-primary" value="yellow" @change="selectColor($event)" :class="{'active': isActive}"></li>
                    <li class="bg-secondary"></li>
                    <li class="bg-success"></li>
                    <li class="bg-warning"></li>
                    <li class="bg-danger"></li>
                    <li class="blue"></li>
                    <li class="red"></li>
                </ul>
            </div>
        </div>
        <div class="product-filter pb-0">
            <h6 class="f-w-600"> Price 
                <input type="range"  :min="min" :max="max"  v-model="start"  @change="setchange()"> </h6>
                <h6 class="f-w-600">New Products</h6>
            <!-- <vue-slider v-model="value" :min="0" :max="800" ref="slider" @change="sliderChange($refs.slider.getValue())">
            </vue-slider> -->
        </div>
        <!-- <carousel> -->
            <div class="product-filter pb-0 new-products">
                <div class="owl-carousel owl-theme" id="testimonial">
                  <div class="item">
                    <div class="product-box row">
                      <div class="product-img col-md-5"><img class="img-fluid img-100" src="@/assets/images/ecommerce/01.jpg" alt="" data-original-title="" title=""></div>
                      <div class="product-details col-md-7 text-start"><span><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning"></i></span>
                        <p class="mb-0">Woman T-shirt</p>
                        <div class="product-price">$100.00</div>
                      </div>
                    </div>
                    <div class="product-box row mt-2">
                      <div class="product-img col-md-5"><img class="img-fluid img-100" src="@/assets/images/ecommerce/02.jpg" alt="" data-original-title="" title=""></div>
                      <div class="product-details col-md-7 text-start"><span><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning"></i></span>
                        <p class="mb-0">Beauty Fashion</p>
                        <div class="product-price">$150.00</div>
                      </div>
                    </div>
                    <div class="product-box row mt-2">
                      <div class="product-img col-md-5"><img class="img-fluid img-100" src="@/assets/images/ecommerce/03.jpg" alt="" data-original-title="" title=""></div>
                      <div class="product-details col-md-7 text-start"><span><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning me-1"></i><i class="fa fa-star font-warning"></i></span>
                        <p class="mb-0">Voxati</p>
                        <div class="product-price">$200.00</div>
                      </div>
                    </div>
                    </div>
                </div>
              </div>
        <!-- </carousel> -->
        <div class="product-filter text-center"><img class="img-fluid banner-product" src="@/assets/images/ecommerce/banner.jpg" alt="" data-original-title="" title=""></div>
    </div>
</div>
</template>

<script>
// import VueSlider from 'vue-slider-component';
// import {
//     swiper,
//     swiperSlide
// } from 'vue-awesome-swiper';
// import 'swiper/css/swiper.css';
import {
    category
} from '../../../data/ecommerce/filter'
// import carousel from 'vue-owl-carousel'
const _ = require("lodash");
import{ mapGetters} from 'vuex'
export default {
    name: 'filterPage',
    data() {
        return {
            min: 0,
            max: 0,
            start: 0,
            category: category,
            applyFilter: [],
            filter: false,
            isActive: false
            // value: [this.min,this.max],
            // swiperOption: {
            //     loop: true,
            //     navigation: {
            //         nextEl: '.swiper-button-next',
            //         prevEl: '.swiper-button-prev'
            //     }
            // }
           
        }
    },
    components: {
        // VueSlider,
        // swiper,
        // swiperSlide
    },
    computed:{
        ...mapGetters({
            price: 'product/price',      
            filterProduct: 'product/filterProducts'
    })},

    mounted()
    {
         var vm = this,
            max = _.maxBy(this.price),
            min = _.minBy(this.price)
        vm.start = max
        vm.min= min,
        vm.max=max
        this.$store.dispatch('product/priceFilter',{min: this.min, max: this.start});
        },
    methods: {
    selectColor(event)
    {
        this.isActive= !this.isActive
        this.applyFilter.push(event.target.value) 
        this.$store.dispatch('product/setTags',this.applyFilter);
        console.log('dda',event.target.value)
      },
    
        addfilter() {
            // this.$emit('allFilters ', this.applyFilter)
            // this.applyFilter= val
            this.$store.dispatch('product/setTags', this.applyFilter);

        },
        setchange()
         {
        this.$store.dispatch('product/priceFilter',{min: this.min, max: this.start});
    }

      },
     
    }
</script>
