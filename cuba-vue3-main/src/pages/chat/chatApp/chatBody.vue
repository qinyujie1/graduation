<template>
    <div class="col call-chat-body">
          <div class="card">
            <div class="card-body p-0">
              <div class="row chat-box">
                  <div class="col pe-0 chat-right-aside">
                  <div class="chat">
                    <div class="chat-header clearfix" >
                      <img
                        class="rounded-circle"
                        v-if="currentchat.thumb"
                        :src="getImgUrl(currentchat.thumb)"
                        alt=""
                      />
                      <div class="about">
                        <div class="name">
                          {{ currentchat.name}}<span class="font-primary f-12">Typing...</span>
                        </div>
                        <div class="status digits">
                          {{ currentchat.lastSeenDate }}
                        </div>
                      </div>
                      <ul class="list-inline float-start float-sm-end chat-menu-icons">
                        <li class="list-inline-item">
                          <a href="#"><i class="icon-search"></i></a>
                        </li>
                        <li class="list-inline-item">
                          <a href="#"><i class="icon-clip"></i></a>
                        </li>
                        <li class="list-inline-item">
                          <a href="#"><i class="icon-headphone-alt"></i></a>
                        </li>
                        <li class="list-inline-item">
                          <a href="#"><i class="icon-video-camera"></i></a>
                        </li>
                        <li class="list-inline-item toogle-bar" data-bs-toggle="collapse"  data-bs-target="#collapseExample" v-on:click="chatmenutoogle = !chatmenutoogle">
                          <a href="#"><i class="icon-menu"></i></a>
                      </li>
                      </ul>
                    </div>
                    <div class="chat-history chat-msg-box custom-scrollbar" ref="chatInput" >
                      <ul>
                        <li
                          v-for="(chat, index) in currentChat.chat.messages" :key="index" v-bind:class="{ clearfix: chat.sender == 0 }" >
                          <div class="message" v-bind:class="{ 'other-message pull-right': chat.sender == 0,
                              'my-message': chat.sender != 0}">
                            <img
                              class="rounded-circle float-start chat-user-img img-30 text-end" alt=""
                              v-if="currentchat.thumb && chat.sender != 0"
                              v-bind:src="getImgUrl(currentchat.thumb)"/>
                            <img
                              class="rounded-circle float-end chat-user-img img-30"
                              alt=""
                              v-if="chat.sender == 0"
                              v-bind:src="getImgUrl('user/1.jpg')" />
                            <div
                              class="message-data text-end"
                              v-bind:class="{ 'text-start': chat.sender == 0 }" >
                              <span class="message-data-time">{{ chat.time }}</span>
                            </div>
                            
                            {{ chat.text }}
                          </div>
                        </li>
                      </ul>
                    </div>
                   <addChat @message="addChat" :chatElement='chatElement' />
                  </div>
                </div>
                <div
                  class="col ps-0 chat-menu custom-scrollbar" :class="{ show: chatmenutoogle }" id="collapseExample">
                <chatMenu/>
                </div>
              </div>
            </div>
          </div>
        </div>
</template>
<script>
 import { mapState } from 'vuex';
 import addChat from "./addChat.vue"
 import chatMenu from "./chatMenu.vue"
//  import {ref} from 'vue'
export default {
    components:{addChat,chatMenu},
    data(){
        return{
         currentchat: [],
        chatmenutoogle: false,
        
        }
    },
    computed: {
      ...mapState({
        currentChat() {
          return (this.currentchat = this.$store.getters['chat/currentChat']);
        },
      }),
    },
    methods: {
      getImgUrl(path) {
        return require('../../../assets/images/' + path);
      },
      addChat(){
        var container = this.$el.querySelector(".chat-history")
          // console.log("container", container)
          setTimeout(function () {
            container.scrollBy({ top: 200, behavior: 'smooth' });
          }, 310);
          setTimeout(function () {
            container.scrollBy({ top: 200, behavior: 'smooth' });
          }, 1100);
      }
      },
     mounted(){
      
     console.log("data",this.chatElement)
     }
  
}
</script>