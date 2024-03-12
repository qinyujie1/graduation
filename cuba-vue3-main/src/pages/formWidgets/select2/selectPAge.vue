<template>
  <div class="col-md-12">
    <div class="card">
      <div class="card-header pb-0">
        <h5 class="card-title">Select-2</h5>
      </div>
      <div class="card-body">
        <div class="mb-2">
          <label class="col-form-label">Default Placeholder</label>
          <Multiselect v-model="multiValue" :options="options" mode="tags"/>
        </div>
        <div class="mb-2"  >
          <label class="col-form-label">Select2 single select</label>
          <Multiselect v-model="multiValue1" :options="optionslist"/>        </div>
        <div class="mb-2">
           <label class="col-form-label">Select2 multi select</label>
           <Multiselect v-model="multiValue2" :options="options" mode="tags"/>        </div>
        <div class="mb-2">
          <label class="col-form-label">RTL support</label>
          <Multiselect v-model="multiValue3" :options="options" mode="tags"/>        </div>
        <div class="mb-2">
           <label class="col-form-label">Limiting The Number Of Selections</label>
           <Multiselect v-model="multiValue4" :options="options" mode="tags"/>        </div>
       
      </div>
      <div class="mb-2">
        <div class="col-form-label">Disabled Results</div>
        <select class="js-example-disabled-results col-sm-12">
          <option value="one">First</option>
          <option value="two" disabled="disabled">
            Second
            (disabled)
          </option>
          <option value="three">Third</option>
        </select>
      </div>
      <div class="mb-2">
        <div class="col-form-label">Hiding The Search Box</div>
        <select class="js-example-basic-hide-search col-sm-12" multiple="multiple">
          <optgroup label="Developer">
            <option value="AL">Smith</option>
            <option value="WY">Peter</option>
            <option value="WY">James</option>
            <option value="WY">Hanry Die</option>
            <option value="WY">John Doe</option>
            <option value="WY">Harry Poter</option>
          </optgroup>
        </select>
      </div>
      <div>
        <div class="col-form-label">Enable-Disable</div>
        <select class="js-example-disabled col-sm-10">
          <option value="AL">Smith</option>
          <option value="WY">Peter</option>
          <option value="WY">James</option>
          <option value="WY">Hanry Die</option>
          <option value="WY">John Doe</option>
          <option value="WY">Harry Poter</option>
        </select>
        <div class="text-end mt-2">
          <button class="btn btn-primary js-programmatic-enable mt-2">Enable</button>
          <button class="btn btn-danger js-programmatic-disable mt-2">Disable</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
// import disabled from "./disabledPage.vue"
import Multiselect from '@vueform/multiselect'
export default {
  components:{
  //  disabled,
  Multiselect
  },
  data() {
      return {
         multiValue: null,
         multiValue1:null,
         multiValue2:null,
         multiValue3:null,
        options: [
           'Alabama' ,
           'Wyoming' ,
           'Coming' ,
           'Hanry Die', 
           'John Doe' 
        ],
         optionslist: [
          { code: 1, name: 'Alabama' },
          { code: 2, name: 'Wyoming' },
          { code: 3, name: 'Coming' },
          { code: 4, name: 'Hanry Die' },
          { code: 5, name: 'John Doe' }
        ],
         options3: [
          { code: 1, name: 'Alabama' },
          { code: 2, name: 'Wyoming' },
          { code: 3, name: 'Coming' },
          { code: 4, name: 'Hanry Die' },
          { code: 5, name: 'John Doe' }
        ],
        options1: [
        {
          language: 'Developer',
          libs: [
            { name: 'Alabama', category: 'Front-end' },
            { name: 'Wyoming', category: 'Backend' }
          ]
        },
        {
          language: 'Designer',
          libs: [
            { name: 'Peter', category: 'Backend' },
            { name: 'Hanry Die', category: 'Backend' },
            { name: 'John Doe', category: 'Backend' }
          ]
        },

      ],
      value: [{ name: 'Alabama', category: 'Front-end' },]
      }
    }
};
</script>
<style src="@vueform/multiselect/themes/default.css"></style>
