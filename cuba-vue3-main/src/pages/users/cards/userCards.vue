<template>
<Breadcrumbs title="User Cards" main="User"  />
<!-- Container-fluid starts-->
<div class="container-fluid ">
    <div class="row">
       <card1/>
       <card2/>
       <card3/>
       <card4/>
    </div>
</div>
<!-- Container-fluid Ends-->
</template>

<script>
// import data from '../../../data/usercard.json'
import card1 from './card1.vue';
import card2 from './card2.vue';
import card3 from './card3.vue';
import card4 from './card4.vue';
export default {
    name: 'userCards',
    components:{
card1,card2,card3,card4
    }
    // data() {
    //     return {
    //         menu: data.data
    //     }
    // },
    // methods: {
    //     getImgUrl(path) {
    //         return require('../../../assets/images/' + path)
    //     }
    // },
    // mounted() {
    //     console.log("data", this.menu)
    // }
}
</script>
