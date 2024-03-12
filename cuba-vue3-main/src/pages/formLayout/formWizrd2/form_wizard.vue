<template>
    <Breadcrumbs title="Form Wizard" main="Form Layout"  />
          <div class="container-fluid text-start">
            <div class="row">
                <SimpleWizard/>
            </div>
          </div>
</template>
<script>
import SimpleWizard from "./SimpleWizard.vue"
export default {
    components:{
        SimpleWizard
    }
}
</script>