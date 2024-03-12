import tags from '../../data/tags.json'
const state={
    tags: tags.data,
    activeclass : 'pills-created-tab'
}
const getters={activeclass:(state)=>{ return state.activeclass}}
const mutations={
    add:(state,payload)=>{
		state.tags.push(payload);
		
	},
    active:(state,payload)=>{
		state.activeclass = payload
	},
}
const actions={active:(context,payload)=>
	{
		context.commit('active',payload);
	},}
export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};