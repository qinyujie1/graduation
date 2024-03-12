<template>
<div class="card">
    <div class="card-header pb-0">
        <h3>Default buttons</h3>
        <div class="card-header-right">
            <settingPage /> <span>Add <code>.btn-pill</code> class for edge button</span>
        </div>
        <div class="card-body btn-showcase">
            <button class="btn btn-pill btn-primary" type="button" title="btn btn-pill btn-primary">Primary Button</button>
            <button class="btn btn-pill btn-secondary" type="button" title="btn btn-pill btn-secondary">Secondary Button</button>
            <button class="btn btn-pill btn-success" type="button" title="btn btn-pill btn-success">Success Button</button>
            <button class="btn btn-pill btn-info" type="button" title="btn btn-pill btn-info">Info Button</button>
            <button class="btn btn-pill btn-warning" type="button" title="btn btn-pill btn-warning">Warning Button</button>
            <button class="btn btn-pill btn-danger" type="button" title="btn btn-pill btn-danger">Danger Button</button>
            <button class="btn btn-pill btn-light" type="button" title="btn btn-pill btn-light">Light Button</button>

        </div>
    </div>
    <div class="card">
        <div class="card-header pb-0">
            <h3>Large buttons</h3>
            <settingPage /><span>Add <code>.btn-pill</code> and <code>.btn-lg</code> class for large button</span>
        </div>
        <div class="card-body btn-showcase">
            <button class="btn btn-pill btn-primary btn-lg" type="button" title="btn btn-pill btn-primary btn-lg">Primary Button</button>
            <button class="btn btn-pill btn-secondary btn-lg" type="button" title="btn btn-pill btn-secondary btn-lg">Secondary Button</button>
            <button class="btn btn-pill btn-success btn-lg" type="button" title="btn btn-pill btn-success btn-lg">Success Button</button>
            <button class="btn btn-pill btn-info btn-lg" type="button" title="btn btn-pill btn-info btn-lg">Info Button</button>
            <button class="btn btn-pill btn-warning btn-lg" type="button" title="btn btn-pill btn-warning btn-lg">Warning Button</button>
            <button class="btn btn-pill btn-danger btn-lg" type="button" title="btn btn-pill btn-danger btn-lg">Danger Button</button>
            <button class="btn btn-pill btn-light btn-lg" type="button" title="btn btn-pill btn-light btn-lg">Light Button</button>

        </div>
    </div>
    <div class="card">
        <div class="card-header pb-0">
            <h3>Small buttons</h3>
            <settingPage /><span>Add <code>.btn-pill</code> and <code>.btn-sm</code> class for small button</span>
        </div>
        <div class="card-body btn-showcase">
            <button class="btn btn-pill btn-primary btn-sm" type="button" title="btn btn-pill btn-primary btn-sm">Primary Button</button>
            <button class="btn btn-pill btn-secondary btn-sm" type="button" title="btn btn-pill btn-secondary btn-sm">Secondary Button</button>
            <button class="btn btn-pill btn-success btn-sm" type="button" title="btn btn-pill btn-success btn-sm">Success Button</button>
            <button class="btn btn-pill btn-info btn-sm" type="button" title="btn btn-pill btn-info btn-sm">Info Button</button>
            <button class="btn btn-pill btn-warning btn-sm" type="button" title="btn btn-pill btn-warning btn-sm">Warning Button</button>
            <button class="btn btn-pill btn-danger btn-sm" type="button" title="btn btn-pill btn-danger btn-sm">Danger Button</button>
            <button class="btn btn-pill btn-light btn-sm" type="button" title="btn btn-pill btn-light btn-sm">Light Button</button>

        </div>
    </div>
    <div class="card">
        <div class="card-header pb-0">
            <h3>Active Buttons</h3>
            <settingPage /><span>Add <code>.active</code> for active state</span>
        </div>
        <div class="card-body btn-showcase">
            <button class="btn btn-pill btn-primary active" type="button" title="btn btn-pill btn-primary active">Active</button>
            <button class="btn btn-pill btn-secondary active" type="button" title="btn btn-pill btn-secondary active">Active</button>
            <button class="btn btn-pill btn-success active" type="button" title="btn btn-pill btn-success active">Active</button>
            <button class="btn btn-pill btn-info active" type="button" title="btn btn-pill btn-info active">Active</button>
            <button class="btn btn-pill btn-warning active" type="button" title="btn btn-pill btn-warning active">Active</button>
            <button class="btn btn-pill btn-danger active" type="button" title="btn btn-pill btn-danger active">Active</button>
            <button class="btn btn-pill btn-light active txt-dark" type="button" title="btn btn-pill btn-light active">Active</button>

        </div>
    </div>
    <div class="card">
        <div class="card-header pb-0">
            <h3>Disabled buttons</h3>
            <settingPage /> <span>Add <code>.disabled</code> class or <code>disabled="disabled"</code> attribute for disabled button</span>
        </div>
        <div class="card-body btn-showcase">
            <button class="btn btn-pill btn-primary disabled" type="button">Disabled</button>
            <button class="btn btn-pill btn-secondary disabled" type="button">Disabled</button>
            <button class="btn btn-pill btn-success disabled" type="button">Disabled</button>
            <button class="btn btn-pill btn-info disabled" type="button">Disabled</button>
            <button class="btn btn-pill btn-warning disabled" type="button">Disabled</button>
            <button class="btn btn-pill btn-danger disabled" type="button">Disabled</button>
            <button class="btn btn-pill btn-light disabled" type="button">Disabled</button>

        </div>
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