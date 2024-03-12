<template>
  <Breadcrumbs main="Page Layout" title="Box Layout" />
        <!-- Container-fluid starts-->
        <div class="container-fluid">
          <div class="row">
            <div class="col-sm-12">
              <div class="card alert alert-primary " role="alert">
                <h2 class="alert-heading">Tip!</h2>
                <p>
                  Add class="box-layout" attribute to get this layout. The boxed layout is helpful when working on
                  large screens because it prevents the site from stretching very wide.
                </p>
              </div>
            </div>
            <div class="col-sm-12">
              <div class="card">
                <div class="card-header pb-0">
                  <h3>Title</h3>
                 
                  <settingPage/>
                </div>
                <div class="card-body"><span>Start creating your amazing application!</span>
                 
                </div>
                <div class="card-footer">
                  <h4 class="mb-0">Card Footer</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Container-fluid Ends-->
      
</template>
<script>
    export default{
        name: 'indexBoxed',
        mounted(){
          this.$store.dispatch('layout/setLayoutType',{class:'box-layout'})
        },
        unmounted(){
      this.$store.dispatch('layout/setLayoutType',{class:'ltr'})
    }
        
    }
</script>