<template>
    <Breadcrumbs main="Tables" title="VueJs Smart Table"/>
    <div class="container-fluid text-start">
			<div class="row">
             <basic/>
             <filterView/>
             <agefilter/>
             <rowSelect/>
            </div>
    </div>
</template>
<script>
import basic from "./basicSmart.vue"
import filterView from "./filterView.vue"
import agefilter from "./ageFilter.vue"
import rowSelect from "./rowSelect.vue"
export default {
    components:{
        basic,
        filterView,
        agefilter,
        rowSelect
    }
}
</script>