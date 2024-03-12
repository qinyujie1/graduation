<template>
  <Breadcrumbs main="Page Layout" title="Email Application" />
    <!-- Container-fluid starts-->
        <div class="container-fluid">
          <div class="email-wrap">
            <div class="row">
              <sidePage/>
              <div class="col-xl-9 col-md-12 xl-70 box-col-70">
                <div class="email-right-aside">
                  <div class="card email-body">
                    <div class="email-profile">                                                                     
                      <div class="email-right-aside">
                        <div class="email-body">
                          <div class="email-content">
                            <div class="email-top">
                              <div class="row">
                                <div class="col-xl-12">
                                  <div class="d-flex"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt="">
                                    <div class="flex-grow-1">
                                      <h6 class="d-block">Lorm lpsa</h6>
                                      <p>Mattis luctus. Donec nisi diam text.</p>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="email-wrapper">
                              <div class="emailread-group">
                                <div class="read-group">
                                  <p>Hello</p>
                                  <p>Dear Sir Good Morning,</p>
                                </div>
                                <div class="read-group">
                                  <h3>Elementum varius nisi vel tempus. Donec eleifend egestas viverra.</h3>
                                  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non diam facilisis, commodo libero et, commodo sapien. Pellentesque sollicitudin massa sagittis dolor facilisis, sit amet vulputate nunc molestie. Pellentesque maximus nibh id luctus porta. Ut consectetur dui nec nulla mattis luctus. Donec nisi diam, congue vitae felis at, ullamcorper bibendum tortor. Vestibulum pellentesque felis felis. Etiam ac tortor felis. </p>
                                  <p class="m-t-10">In elementum varius nisi vel tempus. Donec eleifend egestas viverra. Donec dapibus sollicitudin blandit. Donec scelerisque purus sit amet feugiat efficitur. Quisque feugiat semper sapien vel hendrerit. Mauris lacus felis, consequat nec pellentesque viverra, venenatis a lorem. Sed urna</p>
                                </div>
                              </div>
                              <div class="emailread-group">
                                <h6 class="text-muted mb-0"><i class="icofont icofont-clip"></i> ATTACHMENTS</h6><a class="text-muted text-end right-download font-primary f-w-600" href="javascript:void(0)"><i class="fa fa-long-arrow-down me-2"></i>Download All</a>
                                <div class="clearfix"></div>
                                <div class="attachment">
                                  <ul>
                                    <li><img class="img-fluid" src="@/assets/images/email/1.jpg" alt=""></li>
                                    <li><img class="img-fluid" src="@/assets/images/email/2.jpg" alt=""></li>
                                    <li><img class="img-fluid" src="@/assets/images/email/3.jpg" alt=""></li>
                                  </ul>
                                </div>
                              </div>
                              <div class="emailread-group">
                                <textarea class="form-control" rows="4" cols="50" placeholder="write about your nots"></textarea>
                                <div class="action-wrapper">
                                  <ul class="actions">
                                    <li><a class="btn btn-primary" href="javascript:void(0)"><i class="fa fa-reply me-2"></i>Reply</a></li>
                                    <li><a class="btn btn-secondary" href="javascript:void(0)"><i class="fa fa-reply-all me-2"></i>Reply All</a></li>
                                    <li><a class="btn btn-danger" href="javascript:void(0)"><i class="fa fa-share me-2"></i>Forward</a></li>
                                  </ul>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Container-fluid Ends-->
      
</template>
<script>
import sidePage from '../sidePage'
export default{
    name:'readMail',
    components:{
        sidePage
    }
}
</script>
