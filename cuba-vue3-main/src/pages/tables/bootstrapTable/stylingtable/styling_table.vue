<template>
    <Breadcrumbs title="Styling table" main="Bootstrap Table"  />
         <div class="container-fluid">
            <div class="row">
                <tableRow1/>
                <tableRow2/>
                <tableRow3/>
                <tableCheckbox/>
                <tableRadio/>
                <tableSelect/>
                <tableInput/>
                <tableBadge/>
                <tableTooltip/>
                <tableSwitch/>

            </div>
         </div>
</template>
<script>
import tableRow1 from "./tableRow1.vue"
import tableRow2 from "./tableRow2.vue"
import tableRow3 from "./tableRow3.vue"
import tableCheckbox from "./tableCheckbox.vue"
import tableRadio from "./tableRadio.vue"
import tableSelect from "./tableSelect.vue"
import tableInput from "./tableInput.vue"
import tableBadge from "./tableBadge.vue"
import tableTooltip from "./tableTooltip.vue"
import tableSwitch from "./tableSwitch.vue"


export default {
    components:{
        tableRow1,
                tableRow2,
                tableRow3,
                tableCheckbox,
                tableRadio,
                tableSelect,
                tableInput,
                tableBadge,
                tableTooltip,
                tableSwitch,
    }
}
</script>