<template>
    <breadCrumbs title="Time Picker" main="Form Wizards" title1="Time Picker" />

    <div class="container-fluid">
        <div class="row">
          <div class="col-lg-6">
            <div class="card">
              <div class="card-header pb-0">
                <h3>Default:</h3>
              </div>
              <div class="card-body">
                <form class="theme-form">
                  <div>
                    <div class="input-group clockpicker">
                      <input class="form-control" type="text" value="09:30"><span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="card">
              <div class="card-header pb-0">
                <h3>Align the arrow to top, auto close:</h3>
              </div>
              <div class="card-body">
                <form class="theme-form">
                  <div>
                    <div class="input-group clockpicker pull-center" data-placement="left" data-align="top" data-autoclose="true">
                      <input class="form-control" type="text" value="13:14"><span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="card">
              <div class="card-header pb-0">
                <h3>Set options in javascript, instead of data-* :</h3>
              </div>
              <div class="card-body">
                <form class="theme-form">
                  <div>
                    <div class="input-group clockpicker" data-placement="top" data-align="left" data-donetext="Done">
                      <input class="form-control" type="text" value="18:00"><span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="card">
              <div class="card-header pb-0">
                <h3>Set default value, input without addon:</h3>
              </div>
              <div class="card-body">
                <div class="clearfix">
                  <form class="theme-form">
                    <div>
                      <input class="form-control" id="single-input" type="text" value="" placeholder="Addon">
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
</template>