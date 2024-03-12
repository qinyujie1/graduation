<template>
<div class="form-builder">
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-12">
                <div class="card">
                    <div class="card-header">
                        <h5>Drag & Drop components</h5><span>Copy the html code from View HTML tab </span>
                    </div>
                    <div class="card-body">
                        <div class="row clearfix form-builder">
                            <div class="col-lg-12 col-xl-6">
                                <div class="form-builder-header-1">
                                    <ul class="nav nav-primary" id="formtabs">
                                        <li class="nav-item"><a data-bs-toggle="tab" class="nav-link m-r-5 active" data-bs-target="#input">Input</a></li>
                                        <li class="nav-item"><a data-bs-toggle="tab" class="nav-link m-r-5" data-bs-target="#radio">Radios / Checkboxes</a></li>
                                        <li class="nav-item"><a data-bs-toggle="tab" class="nav-link m-r-5" data-bs-target="#select">Select</a></li>
                                        <li class="nav-item"><a data-bs-toggle="tab" class="nav-link m-r-5" data-bs-target="#buttons">Buttons</a></li>
                                        <li class="nav-item"><a data-bs-toggle="tab" class="nav-link m-r-5" data-bs-target="#view">View HTML</a></li>
                                    </ul>
                                </div>
                                <form class="form-horizontal theme-form" id="components">
                                    <fieldset>
                                        <div class="tab-content">
                                            <div class="tab-pane active" id="input">
                                                <draggable @end="finish()"  :group="{ name: 'universalGroup', pull: 'clone', put: false }">
                                                <div class="component"  id="text">
                                                    <!-- Text input-->
                                                   
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" for="textinput">Text Input</label>
                                                        <div class="col-lg-12">
                                                            <input  name="textinput" type="text" placeholder="placeholder" class="form-control btn-square input-md">
                                                            <p class="help-block">help</p>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="password">
                                                    <!-- Password input-->
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" >Password Input</label>
                                                        <div class="col-lg-12">
                                                            <input id="passwordinput" name="passwordinput" type="password" placeholder="placeholder" class="form-control btn-square input-md">
                                                            <span class="help-block">help</span>
                                                        </div>
                                                    </div>
                                                </div>
                                           
                                                <div class="component" id="search">
                                                    <!-- Search input-->
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" for="searchinput">Search Input</label>
                                                        <div class="col-lg-12">
                                                            <input id="searchinput" name="searchinput" type="search" placeholder="placeholder" class="form-control btn-square input-md">
                                                            <p class="help-block">help</p>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="pre">
                                                    <!-- Prepended text-->
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" for="prependedtext">Prepended Text</label>
                                                        <div class="col-lg-12">
                                                            <div class="input-group">
                                                                <span class="input-group-text btn btn-primary">prepend</span>
                                                                <input id="prependedtext" name="prependedtext" class="form-control btn-square" placeholder="placeholder" type="text">
                                                            </div>
                                                            <p class="help-block">help</p>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="ape">
                                                    <!-- Appended Input-->
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" for="appendedtext">Appended Text</label>
                                                        <div class="col-lg-12">
                                                            <div class="input-group">
                                                                <input id="appendedtext" name="appendedtext" class="form-control btn-square" placeholder="placeholder" type="text">
                                                                <span class="input-group-text btn btn-primary btn-right">append</span>
                                                            </div>
                                                            <p class="help-block">help</p>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="pcheck">
                                                    <!-- Prepended checkbox -->
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" for="prependedcheckbox">Prepended Checkbox</label>
                                                        <div class="col-lg-12">
                                                            <div class="input-group">
                                                                <span class="input-group-text">
                                                                    <input type="checkbox">
                                                                </span>
                                                                <input id="prependedcheckbox" name="prependedcheckbox" class="form-control btn-square" type="text" placeholder="placeholder">
                                                            </div>
                                                            <p class="help-block">help</p>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="acheck">
                                                    <!-- Appended checkbox -->
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" for="appendedcheckbox">Appended Checkbox</label>
                                                        <div class="col-lg-12">
                                                            <div class="input-group">
                                                                <input id="appendedcheckbox" name="appendedcheckbox" class="form-control btn-square" type="text" placeholder="placeholder">
                                                                <span class="input-group-text checkbox-radius">
                                                                    <input type="checkbox">
                                                                </span></div>
                                                        </div>
                                                        <p class="help-block">help</p>

                                                    </div>
                                                </div>
                                                <div class="component" id="button">
                                                    <!-- Button Drop Down -->
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" for="buttondropdown">Button Drop Down</label>
                                                        <div class="col-lg-12">
                                                            <div class="input-group">
                                                                <input id="buttondropdown" name="buttondropdown" class="form-control btn-square" placeholder="placeholder" type="text">
                                                                <div class="input-group-text p-0">
                                                                    <button type="button" class="btn btn-primary dropdown-toggle btn-square" data-toggle="dropdown">
                                                                        Action
                                                                        <span class="caret"></span>
                                                                    </button>
                                                                    <ul class="dropdown-menu pull-right">
                                                                        <li><a href="#" class="dropdown-item">Option one</a></li>
                                                                        <li><a href="#" class="dropdown-item">Option two</a></li>
                                                                        <li><a href="#" class="dropdown-item">Option three</a></li>
                                                                    </ul>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="area">
                                                    <!-- Textarea -->
                                                    <div class="mb-3 row mb-0">
                                                        <label class="col-lg-12 form-label text-lg-start" for="textarea">Text Area</label>
                                                        <div class="col-lg-12">
                                                            <textarea class="form-control btn-square" id="textarea" name="textarea">default text</textarea>
                                                        </div>
                                                    </div>
                                                </div>
                                            </draggable >
                                            </div>
                                            <div class="tab-pane" id="radio">
                                                <draggable  :group="{ name: 'universalGroup', pull: 'clone', put: false }">

                                                <div class="component" id="multiple">
                                                    <!-- Multiple Radios -->
                                                    <div class="mb-3 row">
                                                        <label class="col-sm-3 form-label text-lg-start" for="radios">Multiple Radios</label>
                                                        <div class="col-sm-9 pl-md-radios">
                                                            <div class="radio">
                                                                <label for="radios-0">Option one
                                                                </label>
                                                                <input type="radio" name="radios" id="radios-5" value="1" checked="checked">
                                                            </div>
                                                            <div class="radio">
                                                                <label for="radios-1">Option two
                                                                </label>
                                                                <input type="radio" name="radios" id="radios-6" value="2">
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="inline">
                                                    <!-- Multiple Radios (inline) -->
                                                    <div class="mb-3 row">
                                                        <label class="col-sm-3 form-label text-lg-start" for="radios">Inline Radios</label>
                                                        <div class="col-sm-9  pl-md-radios">
                                                            <div class="m-checkbox-inline">
                                                                <div class="radio radio-primary">
                                                                    <label class="radio-inline" for="radios-0"> 1</label>
                                                                    <input type="radio" name="radios" id="radios-0" value="1" checked="checked">
                                                                </div>
                                                                <div class="radio radio-primary">
                                                                    <label class="radio-inline" for="radios-1"> 2</label>
                                                                    <input type="radio" name="radios" id="radios-1" value="2">
                                                                </div>
                                                                <div class="radio radio-primary">
                                                                    <label class="radio-inline" for="radios-2"> 3</label>
                                                                    <input type="radio" name="radios" id="radios-2" value="3">
                                                                </div>
                                                                <div class="radio radio-primary">
                                                                    <label class="radio-inline" for="radios-3"> 4</label>
                                                                    <input type="radio" name="radios" id="radios-3" value="4">
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>

                                                </div>
                                                <div class="component" id="cmuliple">
                                                    <!-- Multiple Checkboxes -->
                                                    <div class="mb-3 row">
                                                        <label class="col-sm-3 form-label text-lg-start" for="checkboxes">Multiple Checkboxes</label>
                                                        <div class="col-sm-9">
                                                            <div class="checkbox">
                                                                <input type="checkbox" name="checkboxes" id="checkboxes-0" value="1">
                                                                <label for="checkboxes-0" class="mt-0">
                                                                    Option one
                                                                </label>
                                                            </div>
                                                            <div class="checkbox">
                                                                <input type="checkbox" name="checkboxes" id="checkboxes-1" value="2">
                                                                <label for="checkboxes-1" class="mt-0">
                                                                    Option two
                                                                </label>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="cinline">
                                                    <!-- Multiple Checkboxes (inline) -->
                                                    <div class="mb-3 row mb-0">
                                                        <label class="col-sm-3 form-label text-lg-start mb-0" for="checkboxes">Inline Checkboxes</label>
                                                        <div class="col-sm-9">
                                                            <div class="m-checkbox-inline">

                                                                <div class="checkbox"> <input type="checkbox" name="checkboxes" id="checkboxes-7" value="1">
                                                                    <label class="checkbox-inline mb-0" for="checkboxes-0">
                                                                        1
                                                                    </label> </div>

                                                                <div class="checkbox"> <input type="checkbox" name="checkboxes" id="checkboxes-8" value="2">
                                                                    <label class="checkbox-inline mb-0" for="checkboxes-1">
                                                                        2
                                                                    </label> </div>

                                                                <div class="checkbox"> <input type="checkbox" name="checkboxes" id="checkboxes-9" value="3">
                                                                    <label class="checkbox-inline mb-0" for="checkboxes-2">
                                                                        3
                                                                    </label> </div>

                                                                <div class="checkbox"> <input type="checkbox" name="checkboxes" id="checkboxes-10" value="4">
                                                                    <label class="checkbox-inline mb-0" for="checkboxes-3">
                                                                        4
                                                                    </label> </div>

                                                            </div>
                                                        </div>
                                                    </div>
                                                </div></draggable>
                                            </div>

                                            <div class="tab-pane" id="select">
                                                <draggable  :group="{ name: 'universalGroup', pull: 'clone', put: false }">

                                                <div class="component" id="basic">
                                                    <!-- Select Basic -->
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" for="selectbasic">Select Basic</label>
                                                        <div class="col-lg-12">
                                                            <select id="selectbasic" name="selectbasic" class="form-control btn-square">
                                                                <option value="1">Option one</option>
                                                                <option value="2">Option two</option>
                                                            </select>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="smultiple">
                                                    <!-- Select Multiple -->
                                                    <div class="mb-3 row mb-0">
                                                        <label class="col-lg-12 form-label text-lg-start" for="selectmultiple">Select Multiple</label>
                                                        <div class="col-lg-12">
                                                            <select id="selectmultiple" name="selectmultiple" class="form-control btn-square" multiple>
                                                                <option value="1">Option one</option>
                                                                <option value="2">Option two</option>
                                                            </select>
                                                        </div>
                                                    </div>
                                                </div>
                                                </draggable>
                                            </div>
                                            <div class="tab-pane" id="buttons">
                                                <draggable  :group="{ name: 'universalGroup', pull: 'clone', put: false }">

                                                <div class="component" id="file">
                                                    <!-- File Button -->
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" for="filebutton">File Button</label>
                                                        <div class="col-lg-12">
                                                            <input id="filebutton" name="filebutton" class="input-file" type="file">
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="single">
                                                    <!-- Button -->
                                                    <div class="mb-3 row">
                                                        <label class="col-lg-12 form-label text-lg-start" for="singlebutton">Single Button</label>
                                                        <div class="col-lg-12">
                                                            <button id="singlebutton" name="singlebutton" class="btn btn-primary">Button</button>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="component" id="double">
                                                    <!-- Button (Double) -->
                                                    <div class="mb-3 row mb-0">
                                                        <label class="col-lg-12 form-label text-lg-start" for="button1id">Double Button</label>
                                                        <div class="col-md-9">
                                                            <button id="button1id" name="button1id" class="btn btn-success">Good Button</button>
                                                            <button id="button2id" name="button2id" class="btn btn-danger">Scary Button</button>
                                                        </div>
                                                    </div>
                                                </div>
                                                </draggable>
                                            </div>
                                            <div class="tab-pane" id="view">
                                                <h6>Rendered source of your form:</h6>
                                             
                                                <textarea id="render" class="render p-3" spellcheck="false" :value="text"></textarea>
                                            </div>
                                        </div>
                                    </fieldset>
                                </form>
                            </div>
                            <div class="col-lg-12 col-xl-6 lg-mt-col">
                                <div class="form-builder-header-1">
                                    <h6 class="mt-0">Drag Elements Here</h6>
                                </div>
                                <form class="form-horizontal drag-box" id="target"><fieldset><div class="component" 
                                data-title="Form Name" data-trigger="manual" data-html="true"><!-- Form Name -->
                                <h6 class="m-t-10">Form Name</h6><hr>
                               <!-- <div @drop="onDrop($event, index)" @dragover.prevent
                               @dragenter.prevent></div> -->
                               <draggable :list="lista"   style="min-height: 100px" group="universalGroup" id="formhtml"  ></draggable>
                                </div></fieldset></form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>
<script>
import {
    VueDraggableNext
} from 'vue-draggable-next'
import list from '../../data/draggable'
export default {
    data(){
        return{
            text:'',
            lista: list
    }},
    components: {
        draggable: VueDraggableNext,
    },
    methods:{
        finish () {
            if(document.getElementById('formhtml')=== null){
           this.text=''}
          else{
            document.getElementById('formhtml').innerHTML =document.getElementById('formhtml').outerHTML
            this.text= document.getElementById('formhtml').innerHTML}
    },
  
}
}
</script>