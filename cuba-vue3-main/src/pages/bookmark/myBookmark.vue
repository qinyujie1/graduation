<template>
    <div class="fade tab-pane" v-bind:class="(activeclass==='pills_bookmark') ? 'active show': ''" id="pills-bookmark" role="tabpanel" aria-labelledby="pills-bookmark-tab">
        <div class="card mb-0">
      <div class="card-header d-flex">
        <h6 class="f-w-600 mb-0">My Bookmark</h6>
        <ul>
          <li><a class="grid-bookmark-view" href="javascript:void(0);"><vue-feather type="grid" @click="liststyle = !liststyle"></vue-feather></a></li> 
          <li><a class="list-layout-view" href="javascript:void(0);"><vue-feather type="list" @click="liststyle = !liststyle"></vue-feather></a></li>  
        </ul>
      </div>
      <div class="card-body pb-0">
        <div class="details-bookmark text-center" v-bind:class="{ 'list-bookmark' : liststyle}">
          <div class="row" id="bookmarkData">
            <div class="col-xl-3 col-lg-6 col-md-4 col-sm-6 xl-50 box-col-6" v-for="(item,index) in bookmark" :key="index">
              <div class="card card-with-border bookmark-card o-hidden">
                <div class="details-website">
                  <img class="img-fluid" :src='getImgUrl(item.image)' alt="">
                  <div class="favourite-icon favourite_0"><a href="javascript:void(0)"><i class="fa fa-star"></i></a></div>
                  <div class="desciption-data">
                    <div class="title-bookmark">
                      <h6 class="title_0">{{ item.title }}</h6>
                      <p class="weburl_0">{{ item.website_url }}</p>
                      <div class="hover-block">
                        <ul>
                          <editBookmark/>
                          <li><a href="#"><vue-feather type="link"></vue-feather></a></li>
                          <li><a href="#"><vue-feather type="share-2"></vue-feather></a></li>
                          <li><a href="#"><vue-feather type="trash-2" v-on:click="basic_warning_alert(index)"></vue-feather></a></li>
                          <li class="pull-right text-end"><a href="#"><vue-feather type="tag"></vue-feather></a></li>
                        </ul>
                      </div>
                      <div class="content-general">
                        <p class="desc_0"> {{ item.desc }}</p><span class="collection_0">General</span>
                      </div>
                    </div>
                  </div>
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
import { mapGetters, mapState } from 'vuex';
import editBookmark from "./editBookmark.vue"

export default{
    components:{
        editBookmark
    },
    data(){
    return {
      liststyle: false,
      data : [],
   
      favourite : this.$store.state.common.favourite,
      filtered: false,
    };
  },
  computed: {
    ...mapState({
      bookmark: state => state.common.bookmark,
    }),
    ...mapGetters({
      activeclass: 'common/activeclass',  
    })
  },
  methods:{
    getImgUrl(path) {
      return require('@/assets/images/'+path);
    },
    say: function (message) {
      this.$store.dispatch('common/active',message);
    },
     collapseFilter() {
      this.filtered = !this.filtered;
    },
    setFavourite(item) {
      this.$store.dispatch('common/setFavourite',item)
    },
    getActive(itemId) {
     this.$store.dispatch('common/getActive', itemId)
    },
    basic_warning_alert:function(item){
        this.$swal({
            icon: 'warning',
            title:"Are you sure?",
          text:'Once deleted, you will not be able to recover this imaginary file!',
          showCancelButton: true,
           confirmButtonText: 'Ok',
          confirmButtonColor: '#e64942',
          cancelButtonText: 'Cancel',
          cancelButtonColor: '#efefef',
        }).then((result)=>{
          if(result.value){
            this.bookmark.splice(item,1)
            this.$swal({
             icon: 'success',
              text:'Poof! Your imaginary file has been deleted!',
              type:'success',
                
            });
          }else{
            this.$swal({
              text:'Your imaginary file is safe!'
            });
          }
        });
      },
  },
}
</script>