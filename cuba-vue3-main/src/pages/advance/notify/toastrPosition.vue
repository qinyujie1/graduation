<template>
    <div class="col-md-12 text-start">
                <div class="card">
                    <div class="card-header">
                      <h5 class="card-title">toastr with position</h5>
                    </div>
                    <div class="card-body btn-showcase">
                      
                      <button class="btn btn-primary" type="button" @click="top_right" variant="primary">Top Right</button>

                      <button class="btn btn-primary" type="button" @click="top_left" variant="primary">Top Left</button>

                      <button class="btn btn-primary" type="button" @click="top_center" variant="primary">Top Center</button>

                      <button class="btn btn-primary" type="button" @click="bottom_right" variant="primary">Bottom Right</button>

                      <button class="btn btn-primary" type="button" @click="bottom_left" variant="primary">Bottom Left</button>

                      <button class="btn btn-primary" type="button" @click="bottom_center" variant="primary">Bottom Center</button>

                      <button class="btn btn-primary" type="button" @click="full_width" variant="primary">Full Width</button>

                    </div>
                </div>
              </div>
</template>
<script>
export default {
    methods:{
full_width() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'top-right', fullWidth:true, type: 'success', duration: 2000 });
      },
      top_right() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'top-right', type: 'success', duration: 2000 });
      },
      top_left() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'top-left', type: 'success', duration: 2000 });
      },
       top_center() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'top', type: 'success', duration: 2000 });
      },
       bottom_right() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'bottom-right', type: 'success', duration: 2000 });
      },
       bottom_left() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'bottom-left', type: 'success', duration: 2000 });
      },
       bottom_center() {
        this.$toast.show(' New order has been placed ', { theme: 'outline',position: 'bottom', type: 'success', duration: 2000 });
      },
    }
}
</script>