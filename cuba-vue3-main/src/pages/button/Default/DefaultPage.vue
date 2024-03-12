<template>
  <div class="card" id="default">
    <div class="card-header pb-0">
      <h3>Default Buttons</h3>
      <settingPage/>
      <span>Bootstrap state buttons</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-primary" type="button" data-bs-toggle="tooltip" title="btn btn-primary">Primary Button</button>
      <button class="btn btn-secondary" type="button" data-bs-toggle="tooltip" title="btn btn-secondary">Secondary Button</button>
      <button class="btn btn-success" type="button" data-bs-toggle="tooltip" title="btn btn-success">Success Button</button>
      <button class="btn btn-info" type="button" data-bs-toggle="tooltip" title="btn btn-info">Info Button</button>
      <button class="btn btn-warning" type="button" data-bs-toggle="tooltip" title="btn btn-warning">Warning Button</button>
      <button class="btn btn-danger" type="button" data-bs-toggle="tooltip" title="btn btn-danger">Danger Button</button>
      <button class="btn btn-light" type="button" data-bs-toggle="tooltip" title="btn btn-light">Light Button</button>
     
    </div>
  </div>
  <div class="card" id="large-btn">
    <div class="card-header pb-0">
      <h3>Large Buttons</h3>
   <settingPage/>
     <span>Add <code>.btn-lg</code> class for large size buttons</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-primary btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-primary btn-lg">Primary Button</button>
      <button class="btn btn-secondary btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-secondary btn-lg">Secondary Button</button>
      <button class="btn btn-success btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-success btn-lg">Success Button</button>
      <button class="btn btn-info btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-info btn-lg">Info Button</button>
      <button class="btn btn-warning btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-warning btn-lg">Warning Button</button>
      <button class="btn btn-danger btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-danger btn-lg">Danger Button</button>
      <button class="btn btn-light btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-light btn-lg">Light Button</button>
      
    </div>
  </div>
  <div class="card" id="small-btn">
    <div class="card-header pb-0">
      <h3>Small Buttons</h3>
      <settingPage/><span>Add <code>.btn-sm</code> class for small size buttons</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-primary btn-sm" type="button" title="btn btn-primary btn-sm">Primary Button</button>
      <button class="btn btn-secondary btn-sm" type="button" title="btn btn-secondary btn-sm">Secondary Button</button>
      <button class="btn btn-success btn-sm" type="button" title="btn btn-success btn-sm">Success Button</button>
      <button class="btn btn-info btn-sm" type="button" title="btn btn-info btn-sm">Info Button</button>
      <button class="btn btn-warning btn-sm" type="button" title="btn btn-warning btn-sm">Warning Button</button>
      <button class="btn btn-danger btn-sm" type="button" title="btn btn-danger btn-sm">Danger Button</button>
      <button class="btn btn-light btn-sm" type="button" title="btn btn-light btn-sm">Light Button</button>
    </div>
  </div>
  <div class="card" id="ex-small-btn">
    <div class="card-header pb-0">
      <h3>Extra Small buttons</h3>
      <settingPage/><span>Add <code>.btn-xs</code> class for extra small size buttons</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-primary btn-xs" type="button" title="btn btn-primary btn-xs">Primary Button</button>
      <button class="btn btn-secondary btn-xs" type="button" title="btn btn-secondary btn-xs">Secondary Button</button>
      <button class="btn btn-success btn-xs" type="button" title="btn btn-success btn-xs">Success Button</button>
      <button class="btn btn-info btn-xs" type="button" title="btn btn-info btn-xs">Info Button</button>
      <button class="btn btn-warning btn-xs" type="button" title="btn btn-warning btn-xs">Warning Button</button>
      <button class="btn btn-danger btn-xs" type="button" title="btn btn-danger btn-xs">Danger Button</button>
      <button class="btn btn-light btn-xs" type="button" title="btn btn-light btn-xs">Light Button</button>
    </div>
  </div>
  <div class="card" id="active-btn">
    <div class="card-header pb-0">
      <h3>Active Buttons</h3>
     <settingPage/><span>Add <code>.active</code> class for active state</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-primary active" type="button" title="btn btn-primary active">Active</button>
      <button class="btn btn-secondary active" type="button" title="btn btn-secondary active">Active</button>
      <button class="btn btn-success active" type="button" title="btn btn-success active">Active</button>
      <button class="btn btn-info active" type="button" title="btn btn-info active">Active</button>
      <button class="btn btn-warning active txt-dark" type="button" title="btn btn-warning active">Active</button>
      <button class="btn btn-danger active" type="button" title="btn btn-danger active">Active</button>
      <button class="btn btn-light active txt-dark" type="button" title="btn btn-light active">Active</button>
      
    </div>
  </div>
  <div class="card" id="disabled-btn">
    <div class="card-header pb-0">
      <h3>Disabled Buttons</h3>
      <settingPage/><span>Add <code>.disabled</code> class or <code>disabled="disabled"</code> attribute for disabled button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-primary disabled" type="button">Disabled</button>
      <button class="btn btn-secondary disabled" type="button">Disabled</button>
      <button class="btn btn-success disabled" type="button">Disabled</button>
      <button class="btn btn-info disabled" type="button">Disabled</button>
      <button class="btn btn-warning disabled" type="button">Disabled</button>
      <button class="btn btn-danger disabled" type="button">Disabled</button>
      <button class="btn btn-light disabled" type="button">Disabled</button>
    </div>
  </div>
</template>
<script>
import { Tooltip } from 'bootstrap/dist/js/bootstrap.esm.min'
export default{
  mounted(){
    new Tooltip(document.body,{
      selector: "[data-bs-toggle='tooltip']"
    })
  }
}
</script>