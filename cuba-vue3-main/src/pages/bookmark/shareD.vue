<template>
  <div class="fade tab-pane" v-bind:class="(activeclass==='pills_shared') ? 'active show': ''" id="pills-shared" role="tabpanel" aria-labelledby="pills-shared-tab">
  <div class="card mb-0">
    <div class="card-header d-flex">
      <h6 class="f-w-600 mb-0">Shared with me</h6>
      <ul>
        <li>
          <a class="grid-bookmark-view" href="#"><vue-feather type="grid"></vue-feather></a>
        </li>
        <li>
          <a class="list-layout-view" href="#"><vue-feather type="list"></vue-feather></a>
        </li>
      </ul>
    </div>
    <div class="card-body">
      <div class="details-bookmark text-center">
        <span>No Bookmarks Found.</span>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import { mapGetters, mapState } from 'vuex';


export default{
    
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
    }
  },
}
</script>