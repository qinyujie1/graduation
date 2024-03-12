<template>
<div class="col call-chat-sidebar">
    <div class="card">
        <div class="card-body chat-body">
            <div class="chat-box">
                <div class="chat-left-aside">
                    <div class="d-flex"><img class="rounded-circle user-image" src="@/assets/images/user/12.png" alt="">
                        <div class="flex-grow-1">
                            <div class="about"><a class="name f-w-600" href="user-profile.html">Mark Jecno</a>
                                <div class="status">Status...</div>
                            </div>
                        </div>
                    </div>
                    <div class="people-list" id="people-list">
                        <div class="search">
                            <form class="theme-form">
                                <div class="form-group">
                                    <div class="input-group">
                                        <input v-model="search" v-on:keyup="setSerchUsers" class="form-control" type="text" placeholder="search" /><span class="input-group-text"><i class="fa fa-search"></i></span>
                                    </div>
                                </div>
                            </form>
                        </div>
                        <ul class="list" v-if="search == ''">
                            <li class="clearfix" v-for="(user, index) in activeusers" :key="index" @click="setActiveuser(user.id)">
                                <img class="rounded-circle user-image" :src="getImgUrl(user.thumb)" alt="" />
                                <div class="status-circle away"></div>
                                <div class="about">
                                    <div class="name">{{ user.name }}</div>
                                    <div class="status">{{ user.status }}</div>
                                </div>
                            </li>
                        </ul>
                        <ul class="list" v-if="search != ''">
                            <li class="clearfix" v-for="(user, index) in serchUser" :key="index" @click="setActiveuserSerch(user.id)">
                                <img class="rounded-circle user-image" :src="getImgUrl(user.thumb)" alt="" />
                                <div class="status-circle away"></div>
                                <div class="about">
                                    <div class="name">{{ user.name }}</div>
                                    <div class="status">{{ user.status }}</div>
                                </div>
                            </li>
                            <div v-if="!serchUser.length">
                                <div class="search-not-found chat-search text-center">
                                    <p> Sorry, We didn't find any results matching this search </p>
                                </div>
                            </div>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import {
    mapState
} from 'vuex';
export default {
    name: 'searchChat',
    components: {},
    data() {
        return {
            text: '',
            search: '',
        };
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
            chats: (state) =>
                state.chat.chats.find(function (chat) {
                    if (chat.id === state.chat.activeuser) {
                        return chat;
                    }
                }),
        }),
    },
    methods: {
        getImgUrl(path) {
            return require('../../../assets/images/' + path);
        },
        setActiveuser: function (id) {
            this.$store.dispatch('chat/setActiveuser', id);
        },
        setActiveuserSerch: function (id) {
            this.$store.dispatch('chat/setActiveuser', id);
            this.search = '';
        },
        setSerchUsers: function () {
            if (this.search !== '')
                this.$store.dispatch('chat/setSerchUsers', this.search);
        },
    },
};
</script>
