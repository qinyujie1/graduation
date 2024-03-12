<template>
    <button class="btn-primary badge-light d-block btn-mail w-100" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal">
             <vue-feather class="me-2" type="check-circle"></vue-feather> To Do List
    </button>
    <div class="modal fade modal-bookmark" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                               <div class="modal-dialog modal-lg" role="document">
                                 <div class="modal-content">
                                   <div class="modal-header">
                                     <h5 class="modal-title" id="exampleModalLabel">Add To-Do</h5>
                                     <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
                                   </div>
                                   <div class="modal-body">
                                     <form class="form-bookmark needs-validation" id="bookmark-form" novalidate="">
                                         <div class="form-row">
                                       <div class="new-task-wrapper " :class="{'visible':addtask}" >
                           <textarea class="form-control" v-on:keyup.enter="addnewtask" v-model="task" autocomplete="off" id="new-task" placeholder="Enter new task here. . ." ></textarea>
                                       </div>
                           <span @click='addtask = false'  class="btn btn-danger cancel-btn mt-2" id="close-task-panel" data-bs-dismiss="modal" >Close</span>
                           <span @click="addnewtask()" data-bs-dismiss="modal" class="btn btn-success ms-3 add-new-task-btn mt-2" id="add-task">Add Task</span>
                         </div>
                                     </form>
                                   </div>
                                 </div>
                               </div>
                             </div>
</template>
<script>
import { mapState } from 'vuex';
export default {
  data(){
      return{
      addtask :false,
      }
  },
  computed: {
   ...mapState({
     todolist: state => state.todo.todo,
   })
 },
  methods:{
        addnewtask() {
     if(this.task !== '') {
       this.$store.dispatch('todo/addtodo', this.task);
       this.task = '';
       this.addtask = false;
       this.$toast.show('Task list is updated.',{ theme:'outline',position: 'top-right', type : 'success',duration:2000 });
     }
   },
  
  }
}
</script>