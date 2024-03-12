<template>
            <div class="col-sm-12">
            <ul
              class="nav nav-tabs border-tab mb-0"
              id="top-tab"
              role="tablist"
            >
              <li class="nav-item" @click="tabContent('call')">
                <a
                  class="nav-link"
                  id="top-home-tab"
                  data-toggle="tab"
                  role="tab"
                  aria-controls="top-home"
                  aria-selected="false"
                  :class="[{ active: activeTab == 'call' }]"
                  >CALL</a
                >
                <div class="material-border"></div>
              </li>
              <li class="nav-item" @click="tabContent('status')">
                <a
                  class="nav-link"
                  id="profile-top-tab"
                  data-toggle="tab"
                  role="tab"
                  aria-controls="top-profile"
                  aria-selected="false"
                   :class="[{ active: activeTab == 'status'}]"
                  >STATUS</a
                >
                <div class="material-border"></div>
              </li>
              <li class="nav-item" @click="tabContent('profile')">
                <a
                  class="nav-link"
                  id="contact-top-tab"
                  data-toggle="tab"
                  role="tab"
                  aria-controls="top-contact"
                  aria-selected="true"
                  :class="[{ active: activeTab == 'profile' }]"
                  >PROFILE</a
                >
                <div class="material-border"></div>
              </li>
            </ul>
            <div class="tab-content custom-scrollbar" id="top-tabContent">
              <div
                class="tab-pane fade"
                :class="{ 'show active': activeTab == 'call' }"
                id="top-home"
                role="tabpanel"
                aria-labelledby="top-home-tab"
              >
                <div class="people-list">
                        <ul class="list digits custom-scrollbar">
                          <li
                            class="clearfix"
                            v-for="(user, index) in users"
                            :key="index"
                            @click="setActiveuser(user.id)"
                          >
                            <img
                              class="rounded-circle user-image"
                              :src="getImgUrl(user.thumb)"
                              alt=""
                            />
                            <div class="about">
                              <div class="name">{{ user.name }}</div>
                              <div class="status">
                                <i class="fa fa-share font-success me-1"></i
                                >{{ user.lastSeenDate }}
                              </div>
                            </div>
                          </li>
                        </ul>
              </div>
              </div>
              <div
                class="tab-pane fade"
                :class="{ 'show active': activeTab == 'status' }"
                id="top-profile"
                role="tabpanel"
                aria-labelledby="profile-top-tab"
              >
               <div class="people-list">
                          <div class="search">
                            <form class="theme-form">
                              <div class="form-group">
                                <input
                                  class="form-control"
                                  type="text"
                                  placeholder="Write Status...00"
                                /><i class="fa fa-pencil"></i>
                              </div>
                            </form>
                          </div>
                        </div>
                        <div class="status">
                          <p class="font-primary f-w-600">Active</p>
                          <hr />
                          <p>
                            Established fact that a reader will be distracted
                            <i
                              class="icofont icofont-emo-heart-eyes font-danger f-20"
                            ></i
                            ><i
                              class="icofont icofont-emo-heart-eyes font-danger f-20 m-l-5"
                            ></i>
                          </p>
                          <hr />
                          <p>
                            Dolore magna aliqua
                            <i
                              class="icofont icofont-emo-rolling-eyes font-success f-20"
                            ></i>
                          </p>
                        </div>
              </div>
              <div
                class="tab-pane fade"
                id="top-contact"
                role="tabpanel"
                :class="{ 'show active': activeTab == 'profile' }"
                aria-labelledby="contact-top-tab"
              >
               <div class="user-profile">
                          <div class="image">
                            <div class="avatar text-center">
                              <img
                                alt=""
                                src="../../../assets/images/user/2.png"
                              />
                            </div>
                            <div class="icon-wrapper">
                              <i class="icofont icofont-pencil-alt-5"></i>
                            </div>
                          </div>
                          <div class="user-content text-center">
                            <h5 class="text-uppercase">Elana Jecno</h5>
                            <div class="social-list">
                                  <ul>
                                    <li><a href="javascript:void(0)"><i class="fa fa-facebook"></i></a></li>
                                     <li ><a href="javascript:void(0)"><i class="fa fa-google-plus"></i></a></li>
                                    <li><a href="javascript:void(0)"><i class="fa fa-twitter"></i></a></li>
                                    <li><a href="javascript:void(0)"><i class="fa fa-instagram"></i></a></li>
                                    <li><a href="javascript:void(0)"><i class="fa fa-rss"></i></a></li>
                                  </ul>
                                </div>
                            <div class="follow text-center">
                              <div class="row">
                                <div class="col border-right">
                                  <span>Following</span>
                                  <div class="follow-num">236k</div>
                                </div>
                                <div class="col">
                                  <span>Follower</span>
                                  <div class="follow-num">3691k</div>
                                </div>
                              </div>
                            </div>
                            <div class="text-center digits">
                              <p class="mb-0">Mark.jecno23@gmail.com</p>
                              <p class="mb-0">+91 365 - 658 - 1236</p>
                              <p class="mb-0">Fax: 123-4560</p>
                            </div>
                          </div>
                        </div>
              </div>
            </div>
          </div>  
</template>
<script>
// import VueFeather from "vue-feather";
 import { mapState } from 'vuex';
//  import addChat from "./addChat.vue"
export default {
    // components:{addChat,},
    data(){
        return{
         currentchat: [],
        chatmenutoogle: false,
        activeTab: 'call',
        }
    },
    computed: {
      ...mapState({
           activeuser: (state) => state.chat.activeuser,
        users: (state) =>
          state.chat.users.filter(function (user) {
            if (user.id !== 0) return user;
          }),
       serchUser: (state) => state.chat.serchUser,
       activeusers: (state) =>
          state.chat.users.filter(function (user) {
            if (user.active === 'active' && user.id !== 0) return user;
          }),
        currentChat() {
          return (this.currentchat = this.$store.getters['chat/currentChat']);
        },
      }),
    },
    
    methods: {
      getImgUrl(path) {
        return require('../../../assets/images/' + path);
      },
       tabContent(val) {
        this.activeTab = val;
      },
        setActiveuser: function (id) {
        this.$store.dispatch('chat/setActiveuser', id);
      },
      }
}
</script>