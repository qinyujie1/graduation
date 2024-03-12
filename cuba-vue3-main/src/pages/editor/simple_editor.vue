<template>
    <div>
        <Breadcrumbs main="Editor" title="Simple Editor"/>
        <!-- Container-fluid starts-->
        <div class="container-fluid">
            <div class="row">
              <div class="col-md-12">
                <div class="card">
                    <div class="card-header">
                      <h5 class="card-title">Simple Editor</h5>
                    </div>
                    <div class="card-body">
                      <quill-editor
                      v-model:value="state.content"
                      :options="state.editorOption"
                      @blur="onEditorBlur($event)"
                      @focus="onEditorFocus($event)"
                      @ready="onEditorReady($event)"
                      @change="onEditorChange($event)"
                    />                    </div>
                </div>
              </div>

            </div>
        </div>
        <!-- Container-fluid Ends-->
    </div>
</template>

<script>
 import { reactive } from 'vue'
export default {
    setup() {
    const state = reactive({
      content: '<h1>Some initial content</h1>',
      _content: '',
      editorOption: {
        placeholder: 'core',
      },
      disabled: false
    })

    const onEditorBlur = (quill) => {
      console.log('editor blur!', quill)
    }
    const onEditorFocus = (quill) => {
      console.log('editor focus!', quill)
    }
    const onEditorReady = (quill) => {
      console.log('editor ready!', quill)
    }
    const onEditorChange = ({ quill, html, text }) => {
      console.log('editor change!', quill, html, text)
      state._content = html
    }

    setTimeout(() => {
      state.disabled = true
    }, 2000)

    return { state, onEditorBlur, onEditorFocus, onEditorReady, onEditorChange }
  },
};
</script>