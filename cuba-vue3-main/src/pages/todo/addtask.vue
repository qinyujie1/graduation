<template>
    <div class="card">
                 <div class="card-header"><h3 class="mb-0">To-Do</h3></div>
                <div class="card-body pt-0">
                  <div class="todo">
                    <div class="todo-list-wrapper">
                      <div class="todo-list-container">
                           <div class="mark-all-tasks">
                          <div @click="alltaskcomplete()" class="mark-all-tasks-container">
                            <span class="mark-all-btn" :class="{'move-down':!markallread}"  id="mark-all-finished" role="button">
                              <span class="btn-label">Mark all as finished</span>
                              <span class="action-box completed"><i class="icon"><i class="icon-check"></i></i></span>
                            </span>
                            <span class="mark-all-btn " :class="{'move-down':markallread}" id="mark-all-incomplete" role="button">
                              <span class="btn-label">Mark all as Incomplete</span>
                              <span class="action-box"> <i class="icon"><i class="icon-check"></i></i></span>
                            </span>
                          </div>
                           <div class="todo-list-footer ms-2">
                              <div class="add-task-btn-wrapper">
                              <span class="add-task-btn"><button  @click='addtask =! addtask' class="btn btn-primary" :class="{'d-none':addtask}"><i class="icon-plus"></i> Add new task</button></span>
                              </div>
                           </div>
                        </div>
                        <div class="todo-list-body">
                          <ul id="todo-list">
                            <li  v-for="(todo,index) in todolist" :key="index" class="task" :class="{'completed':todo.status == 'complete' }">
                              <div class="task-container">
                                <h4 class="task-label "> {{todo.title}} </h4>
                                <div class="d-flex align-items-center gap-4"><span class="badge " :class="todo.badgeClass">{{todo.priority}}</span>
                                  <h5 class="assign-name m-0">{{todo.date}}</h5>
                                   <span class="task-action-btn">
                                    <span @click="tododelete(todo.id)" class="action-box large delete-btn" title="Delete Task"><i class="icon"><i class="icon-trash"></i></i></span>
                                   <span @click="taskcomplete(todo.id,todo.status)" class="action-box large complete-btn" title="Mark Complete"><i class="icon"><i class="icon-check"></i></i></span>
                                </span>
                                </div>  
                              </div>
                            </li>
                          </ul>
                        </div>
                      <div class="todo-list-footer">
                           <div class="new-task-wrapper " :class="{'visible':addtask}">
                            <textarea v-on:keyup.enter="addnewtask" v-model="task" id="new-task" placeholder="Enter new task here. . ."></textarea>
                            <span @click='addtask = false'  class="btn btn-danger cancel-btn" id="close-task-panel">Close</span>
                            <span @click="addnewtask()" class="btn btn-success ms-3 add-new-task-btn" id="add-task">Add Task</span>
                          </div>
                      </div>
                      </div>
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
       markallread :true,
       task:'',
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
        this.$store.commit('todo/addtodo', this.task);
        this.task = '';
        this.addtask = false;
        this.$toast.show('Task list is updated.',{ theme:'outline',position: 'top-right', type : 'success',duration:2000 });
      }
    },
    alltaskcomplete() {
      this.$store.commit('todo/alltaskcomplete',this.markallread);
      this.markallread =! this.markallread;
      if(this.markallread)
        this.$toast.show('All tasks marked as Incomplete.',{ theme:'outline',position: 'top-right', type : 'error',duration:2000 });
      else
        this.$toast.show('All tasks marked as complete.',{ theme:'outline',position: 'top-right', type : 'success',duration:2000 });
    },
    tododelete(id) {
      this.$store.commit('todo/tododelete', id);
      this.$toast.show('Task has been deleted.',{ theme:'outline',position: 'top-right', type : 'success',duration:2000 });
    },
     taskcomplete(id,status) {
      this.$store.commit('todo/taskcomplete', id);
      if(status !== 'complete')
        this.$toast.show(' tasks marked as complete.', { theme: 'outline',position: 'top-right', type: 'success', duration: 2000 });
      else
        this.$toast.show(' tasks marked as incomplete.', { theme: 'outline',position: 'top-right', type: 'error', duration: 2000 });
    },
   },
  
}
</script>