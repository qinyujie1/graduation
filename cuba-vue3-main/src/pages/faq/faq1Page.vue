<template>
  <div class="col-lg-12 ">
              <div class="header-faq">
                <h5 class="mb-0">Quick Questions are answered</h5>
              </div>
              <div class="row default-according style-1 faq-accordion" id="accordionoc">
                <div class="col-xl-8 xl-60 col-lg-6 col-md-7">
                  <div class="card">
                    <div class="card-header">
                      <h5 class="mb-0">
                        <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon" aria-expanded="false" aria-controls="collapseicon" :class="[isActive ? 'active' : '', 'collapsible']" v-on:click="toggle"><vue-feather type="help-circle"></vue-feather> Integrating WordPress with Your Website?</button>
                      </h5>
                    </div>
                    <div class="collapse" id="collapseicon" aria-labelledby="collapseicon" data-parent="#accordionoc" :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
                      <div class="card-body"><p>{{lorem}}</p></div>
                    </div>
                  </div>
                  <div class="card">
                    <div class="card-header">
                      <h5 class="mb-0">
                        <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon2" aria-expanded="false" aria-controls="collapseicon2" :class="[isActive ? 'active' : '', 'collapsible']" v-on:click="toggle"><vue-feather type="help-circle"></vue-feather> WordPress Site Maintenance ?</button>
                      </h5>
                    </div>
                    <div class="collapse" id="collapseicon2" data-parent="#accordionoc" :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
                      <div class="card-body"><p>{{lorem}}</p></div>
                    </div>
                  </div>
                  <div class="card">
                    <div class="card-header">
                      <h5 class="mb-0">
                        <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon3" aria-expanded="false" aria-controls="collapseicon2" :class="[isActive ? 'active' : '', 'collapsible']" v-on:click="toggle"><vue-feather type="help-circle"></vue-feather>Meta Tags in WordPress ?</button>
                      </h5>
                    </div>
                    <div class="collapse" id="collapseicon3" data-parent="#accordionoc" :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
                      <div class="card-body"><p>{{lorem}}</p></div>
                    </div>
                  </div>
                  <div class="card">
                    <div class="card-header">
                      <h5 class="mb-0">
                        <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon4" aria-expanded="false" aria-controls="collapseicon2" :class="[isActive ? 'active' : '', 'collapsible']" v-on:click="toggle"><vue-feather type="help-circle"></vue-feather>   WordPress in Your Language ?</button>
                      </h5>
                    </div>
                    <div class="collapse" id="collapseicon4" data-parent="#accordionoc" :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
                      <div class="card-body"><p>{{lorem}}</p></div>
                    </div>
                  </div>
                  <div class="faq-title"> <h6>Intellectual Property</h6> </div>
                  <div class="card">
                    <div class="card-header">
                      <h5 class="mb-0">
                        <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon5" aria-expanded="false" :class="[isActive ? 'active' : '', 'collapsible']" v-on:click="toggle"><vue-feather type="help-circle"></vue-feather> WordPress Site Maintenance ?</button>
                      </h5>
                    </div>
                    <div class="collapse" id="collapseicon5" aria-labelledby="collapseicon5" data-parent="#accordionoc" :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
                      <div class="card-body"><p>{{lorem}}</p>
                      </div>
                    </div>
                  </div>
                  <div class="card">
                    <div class="card-header">
                      <h5 class="mb-0">
                        <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon7" aria-expanded="false" aria-controls="collapseicon2" :class="[isActive ? 'active' : '', 'collapsible']" v-on:click="toggle"><vue-feather type="help-circle"></vue-feather>  WordPress in Your Language ?</button>
                      </h5>
                    </div>
                    <div class="collapse" id="collapseicon7" data-parent="#accordionoc" :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
                      <div class="card-body"><p>{{lorem}}</p>
                      </div>
                    </div>
                  </div>
                  <div class="card">
                    <div class="card-header">
                      <h5 class="mb-0">
                        <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon8" aria-expanded="false" aria-controls="collapseicon2" :class="[isActive ? 'active' : '', 'collapsible']" v-on:click="toggle"><vue-feather type="help-circle"></vue-feather>Integrating WordPress with Your Website ?</button>
                      </h5>
                    </div>
                    <div class="collapse" id="collapseicon8" data-parent="#accordionoc" :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
                      <div class="card-body"><p>{{lorem}}</p>
                      </div>
                    </div>
                  </div>
                 <faq2/>
                </div>
                <navigation/>
              </div>
  </div>
</template>
<script>
import faq2 from "./faq2Page.vue"
import navigation from "./navigationPage.vue"
export default {
components:{faq2,navigation},
data(){
return{
 isActive: false,
   lorem:"Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
}
},
methods: {
toggle() {
  this.isActive = !this.isActive
},
}
}
</script>