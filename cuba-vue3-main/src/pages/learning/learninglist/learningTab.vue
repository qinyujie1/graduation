<template>
 
                        <div class="col-xl-3 xl-40 box-col-12 learning-filter">
                          <div class="md-sidebar"><a class="btn btn-primary email-aside-toggle md-sidebar-toggle" @click="isOpen">Learning filter</a>
                            <div class="md-sidebar-aside job-sidebar" :class="open?'open':''">
                              <div class="default-according style-1 faq-accordion job-accordion" id="accordionoc">
                                <div class="row">
                                  <div class="col-xl-12">
                                    <div class="card">
                                      <div class="card-header">
                                        <h5 class="mb-0">
                                          <button class="btn btn-link"  data-bs-target="#collapseicon" :aria-expanded="active?'false':'true'" aria-controls="collapseicon" @click="showOpen">Find Course</button>
                                        </h5>
                                      </div>
                                      <div class="collapse" :class="active?'':'show'"  id="collapseicon" aria-labelledby="collapseicon" data-bs-parent="#accordion">
                                        <div class="card-body filter-cards-view animate-chk">
                                          <div class="job-filter">
                                            <div class="faq-form">
                                              <input class="form-control" type="text" placeholder="Search.."><i class="search-icon" data-feather="search"></i>
                                            </div>
                                          </div>
                                          <div class="checkbox-animated">
                                            <div class="learning-header"><span class="f-w-600">Categories</span></div>
                                            <label class="d-block" for="chk-ani">
                                              <input class="checkbox_animated" id="chk-ani" type="checkbox">                      Accounting
                                            </label>
                                            <label class="d-block" for="chk-ani0">
                                              <input class="checkbox_animated" id="chk-ani0" type="checkbox">                            Design
                                            </label>
                                            <label class="d-block" for="chk-ani1">
                                              <input class="checkbox_animated" id="chk-ani1" type="checkbox">                            Development
                                            </label>
                                            <label class="d-block" for="chk-ani2">
                                              <input class="checkbox_animated" id="chk-ani2" type="checkbox">                            Management
                                            </label>
                                          </div>
                                          <div class="checkbox-animated mt-0">
                                            <div class="learning-header"><span class="f-w-600">Duration</span></div>
                                            <label class="d-block" for="chk-ani6">
                                              <input class="checkbox_animated" id="chk-ani6" type="checkbox">                            0-50 hours
                                            </label>
                                            <label class="d-block" for="chk-ani7">
                                              <input class="checkbox_animated" id="chk-ani7" type="checkbox">                            50-100 hours
                                            </label>
                                            <label class="d-block" for="chk-ani8">
                                              <input class="checkbox_animated" id="chk-ani8" type="checkbox">                            100+ hours
                                            </label>
                                          </div>
                                          <div class="checkbox-animated mt-0">
                                            <div class="learning-header"><span class="f-w-600">Price</span></div>
                                            <label class="d-block" for="edo-ani">
                                              <input class="radio_animated" id="edo-ani" type="radio" name="rdo-ani" checked="">                            All Courses
                                            </label>
                                            <label class="d-block" for="edo-ani1">
                                              <input class="radio_animated" id="edo-ani1" type="radio" name="rdo-ani" checked="">                            Paid Courses
                                            </label>
                                            <label class="d-block" for="edo-ani2">
                                              <input class="radio_animated" id="edo-ani2" type="radio" name="rdo-ani" checked="">                            Free Courses
                                            </label>
                                          </div>
                                          <div class="checkbox-animated mt-0">
                                            <div class="learning-header"><span class="f-w-600">Status</span></div>
                                            <label class="d-block" for="chk-ani3">
                                              <input class="checkbox_animated" id="chk-ani3" type="checkbox">                            Registration
                                            </label>
                                            <label class="d-block" for="chk-ani4">
                                              <input class="checkbox_animated" id="chk-ani4" type="checkbox">                            Progress
                                            </label>
                                            <label class="d-block" for="chk-ani5">
                                              <input class="checkbox_animated" id="chk-ani5" type="checkbox">                            Completed
                                            </label>
                                          </div>
                                          <button class="btn btn-primary text-center" type="button">Filter</button>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="col-xl-12">
                                    <div class="card">
                                      <div class="card-header">
                                        <h5 class="mb-0">
                                          <button class="btn btn-link" data-bs-target="#collapseicon1" :aria-expanded="active1?'false':'true'" aria-controls="collapseicon1" @click="showOpen1">Categories</button>
                                        </h5>
                                      </div>
                                      <div class="collapse card-body px-0 " :class="active1?'':'show'" id="collapseicon1" aria-labelledby="collapseicon1" data-bs-parent="#accordion">
                                        <div class="categories">
                                          <div class="learning-header"><span class="f-w-600">Design</span></div>
                                          <ul>
                                            <li><a href="#">UI Design </a><span class="badge badge-primary pull-right">28</span></li>
                                            <li><a href="#">UX Design </a><span class="badge badge-primary pull-right">35</span></li>
                                            <li><a href="#">Interface Design </a><span class="badge badge-primary pull-right">17</span></li>
                                            <li><a href="#">User Experience </a><span class="badge badge-primary pull-right">26</span></li>
                                          </ul>
                                        </div>
                                        <div class="categories pt-0">
                                          <div class="learning-header"><span class="f-w-600">Development</span></div>
                                          <ul>
                                            <li><a href="#">Frontend Development</a><span class="badge badge-primary pull-right">48</span></li>
                                            <li><a href="#">Backend Development</a><span class="badge badge-primary pull-right">19</span></li>
                                          </ul>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="col-xl-12">
                                    <div class="card">
                                      <div class="card-header">
                                        <h5 class="mb-0">
                                          <button class="btn btn-link"  data-bs-target="#collapseicon2" :aria-expanded="active2?'false':'true'" aria-controls="collapseicon2" @click="showOpen2">Upcoming Courses</button>
                                        </h5>
                                      </div>
                                      <div class="collapse " :class="active2?'':'show'" id="collapseicon2" aria-labelledby="collapseicon2" data-bs-parent="#accordion">
                                        <div class="upcoming-course card-body">
                                          <div class="media">
                                            <div class="media-body"><span class="f-w-600">UX Development</span><span class="d-block">Course By <a href="#"> Lorem ipsum</a></span><span class="d-block"><i class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i class="fa fa-star-half-o font-warning"></i></span></div>
                                            <div>
                                              <h5 class="mb-0 font-primary">18</h5><span class="d-block">Dec</span>
                                            </div>
                                          </div>
                                          <div class="media">
                                            <div class="media-body"><span class="f-w-600">Business Analyst</span><span class="d-block">Course By <a href="#">Lorem ipsum </a></span><span class="d-block"><i class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i></span></div>
                                            <div>
                                              <h5 class="mb-0 font-primary">28</h5><span class="d-block">Dec</span>
                                            </div>
                                          </div>
                                          <div class="media">
                                            <div class="media-body"><span class="f-w-600">Web Development</span><span class="d-block">Course By <a href="#">Lorem ipsum </a></span><span class="d-block"><i class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i class="fa fa-star-o font-warning"></i></span></div>
                                            <div>
                                              <h5 class="mb-0 font-primary">5</h5><span class="d-block">Jan</span>
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
                        <!-- <categories/> -->
</template>
<script>
import categories from "./categoriesPage.vue"
export default {
    components:{
        categories
    },
    methods: {
isOpen() {
  this.open = !this.open
},
showOpen() {
  this.active = !this.active
  console.log("item is,",this.active)
},
showOpen1() {
  this.active1 = !this.active1
  console.log("item is,",this.active)
},
showOpen2() {
  this.active2 = !this.active2
  console.log("item is,",this.active)
},
},
data(){
return{
 open: false,
 active:false,
 active1:false,
 active2:false,

}
}
}
</script>