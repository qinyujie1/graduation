<template>
     <Breadcrumbs main="Data tables" title="Filter"/>
      <div class="container-fluid text-start">
            <div class="row">
              <div class="col-md-12">
                <div class="card">
                    <div class="card-header">
                      <h5>Zero Configuration</h5><span>DataTables has most features enabled by default, so all you need to do to use it with your own tables is to call the construction function:<code>$().DataTable();</code>.</span><span>Searching, ordering and paging goodness will be immediately added to the table, as shown in this example.</span>
                    </div>

                    <div class="card-body">
                    <div class="table-responsive">
                             <div id="basic-1_wrapper" class="dataTables_wrapper no-footer">
                           <datatable/>
                             </div>
                        </div>
                    </div>
                </div>
              </div>
            </div>
      </div>
</template>
<script>
import datatable from "../datatablePage.vue"
export default {
    components:{
        datatable
    }
}
</script>