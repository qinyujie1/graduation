<template>
    <Breadcrumbs title="Basic table" main="Bootstrap Table" />
    <div class="container-fluid basic_table">
            <div class="row">
            <basicTable/>
            <inverseTable/>
            <hoverableRows/>
            <backgroundUtilities/>
            <tableHead/>
            <stripedRow/>
            <!-- <captionTable/>
            <responsiveTables/>
            <breckpointSpecific/> -->
            </div>
            </div>
</template>
<script>
import basicTable from "./basicTable.vue"
import inverseTable from "./inverseTable.vue"
import hoverableRows from "./hoverableRows.vue"
import backgroundUtilities from "./backgroundUtilities.vue"
import tableHead from "./tableHead.vue"
import stripedRow from "./stripedRow.vue"
// import captionTable from "./captionTable.vue"
// import responsiveTables from "./responsiveTables.vue"
// import breckpointSpecific from "./breckpointSpecific.vue"
export default {
    components:{
        basicTable,
        inverseTable,
        hoverableRows,
        backgroundUtilities,
        tableHead,
        stripedRow,
        // captionTable,
        // responsiveTables,
        // breckpointSpecific
    }
}
</script>