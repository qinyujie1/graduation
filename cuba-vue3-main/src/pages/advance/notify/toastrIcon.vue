<template>
     <div class="col-md-12 text-start">
                <div class="card">
                    <div class="card-header">
                      <h5 class="card-title">toastr with icon</h5>
                    </div>
                    <div class="card-body btn-showcase">
                      
                      <button class="btn btn-success " type="button" @click="success_with_icon" variant="success">Success</button>
                      
                      <button class="btn btn-info " type="button" @click="info_with_icon" variant="info">Info</button>

                      <button class="btn btn-danger " type="button" @click="error_with_icon" variant="danger">Error</button>

                      <button class="btn btn-info " type="button" @click="info_with_cancle" variant="info">Cancle</button>

                    </div>
                </div>
              </div>
</template>
<script>
export default {
    methods:{
         success_with_icon() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'top-right', type: 'success', icon : 'check',iconClass:"toast-custom", duration: 2000 });
      },
      info_with_icon() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'top-right', type: 'info', icon : 'info', duration: 2000 });
      },
      error_with_icon() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'top-right', icon : 'times', type: 'error', duration: 2000 });
      },
       info_with_cancle() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'bottom-right', closeOnSwipe: true, type: 'default', duration: 2000, });
      }
    }
}
</script>