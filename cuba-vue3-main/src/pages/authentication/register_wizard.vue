<template>
    <div class="container-fluid">
        <div class="row">         
          <div class="col-12 p-0">
            <div>
              <div class="theme-form">                     
                <div class="wizard-4" id="wizard">                       
                    <ul class="anchor">
                      <li><a class="logo text-start ps-0" href="index.html" data-bs-original-title="" title=""><img class="img-fluid for-light" src="@/assets/images/logo/logo.png" alt="looginpage"><img class="img-fluid for-dark" src="@/assets/images/logo/logo_dark.png" alt="looginpage"></a></li>
                      <li><a href="#step-1" class="selected" isdone="1" rel="1" data-bs-original-title="" title="">
                          <h4>1</h4>
                          <h5>personal</h5><small>Add personal details</small></a></li>
                      <li><a href="#step-2" class="done" isdone="1" rel="2" data-bs-original-title="" title="">
                          <h4>2</h4>
                          <h5>Address</h5><small>Add additional info</small></a></li>
                      <li><a href="#step-3" class="done" isdone="1" rel="3" data-bs-original-title="" title="">
                          <h4>3</h4>
                          <h5>Message</h5><small>Add message(optional)</small></a></li>
                      <li class="pb-0"><a href="#step-4" class="done" isdone="1" rel="4" data-bs-original-title="" title="">
                          <h4>4</h4>
                          <h5> Done <i class="fa fa-thumbs-o-up"></i></h5><small>Complete.. !</small></a></li>
                      <li>                           <img src="@/assets/images/login/icon.png" alt="looginpage"></li>
                    </ul>
                    
                    
                    
                    
                  <div class="step-container login-card" style="height: 450.391px;"><div id="step-1" class="content" style="left: 0px;">
                      <div class="wizard-title">
                        <h2>Sign up to account</h2>
                        <h5 class="text-muted mb-4">Enter your email &amp; password to login</h5>
                      </div>
                      <div class="login-main">
                        <div class="theme-form">
                          <div class="form-group mb-3">
                            <label for="name">First Name</label>
                            <input class="form-control" id="name" type="text" placeholder="Johan" required="required" data-bs-original-title="" title="">
                          </div>
                          <div class="form-group mb-3">
                            <label for="lname">Last Name</label>
                            <input class="form-control" id="lname" type="text" placeholder="Deo" data-bs-original-title="" title="">
                          </div>
                          <div class="form-group mb-3">
                            <label for="contact">Contact No.</label>
                            <input class="form-control" id="contact" type="number" placeholder="123456789" data-bs-original-title="" title="">
                          </div>
                        </div>
                      </div>
                    </div><div id="step-2" class="content" style="left: 1294.5px; display: none;">
                      <div class="wizard-title">
                        <h2>Sign up to account</h2>
                        <h5 class="text-muted mb-4">Enter your email &amp; password to login</h5>
                      </div>
                      <div class="login-main">
                        <div class="theme-form">
                          <div class="form-group mb-3 m-t-15">
                            <label for="exampleFormControlInput1">Email address</label>
                            <input class="form-control" id="exampleFormControlInput1" type="email" placeholder="name@example.com" data-bs-original-title="" title="">
                          </div>
                          <div class="form-group mb-3">
                            <label for="exampleInputPassword1">Password</label>
                            <input class="form-control" id="exampleInputPassword1" type="password" placeholder="Password" data-bs-original-title="" title="">
                          </div>
                          <div class="form-group mb-3">
                            <label for="exampleInputPassword1">Confirm Password</label>
                            <input class="form-control" id="exampleInputcPassword1" type="password" placeholder="Enter again" data-bs-original-title="" title="">
                          </div>
                        </div>
                      </div>
                    </div><div id="step-3" class="content" style="left: 1294.5px; display: none;">
                      <div class="wizard-title">
                        <h2>Sign up to account</h2>
                        <h5 class="text-muted mb-4">Enter your email &amp; password to login</h5>
                      </div>
                      <div class="login-main">
                        <div class="theme-form">
                          <div class="form-group mb-3">
                            <label for="exampleFormControlInput1">Birthday:</label>
                            <input class="form-control" type="date" data-bs-original-title="" title="">
                          </div>
                          <div class="form-group mb-3">
                            <label class="control-label">Age</label>
                            <input class="form-control" placeholder="Age" type="text" data-bs-original-title="" title="">
                          </div>
                          <div class="form-group mb-3">
                            <label class="control-label">Have Passport</label>
                            <input class="form-control" placeholder="Yes/No" type="text" data-bs-original-title="" title="">
                          </div>
                        </div>
                      </div>
                    </div><div id="step-4" class="content" style="left: 1294.5px; display: none;">
                      <div class="wizard-title">
                        <h2>Sign up to account</h2>
                        <h5 class="text-muted mb-4">Enter your email &amp; password to login</h5>
                      </div>
                      <div class="login-main">
                        <div class="theme-form">
                          <div class="form-group mb-3">
                            <label class="control-label">Country</label>
                            <input class="form-control mt-1" type="text" placeholder="Country" required="required" data-bs-original-title="" title="">
                          </div>
                          <div class="form-group mb-3">
                            <label class="control-label">State</label>
                            <input class="form-control mt-1" type="text" placeholder="State" required="required" data-bs-original-title="" title="">
                          </div>
                          <div class="form-group mb-3">
                            <label class="control-label">City</label>
                            <input class="form-control mt-1" type="text" placeholder="City" required="required" data-bs-original-title="" title="">
                            <!-- Smart Wizard Ends-->
                          </div>
                        </div>
                      </div>
                    </div></div><div class="action-bar"><div class="loader">Loading</div><a href="#" class="btn btn-primary" data-bs-original-title="" title="">Finish</a><a href="#" class="btn btn-primary" data-bs-original-title="" title="">Next</a><a href="#" class="btn btn-primary buttonDisabled" data-bs-original-title="" title="">Previous</a><div class="msg-box" style="display: none;"><div class="content">Congratulation ! All step Done.</div><a href="#" class="close"><i class="icofont icofont-close-line-circled"></i></a></div></div></div>
              </div>
            </div>
          </div>
        </div>
        
        
      </div>
</template>