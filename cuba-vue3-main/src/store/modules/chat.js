import users from '../../data/chatmember.json';

const state = {
    all: users.data,
    users: users.data,
    serchUser: users.data,
    chats: users.chat,
    activeuser:1,

};

const getters = {currentChat: (state) => {
    var chats = state.chats.find( chat => {
        if(chat.id === state.activeuser)
            return chat;
    });
    var users = state.users.find( user => {
        if(user.id === state.activeuser)
            return user;
    });
    return { ...users,'chat':chats };
},

};
const mutations = {
    addChat: (state, payload) => {
        var today = new Date().toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
        const id = state.activeuser;
        const addchat = state.chats.find(chat => chat.id === id);
        addchat.messages.push({ 'sender': 0, 'time': today.toLowerCase(), 'text': payload });
    },
    addChatResponce: (state) => {
        var today = new Date().toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
        const id = state.activeuser;
        const addchat = state.chats.find(chat => chat.id === id);
        addchat.messages.push({ 'sender': id , 'time': today.toLowerCase(), 'text': '... I will text you later.' });
    },
    setActiveuser: (state, payload) => {

        state.activeuser = payload;

        const chats = state.chats.find( chat => {
            if(chat.id === payload)
                return chat;
        });
        if(!chats) {
            state.users.find( user => {
                if(user.id === payload) {
                    user.active = 'active';
                }
            });
            state.chats.push({
                'id': payload,
                'users': [
                    0,
                    payload
                ],
                'lastMessageTime': 'Last seen yesterday 14:14',
                'messages': [],
                "video":[]
            });
        }
    },
     setSerchUsers: (state, payload) => {
        state.serchUser = state.all.filter(function (search) {
            if (search.name.toLowerCase().search(payload.toLowerCase()) !== -1 && search.id !== 0)
                return search;
        });
    }
};
const actions = {
    addChat: (context, payload) => {
        context.commit('addChat', payload);
    setTimeout(function () {
        context.commit('addChatResponce');
    },1000);


},
    setActiveuser: (context, payload) => {
        context.commit('setActiveuser',payload);
     },
     setSerchUsers:(context, payload) => {
        context.commit('setSerchUsers',payload);
    }
};
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};