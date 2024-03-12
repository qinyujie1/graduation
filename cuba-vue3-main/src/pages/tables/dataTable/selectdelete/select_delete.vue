<template>
  <breadCrumbs title="Select Delete" main="Data Table" title1="Select Delete" />
  <div class="container-fluid text-start">
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-header">
            <h5>Zero Configuration</h5>
            <span>DataTables has most features enabled by default, so all you need to do to use it with your own tables is to call the construction function:<code>$().DataTable();</code>.</span><span>Searching, ordering and paging goodness will be immediately added to the table, as shown in this example.</span >
          </div>
          <div class="card-body">
           <div class="table-responsive">
            <div id="basic-1_wrapper" class="dataTables_wrapper no-footer">
            <div class="dataTables_length" id="basic-1_length">
              <label>Show
                <select name="basic-1_length" aria-controls="basic-1" class="" v-model="perPage" >
                  <option v-for="option in pageOptions" :key="option" :options="pageOptions"> {{ option }}</option>
                </select>
                entries</label>
            </div>
            <table class="display dataTable" id="basic-1">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Position</th>
                  <th>Office</th>
                  <th>Age</th>
                  <th>Start date</th>
                  <th>Salary</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="row in get_rows()" :key="row">
                  <td>{{ row.name }}</td>
                  <td>{{ row.position }}</td>
                  <td>{{ row.office }}</td>
                  <td>{{ row.age }}</td>
                  <td>{{ row.startdate }}</td>
                  <td>{{ row.salary }}</td>
                </tr>
              </tbody>
            </table>
            <ul class="pagination">
              <li class="page-item">
                <a class="page-link" href="#" aria-label="Previous">
                  <span aria-hidden="true">&laquo;</span>
                </a>
              </li>
              <li class="page-item" v-for="i in num_pages()" :key="i" v-bind:class="[i == currentPage ? 'active' : '']" v-on:click="change_page(i)" >
                <a class="page-link">{{ i }}</a>
              </li>
              <li class="page-item">
                <a class="page-link" href="#" aria-label="Next">
                  <span aria-hidden="true">&raquo;</span>
                </a>
              </li>
            </ul>
          </div>
        </div>
        </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
       elementsPerPage: 10,
         currentPage: 1,
          ascending: false,
          sortColumn: '',
           perPage: 10,
          pageOptions: [ 10, 25,50,100],
           filter: null,
    };
  },
   computed: {
    ...mapState({
      tableItems:(state)=>state.table.items,    
    }),
   columns() {
      if (this.tableItems.length == 0) {
        return [];
      }
      return Object.keys(this.tableItems[0])
    }
   },
  methods:{
      num_pages() {
      return Math.ceil(this.tableItems.length / this.elementsPerPage);
    },
     change_page(page) {
      this.currentPage = page;
    },
     get_rows() {
      var start = (this.currentPage-1) * this.elementsPerPage;
      var end = start + this.elementsPerPage;
      return this.tableItems.slice(start, end);
    },
  }
};
</script>