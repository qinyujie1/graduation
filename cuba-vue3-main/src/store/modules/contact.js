//import data from '../../data/contact.json'
const state={
    display:true,
    activeTab: '0',
    selectedUser: ''
};
const mutations={
    change:(state)=>{
    state.display = !state.display 
    },
   
    active:(state,payload)=>
    {
    state.activeTab = payload 
   
    },
    print:(state,payload)=>
    {
    state.selectedUser = payload 
   
    },
};
const getters={
    display:(state)=>{return state.display},
    activeTab:(state)=>{return state.activeTab},
    selectedUser:(state)=>{return state.selectedUser}
};
const actions={
    change:(context)=>
	{
	context.commit('change');
	},
    active:(context,payload)=>
	{
	context.commit('active',payload);
	},
};
export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};