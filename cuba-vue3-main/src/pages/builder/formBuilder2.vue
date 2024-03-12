<template>
<div class="form-builder">
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-12">
                <div class="card">
                    <div class="card-header">
                        <h5>Form Builder</h5>
                    </div>
                    <div class="card-body form-builder">
                        <div class="form-builder-column">
                            <div class="row">
                                <div class="col-sm-12">
                                    <div class="form-builder-2-header">
                                        <div>
                                            <ul class="nav nav-primary" id="pills-tab" role="tablist">
                                                <li class="nav-item"><a class="nav-link active" id="pills-input-tab" data-bs-toggle="pill" href="#pills-input" role="tab" aria-controls="pills-input" aria-selected="true">Input</a></li>
                                                <li class="nav-item"><a class="nav-link" id="pills-radcheck-tab" data-bs-toggle="pill" href="#pills-radcheck" role="tab" aria-controls="pills-radcheck" aria-selected="false">Radio/Checkbox</a></li>
                                                <li class="nav-item"><a class="nav-link" id="pills-select-tab" data-bs-toggle="pill" href="#pills-select" role="tab" aria-controls="pills-select" aria-selected="false">Select</a></li>
                                                <li class="nav-item"><a class="nav-link" id="pills-button-tab" data-bs-toggle="pill" href="#pills-button" role="tab" aria-controls="pills-button" aria-selected="false">Buttons</a></li>
                                            </ul>
                                        </div>
                                        <div>
                                            <nav class="navbar navbar-expand-md p-0">
                                                <form class="form-inline" @submit.prevent="">
                                                    <div class="me-2">
                                                        <select class="btn form-control b-light" id="n-columns" @change="change($event)">
                                                            <option value="1">1 Column</option>
                                                            <option value="2">2 Columns</option>
                                                        </select>
                                                    </div>
                                                    <button class="btn btn-primary"  data-bs-toggle="modal" data-bs-target="#exampleModalCenter" >Copy HTML</button>
                                                </form>
                                            </nav>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-6 col-xl-6">
                                    <div class="tab-content" id="pills-tabContent">
                                        <div class="tab-pane fade show active" id="pills-input" role="tabpanel" aria-labelledby="pills-input-tab">
                                            <form class="theme-form">
                                                <draggable @end="finish($event)" :group="{ name: 'universalGroup', pull: 'clone', put: false }">
                                                    <div class="mb-3 draggable" id="input">
                                                        <label for="input-text-1">Text Input</label>
                                                        <input class="form-control btn-square" id="input-text-1" type="email" placeholder="Enter email">
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                    <p class="tools" id="add">						
                                                    <a class="edit-link">Edit HTML</a>
                                                    <a class="remove-link">Remove</a>
                                                </p>
                                                    <hr>
                                                    <div class="mb-3 draggable">
                                                        <label for="input-password-1">Password</label>
                                                        <input class="form-control btn-square" id="input-password-1" type="password" placeholder="Password">
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                    <hr>
                                                    <div class="mb-3 draggable">
                                                        <label for="select-1">Select</label>
                                                        <select class="form-control btn-square" id="select-1">
                                                            <option value="Option 1">Option 1</option>
                                                            <option value="Option 2">Option 2</option>
                                                            <option value="Option 3">Option 3</option>
                                                        </select>
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                    <hr>
                                                    <div class="mb-3 draggable">
                                                        <label for="input-file-1">File input</label>
                                                        <input id="input-file-1" type="file">
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                    <hr>
                                                    <div class="mb-3 draggable">
                                                        <label for="prependedcheckbox">Appended Checkbox</label>
                                                        <div class="input-group"><span class="input-group-text">
                                                                <input class="me-0" type="checkbox"></span>
                                                            <input class="form-control btn-square" id="prependedcheckbox" name="prependedcheckbox" type="text" placeholder="Placeholder">
                                                        </div>
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                    <hr>
                                                    <div class="mb-3 draggable">
                                                        <label for="prependedcheckbox">Button DropDown</label>
                                                        <div class="input-group">
                                                            <input class="form-control btn-square" id="buttondropdown" name="buttondropdown" placeholder="Placeholder" type="text">
                                                            <div class="input-group-btn btn btn-square p-0">
                                                                <button class="btn btn-primary dropdown-toggle btn-square" type="button" data-bs-toggle="dropdown">Action<span class="caret"></span></button>
                                                                <ul class="dropdown-menu pull-right">
                                                                    <li><a class="dropdown-item" href="#">Option one</a></li>
                                                                    <li><a class="dropdown-item" href="#">Option two</a></li>
                                                                    <li><a class="dropdown-item" href="#">Option three</a></li>
                                                                </ul>
                                                            </div>
                                                        </div>
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                </draggable>
                                            </form>
                                        </div>
                                        <div class="tab-pane fade" id="pills-radcheck" role="tabpanel" aria-labelledby="pills-radcheck-tab">
                                            <form class="theme-form">
                                                <draggable @end="finish" :group="{ name: 'universalGroup', pull: 'clone', put: false }">

                                                    <div class="mb-3 draggable">
                                                        <label>Inline checkbox</label>
                                                        <div class="col">
                                                            <div class="m-checkbox-inline">
                                                                <div class="checkbox">
                                                                    <input id="checkbox1" type="checkbox">
                                                                    <label for="checkbox1">Default 1</label>
                                                                </div>
                                                                <div class="checkbox">
                                                                    <input id="checkbox2" type="checkbox">
                                                                    <label for="checkbox2">Default 2</label>
                                                                </div>
                                                                <div class="checkbox">
                                                                    <input id="checkbox3" type="checkbox">
                                                                    <label for="checkbox3">Default 3</label>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <p class="help-block m-t-help-block">Example block-level help text here.</p>
                                                    </div>
                                                    <hr>
                                                    <div class="mb-3 draggable">
                                                        <label>Inline Radiobox</label>
                                                        <div class="col">
                                                            <div class="m-checkbox-inline">
                                                                <div class="radio radio-theme">
                                                                    <input id="radioinline1" type="radio" name="radio1" value="option1">
                                                                    <label for="radioinline1">Option 1</label>
                                                                </div>
                                                                <div class="radio radio-theme">
                                                                    <input id="radioinline2" type="radio" name="radio1" value="option2">
                                                                    <label for="radioinline2">Option 2</label>
                                                                </div>
                                                                <div class="radio radio-theme">
                                                                    <input id="radioinline3" type="radio" name="radio1" value="option3">
                                                                    <label for="radioinline3">Option 3</label>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <p class="help-block m-t-help-block">Example block-level help text here.</p>
                                                    </div>
                                                    <hr>
                                                    <div class="mb-3 draggable">
                                                        <label>Custom checkbox</label>
                                                        <div class="col">
                                                            <div class="checkbox">
                                                                <input id="checkbox-def" type="checkbox">
                                                                <label for="checkbox-def">Default</label>
                                                            </div>
                                                            <div class="checkbox">
                                                                <input id="checkbox-dis" type="checkbox" disabled="">
                                                                <label for="checkbox-dis">Disabled</label>
                                                            </div>
                                                            <div class="checkbox">
                                                                <input id="checkbox-chk" type="checkbox" checked="">
                                                                <label for="checkbox-chk">Checked</label>
                                                            </div>
                                                        </div>
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                </draggable>
                                            </form>
                                        </div>
                                        <div class="tab-pane fade" id="pills-select" role="tabpanel" aria-labelledby="pills-select-tab">
                                            <form class="theme-form">
                                                <draggable @end="finish" :group="{ name: 'universalGroup', pull: 'clone', put: false }">

                                                    <div class="mb-3 draggable">
                                                        <label for="formcontrol-select1">Example select</label>
                                                        <select class="form-control btn-square" id="formcontrol-select1">
                                                            <option>1</option>
                                                            <option>2</option>
                                                            <option>3</option>
                                                            <option>4</option>
                                                            <option>5</option>
                                                        </select>
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                    <hr>
                                                    <div class="mb-3 draggable">
                                                        <label for="formcontrol-select2">Example multiple select</label>
                                                        <select class="form-control btn-square" id="formcontrol-select2" multiple>
                                                            <option>1</option>
                                                            <option>2</option>
                                                            <option>3</option>
                                                            <option>4</option>
                                                            <option>5</option>
                                                        </select>
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                </draggable>
                                            </form>
                                        </div>
                                        <div class="tab-pane fade" id="pills-button" role="tabpanel" aria-labelledby="pills-button-tab">
                                            <form class="theme-form">
                                                <draggable @end="finish" :group="{ name: 'universalGroup', pull: 'clone', put: false }">

                                                    <div class="mb-3 draggable">
                                                        <label class="m-r-10">Single Button</label><br>
                                                        <button class="btn btn-primary active" type="button" data-original-title="btn btn-dark active" title="">Button</button>
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                    <hr>
                                                    <div class="mb-3 draggable">
                                                        <label class="m-r-10">Double Button</label><br>
                                                        <button class="btn btn-primary" type="button" data-original-title="btn btn-primary-gradien" title="">Primary</button>
                                                        <button class="btn btn-secondary" type="button" data-original-title="btn btn-primary-gradien" title="">Secondary</button>
                                                        <p class="help-block">Example block-level help text here.</p>
                                                    </div>
                                                </draggable>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-6 col-xl-6 lg-mt">
                                    <!-- Form builder column wise start-->
                                    <div class="drag-bx card-body">
                                        <div class="text-muted empty-form text-center">
                                            <h6>Drag & Drop elements to build form.</h6>
                                        </div>
                                        <div class="form-body row form-builder-2">
                                            <div class="droppable sortable" :class="show==2?'col-md-6':'col-md-12'">
                                                <draggable :list="lista" style="min-height: 100px" group="universalGroup" id="formhtml"></draggable>
                                            </div>
                                            <div class="col-md-6 droppable sortable" :style="{display:show==2?'':'none'}">
                                                <draggable :list="lista" style="min-height: 100px" group="universalGroup" id="formhtml"></draggable>
                                            </div>
                                            <!-- <div class="col-md-6 droppable sortable" :style="{display:show==2?'':'none'}"><draggable :list="lista"   style="min-height: 100px" group="universalGroup" id="formhtml"  ></draggable></div> -->
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- Form builder column wise ends-->
                        <!-- Container-fluid Ends-->
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<div class="modal" id="exampleModalCenter"  tabindex="-1" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h4 class="modal-title">Copy HTML</h4> <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body ui-front">
                <grammarly-extension data-grammarly-shadow-root="true" style="position: absolute; top: 0px; left: 0px; pointer-events: none;" class="cGcvT"></grammarly-extension>
                <grammarly-extension data-grammarly-shadow-root="true" style="mix-blend-mode: darken; position: absolute; top: 0px; left: 0px; pointer-events: none;" class="cGcvT"></grammarly-extension> <textarea class="form-control btn-square" style="min-height: 200px; margin-bottom: 10px;		font-family: Monaco, Fixed" spellcheck="true">&lt;div class="row form-builder-2"&gt;
        &lt;div class="col-md-12"&gt;
            &lt;div class="mb-3 ui-draggable-handle" style="position: static;"&gt;
                &lt;label for="input-text-1"&gt;Text Input&lt;/label&gt;
                &lt;input class="form-control btn-square" id="input-text-1" type="email" placeholder="Enter email"&gt;
                &lt;p class="help-block"&gt;Example block-level help text here.&lt;/p&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;</textarea>
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
    data() {
        return {
            display: false,
            show: 1,
            text: '',
            lista: list
        }
    },
    components: {
        draggable: VueDraggableNext,
    },
    methods: {
        change(e) {
            this.show = e.target.value
            console.log("selected value is", e.target.value)
        },
        finish(e) {
            // this.display =
            var a=document.getElementById(e.item.id)
            console.log("dsa element is",document.getElementById(e.item.id))
            if (document.getElementById(e.item)==null)
            {
                console.log("outter",document.getElementById('add').outerHTML )
                a[0].append(document.getElementById('add').outerHTML)
                console.log("inner",document.getElementById(e.item.id).outerHTML )

            }
            if (document.getElementById('formhtml') === null) {
                this.text = ''
            } else {
                document.getElementById('formhtml').innerHTML = document.getElementById('formhtml').outerHTML
                this.text = document.getElementById('formhtml').innerHTML
            }
        },

    }
}
</script>
