<template>
    <div class="chat-message clearfix">
 
                      <div class="row">
                        <div class="col-xl-12 d-flex">
                          <div class="smiley-box bg-primary" >
                            <div class="picker">
                              <img
                                src="../../../assets/images/smiley.png"
                                alt=""
                              />
                            </div>
                          </div>
                          <div class="input-group text-box" ref="abc">
                            <input
                              class="form-control input-txt-bx"
                              id="message-to-send"
                              v-model="text"
                              v-on:keyup.enter="addChat()"
                              type="text"
                              name="message-to-send"
                              placeholder="Type a message......"
                            />
                              <button
                                @click="addChat()"
                                class="btn btn-primary input-group-text"
                                type="button"
                              >
                                SEND
                              </button>
                          </div>
                        </div>
                      </div>
                    </div>
</template>
<script>
import { mapState } from 'vuex';
// import {ref } from 'vue'
export default {
    name:'addChat',
    props:{
      chatElement:String
    },
    data(){
        return{
            text:"",
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
            addChat: function () {
              this.$emit("message")
        if (this.text !== '') {
          this.$store.dispatch('chat/addChat', this.text);
          this.text = '';
        
        }
            },
      }
}
</script>