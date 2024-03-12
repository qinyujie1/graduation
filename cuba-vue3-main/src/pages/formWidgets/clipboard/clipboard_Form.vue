<template>
   <Breadcrumbs main="Form Widgets" title="clipboard"/>
      <div class="container-fluid">
            <div class="row">
                <clipboardTextInput/>
                <clipboardTextarea/>
                <cipboardParagraph/>
                <copyPortion/>
            </div>
      </div>
</template>
<script>
import clipboardTextInput from "./clipboardTextInput.vue"
import clipboardTextarea from "./clipboardTextarea.vue"
import cipboardParagraph from "./cipboardParagraph.vue"
import copyPortion from "./copyPortion.vue"
export default {
    components:{
        clipboardTextInput,
        clipboardTextarea,
        cipboardParagraph,
        copyPortion
    }
}
</script>