<template>
<breadCrumbs title="Email Application" main="Email" title1="Email Inbox" />

<!-- Container-fluid starts-->
<div class="container-fluid">
    <div class="email-wrap">
        <div class="row">
            <sidePage/>
            <div class="col-xl-9 col-md-12 xl-70 box-col-70">
                <div class="email-right-aside">
                    <div class="card email-body">
                        <div class="email-profile">
                            <div>
                                <div class="pe-0 b-r-light"></div>
                                <div class="email-top">
                                    <div class="row">
                                        <div class="col-12">
                                            <div class="d-flex">
                                                <label class="email-chek d-block">
                                                    <input class="checkbox_animated" v-model="checkAll" type="checkbox">
                                                </label>
                                                <div class="flex-grow-1">
                                                    <div class="dropdown">
                                                        <button class="btn btn-primary dropdown-toggle" :class="this.active?'show': ''" id="dropdownMenuButton" type="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false"  @click="isActive()">Action</button>
                                                        <div class="dropdown-menu" :class="this.active? 'show':''" aria-labelledby="dropdownMenuButton" ><a class="dropdown-item" href="javascript:void(0)">Refresh</a><a class="dropdown-item" href="javascript:void(0)">Mark as important</a><a class="dropdown-item" href="javascript:void(0)">Move to span</a><a class="dropdown-item" href="javascript:void(0)">Move to trush </a></div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inbox">
                                    <div class="d-flex" v-for="(item,index) in menu" :key="index">
                                        <div class="d-flex-size-email">
                                            <label class="d-block mb-0">
                                                <input class="checkbox_animated" v-model="item.checkbox" type="checkbox"  >
                                            </label>
                                            <vue-feather class="like" type="star"></vue-feather><img class="me-3 rounded-circle" :src="getImgUrl(item.image)" alt="">
                                        </div>
                                        <div class="flex-grow-1">
                                            <h6>{{item.name}} </h6>
                                            <p>{{item.text}}</p><span>{{item.time}}</span>
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
<!-- Container-fluid Ends-->
</template>

<script>
import sidePage from '../sidePage.vue' 
import mailData from '../../../data/mailInbox.json'
export default {
    
    name: 'mailInbox',
    data() {
        return {
            menu: mailData.data,
            checkAll:false,
            active: false
        }
    },
    components:{
        sidePage
    },
watch:{
    checkAll:function(){
        // console.log('comming to checkall',this.checkAll)
        if(this.checkAll){
            this.menu.forEach(item=>{item.checkbox=true})
        }else{
            this.menu.forEach(item=>{item.checkbox=false})
        }
    }
},  
    methods: {
        getImgUrl(path) {
            return require("../../../assets/images/" + path);
        },
        isActive(){
            this.active = !this.active
        }
    }

}
</script>
