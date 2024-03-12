<template>
<div class="container-fluid product-wrapper" :class="{'sidebaron' : isActive}">
    <div class="product-grid">
        <div class="feature-products">
            <div class="row">
                <div class="col-md-6 products-total">
                    <div class="square-product-setting d-inline-block"><a class="icon-grid grid-layout-view" @click="gridView()">
                            <vue-feather type="grid"></vue-feather>
                        </a></div>
                    <div class="square-product-setting d-inline-block"><a class="icon-grid m-0 list-layout-view" @click="listView()">
                            <vue-feather type="list"></vue-feather>
                        </a></div>
                    <span class="d-none-productlist filter-toggle" @click="disp()">Filters
                        <span class="ms-2">
                                <vue-feather class="toggle-data" type="chevron-down"></vue-feather>
                            </span> 
                    </span>
                    <div class="grid-options d-inline-block">
                        <ul>
                            <li @click="grid2()"><a class="product-2-layout-view" href="javascript:void(0)" data-original-title="" title=""><span class="line-grid line-grid-1 bg-primary"></span><span class="line-grid line-grid-2 bg-primary"></span></a></li>
                            <li @click="grid3()"><a class="product-3-layout-view" href="javascript:void(0)" data-original-title="" title=""><span class="line-grid line-grid-3 bg-primary"></span><span class="line-grid line-grid-4 bg-primary"></span><span class="line-grid line-grid-5 bg-primary"></span></a></li>
                            <li @click="grid4()"><a class="product-4-layout-view" href="javascript:void(0)" data-original-title="" title=""><span class="line-grid line-grid-6 bg-primary"></span><span class="line-grid line-grid-7 bg-primary"></span><span class="line-grid line-grid-8 bg-primary"></span><span class="line-grid line-grid-9 bg-primary"></span></a></li>
                            <li @click="grid6()"><a class="product-6-layout-view" href="javascript:void(0)" data-original-title="" title=""><span class="line-grid line-grid-10 bg-primary"></span><span class="line-grid line-grid-11 bg-primary"></span><span class="line-grid line-grid-12 bg-primary"></span><span class="line-grid line-grid-13 bg-primary"></span><span class="line-grid line-grid-14 bg-primary"></span><span class="line-grid line-grid-15 bg-primary"></span></a></li>
                        </ul>
                    </div>
                </div>
                <sortingPage />
            </div>
            <div class="row">
                <div class="col-sm-3">
                    <!-- <div class="pro-filter-sec"> -->
                        <div class="product-sidebar" :class="{'open':isActive}">
                            <div class="filter-section">
                                <div class="card">
                                    <div class="card-header">
                                        <h6 class="mb-0 f-w-600">Filters<span class="pull-right"><i class="fa fa-chevron-down toggle-data" @click.prevent="disp()"></i></span></h6>
                                    </div>
                                    <filterPage />
                                </div>
                            </div>
                        </div></div>
                        <div class="col-md-9 col-sm-12">
                            <form>
                                <div class="form-group m-0">
                                    <input class="form-control" type="search" placeholder="Search.." data-original-title="" title=""><i class="fa fa-search"></i>
                                </div>
                            </form>
                        </div>
                    <!-- </div> -->
                
            </div>
        </div>
        <productView />
    </div>
</div>
</template>

<script>
//import {mapGetters} from 'vuex'
import filterPage from './filterPage.vue'
import productView from './productView.vue'
import sortingPage from './sortingPage.vue'
export default {
    name: 'topPage',
    data() {
        return {
            isActive: false,
            modalShow: false,
            quickViewProduct: [],
            counter: 1,
            priceArray: [],
            allfilters: [],
            items: [],
            filtered: false,
        }
    },
    components: {
        filterPage,
        productView,
        sortingPage
    },
    methods: {
        grid2() {
            this.$store.commit('product/grid2', true);
        },
        grid3() {
            this.$store.commit('product/grid3');
        },
        grid4() {
            this.$store.commit('product/grid4');
        },
        grid6() {
            this.$store.commit('product/grid6');
        },
        listView() {
            this.$store.commit('product/listView');
        },
        gridView() {
            this.$store.commit('product/grid6');
        },
        disp() {
            
            this.isActive = !this.isActive
        },
        // allfilter(selectedVal) {
        // this.allfilters = selectedVal;
        // this.$store.dispatch('products/setTags', selectedVal);
        // },  
        // pricefilterArray(item) {
        //   this.$store.dispatch('products/priceFilter', item);
        // },
    }
}
</script>
