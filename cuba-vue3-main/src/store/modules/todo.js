import todo from "../../data/todo.json"

const state = {
    todo : todo.data
};

const mutations = {
    taskcomplete:(state,payload)=>{
        state.todo.find(function (list) {
            if (list.id === payload) {
                return list.status = list.status === 'complete' ? 'incomplete' : 'complete';
            }
        });
    },
    alltaskcomplete:(state,payload)=>{
       state.todo.filter(function (list) {
               return list.status = payload === true ? 'complete':'incomplete';
        });
    },
    tododelete:(state,payload)=>{
        state.todo = state.todo.filter(list => list.id !== payload);
    },
    addtodo:(state,payload)=>{
        let id = state.todo.slice(-1)[0].id+1;
         state.todo.push(
            {
                'id': id,
                'title': payload,
                'priority':"Pending",
                'date':"16 Jan",
                'badgeClass':"badge-light-danger",
                'delete': false,
                'status': 'incomplete'
            }
        );
    }
};
export default {
	namespaced: true,
	state,
	mutations
};