<template>
<Breadcrumbs main="Page Layout" title="Email Compose" />
<!-- Container-fluid starts-->
<div class="container-fluid">
    <div class="email-wrap">
        <div class="row">
            <sidePage />
            <div class="col-xl-9 box-col-12">
              <div class="email-right-aside">
                <div class="card email-body">
                  <div class="row">
                    <div class="col-xl-4 col-md-12 box-md-12 pe-0">
                      <div class="pe-0 b-r-light"></div>
                      <div class="email-top">
                        <div class="row">
                          <div class="col">
                            <h5>Inbox</h5>
                          </div>
                          <div class="col text-end">
                            <div class="dropdown">
                              <button class="btn dropdown-toggle" id="dropdownMenuButton" type="button" data-bs-toggle="dropdown" aria-expanded="false">More</button>
                              <div class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton"><a class="dropdown-item" href="#">Action</a><a class="dropdown-item" href="#">Another action</a><a class="dropdown-item" href="#">Something else here</a></div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="inbox">
                        <div class="media">
                          <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                          <div class="media-body">
                            <h6>Pork Lorn  <small><span>(15</span> July <span>2018)</span></small></h6>
                            <p>Mattis luctus. Donec nisi diam,</p>
                          </div>
                        </div>
                        <div class="media active">
                          <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                          <div class="media-body">
                            <h6>Lorm lpsa  <small><span>(20</span> January)</small></h6>
                            <p>Mattis luctus. Donec nisi diam,</p>
                          </div>
                        </div>
                        <div class="media">
                          <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                          <div class="media-body">
                            <h6>Hileri makr  <small><span>(20</span> Aug<span> 2018)</span></small></h6>
                            <p>Mattis luctus. Donec nisi diam,</p>
                          </div>
                        </div>
                        <div class="media">
                          <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                          <div class="media-body">
                            <h6>Lion Lorpa  <small><span>(02</span> Jun <span>2016)</span></small></h6>
                            <p>Mattis luctus. Donec nisi diam,</p>
                          </div>
                        </div>
                        <div class="media">
                          <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                          <div class="media-body">
                            <h6 class="mt-0">Solvn Relto  <small><span>(25</span> July <span>2015)</span></small></h6>
                            <p>Mattis luctus. Donec nisi diam,</p>
                          </div>
                        </div>
                        <div class="media">
                          <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                          <div class="media-body">
                            <h6>Repro Soft  <small><span>(15</span> July <span>2018)</span></small></h6>
                            <p>Mattis luctus. Donec nisi diam,</p>
                          </div>
                        </div>
                        <div class="media media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt="">
                          <div class="media-body">
                            <h6>Lion Lorpa  <small><span>(02</span> Jun <span>2016)</span></small></h6>
                            <p>Mattis luctus. Donec nisi diam,</p>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="col-xl-8 col-md-12 box-md-12 ps-0">
                      <div class="email-right-aside">
                        <div class="email-body radius-left">
                          <div class="ps-0">
                            <div class="tab-content">
                              <div class="tab-pane fade active show" id="pills-darkhome" role="tabpanel" aria-labelledby="pills-darkhome-tab">
                                <div class="email-compose">
                                  <div class="email-top compose-border">
                                    <div class="row">
                                      <div class="col-sm-8 xl-50">
                                        <h4 class="mb-0">New Message</h4>
                                      </div>
                                      <div class="col-sm-4 btn-middle xl-50">
                                        <button class="btn btn-primary btn-block btn-mail text-center mb-0 mt-0 w-100" type="button"><i class="fa fa-paper-plane me-2"></i> SEND</button>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="email-wrapper">
                                    <form class="theme-form">
                                      <div class="mb-3">
                                        <label class="col-form-label pt-0" for="exampleInputEmail1">To</label>
                                        <input class="form-control" id="exampleInputEmail1" type="email">
                                      </div>
                                      <div class="mb-3">
                                        <label for="exampleInputPassword1">Subject</label>
                                        <input class="form-control" id="exampleInputPassword1" type="text">
                                      </div>
                                      <div>
                                        <label class="text-muted">Message</label>
                                        <ckeditor :editor="editor"  v-model="editorData"></ckeditor>
                                        <!-- <textarea id="text-box" name="text-box" cols="10" rows="2">                                                            </textarea> -->
                                      </div>
                                    </form>
                                  </div>
                                </div>
                              </div>
                              <div class="tab-pane fade" id="pills-darkprofile" role="tabpanel" aria-labelledby="pills-darkprofile-tab">
                                <div class="email-content">
                                  <div class="email-top">
                                    <div class="row">
                                      <div class="col-md-6 xl-100 col-sm-12">
                                        <div class="media"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt="">
                                          <div class="media-body">
                                            <h6>Lorm lpsa  <small><span>(20</span> January) <span>6:00</span> AM</small></h6>
                                            <p>Mattis luctus. Donec nisi diam text.</p>
                                          </div>
                                        </div>
                                      </div>
                                      <div class="col-md-6 col-sm-12 xl-100">
                                        <div class="float-end d-flex">
                                          <p class="user-emailid">Lormlpsa<span>23</span>@company.com</p><i class="fa fa-star-o f-18 mt-1"></i>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="email-wrapper">
                                    <p>Hello</p>
                                    <p>Dear Sir Good Morning,</p>
                                    <h5>Elementum varius nisi vel tempus. Donec eleifend egestas viverra.</h5>
                                    <p class="m-b-20">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non diam facilisis, commodo libero et, commodo sapien. Pellentesque sollicitudin massa sagittis dolor facilisis, sit amet vulputate nunc molestie. Pellentesque maximus nibh id luctus porta. Ut consectetur dui nec nulla mattis luctus. Donec nisi diam, congue vitae felis at, ullamcorper bibendum tortor. Vestibulum pellentesque felis felis. Etiam ac tortor felis. Ut elit arcu, rhoncus in laoreet vel, gravida sed tortor.</p>
                                    <p>In elementum varius nisi vel tempus. Donec eleifend egestas viverra. Donec dapibus sollicitudin blandit. Donec scelerisque purus sit amet feugiat efficitur. Quisque feugiat semper sapien vel hendrerit. Mauris lacus felis, consequat nec pellentesque viverra, venenatis a lorem. Sed urna</p>
                                    <hr>
                                    <div class="d-inline-block">
                                      <h6 class="text-muted"><i class="icofont icofont-clip"></i> ATTACHMENTS</h6><a class="text-muted text-end right-download" href="#"><i class="fa fa-long-arrow-down me-2"></i>Download All</a>
                                      <div class="clearfix"></div>
                                    </div>
                                    <div class="attachment">
                                      <ul class="list-inline">
                                        <li class="list-inline-item"><img class="img-fluid" src="@/assets/images/email/1.jpg" alt=""></li>
                                        <li class="list-inline-item"><img class="img-fluid" src="@/assets/images/email/2.jpg" alt=""></li>
                                        <li class="list-inline-item"><img class="img-fluid" src="@/assets/images/email/3.jpg" alt=""></li>
                                      </ul>
                                    </div>
                                    <hr>
                                    <div class="action-wrapper">
                                      <ul class="actions">
                                        <li><a class="text-muted" href="#"><i class="fa fa-reply me-2"></i>Reply</a></li>
                                        <li><a class="text-muted" href="#"><i class="fa fa-reply-all me-2"></i>Reply All</a></li>
                                        <li><a class="text-muted" href="#"><i class="fa fa-share me-2"></i></a>Forward</li>
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
            <!-- <div class="col-xl-9 box-col-12">
                <div class="email-right-aside">
                    <div class="card email-body">
                        <div class="row">
                            <div class="col-xl-4 col-md-12 box-md-12 pe-0">
                                <div class="pe-0 b-r-light"></div>
                                <div class="email-top">
                                    <div class="row">
                                        <div class="col">
                                            <h5>Inbox</h5>
                                        </div>
                                        <div class="col text-end">
                                            <div class="dropdown">
                                                <button class="btn dropdown-toggle" id="dropdownMenuButton" type="button" data-bs-toggle="dropdown" aria-expanded="false">More</button>
                                                <div class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton"><a class="dropdown-item" href="#">Action</a><a class="dropdown-item" href="#">Another action</a><a class="dropdown-item" href="#">Something else here</a></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="inbox">
                                    <div class="media">
                                        <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                                        <div class="media-body">
                                            <h6>Pork Lorn <small><span>(15</span> July <span>2018)</span></small></h6>
                                            <p>Mattis luctus. Donec nisi diam,</p>
                                        </div>
                                    </div>
                                    <div class="media active">
                                        <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                                        <div class="media-body">
                                            <h6>Lorm lpsa <small><span>(20</span> January)</small></h6>
                                            <p>Mattis luctus. Donec nisi diam,</p>
                                        </div>
                                    </div>
                                    <div class="media">
                                        <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                                        <div class="media-body">
                                            <h6>Hileri makr <small><span>(20</span> Aug<span> 2018)</span></small></h6>
                                            <p>Mattis luctus. Donec nisi diam,</p>
                                        </div>
                                    </div>
                                    <div class="media">
                                        <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                                        <div class="media-body">
                                            <h6>Lion Lorpa <small><span>(02</span> Jun <span>2016)</span></small></h6>
                                            <p>Mattis luctus. Donec nisi diam,</p>
                                        </div>
                                    </div>
                                    <div class="media">
                                        <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                                        <div class="media-body">
                                            <h6 class="mt-0">Solvn Relto <small><span>(25</span> July <span>2015)</span></small></h6>
                                            <p>Mattis luctus. Donec nisi diam,</p>
                                        </div>
                                    </div>
                                    <div class="media">
                                        <div class="media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt=""></div>
                                        <div class="media-body">
                                            <h6>Repro Soft <small><span>(15</span> July <span>2018)</span></small></h6>
                                            <p>Mattis luctus. Donec nisi diam,</p>
                                        </div>
                                    </div>
                                    <div class="media media-size-email"><img class="me-3 rounded-circle" src="@/assets/images/user/user.png" alt="">
                                        <div class="media-body">
                                            <h6>Lion Lorpa <small><span>(02</span> Jun <span>2016)</span></small></h6>
                                            <p>Mattis luctus. Donec nisi diam,</p>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="email-profile">
                            </div>
                            <div class="email-body">
                                <div class="email-compose">
                                    <div class="email-top compose-border">
                                        <div class="compose-header">
                                            <h4 class="mb-0">New Message</h4>
                                            <button class="btn btn-primary" type="button"><i class="fa fa-file me-2"></i> save</button>
                                        </div>
                                    </div>
                                    <div class="email-wrapper">
                                        <form class="theme-form">
                                            <div class="form-group">
                                                <label class="col-form-label pt-0" for="exampleInputEmail1">To</label>
                                                <input class="form-control" id="exampleInputEmail1" type="email">
                                            </div>
                                            <div class="form-group">
                                                <label for="exampleInputPassword1">Subject</label>
                                                <input class="form-control" id="exampleInputPassword1" type="text">
                                            </div>
                                            <div class="form-group">
                                                <label>Message</label>
                                                <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>

                                            </div>
                                            <div class="form-group">
                                                <div class="dropzone digits text-center" id="singleFileUpload" action="/upload.php">
                                                    <div class="dz-message needsclick"><i class="icon-cloud-up"></i>

                                                        <DropZone :maxFileSize="Number(60000000)" url="http://localhost:8080" :uploadOnDrop="true" :multipleUpload="true" :parallelUpload="2" />
                                                        <h4>Drop files here or click to upload.</h4><span class="note needsclick">(This is just a demo dropzone. Selected files are <strong>not</strong> actually uploaded.)</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </form>
                                        <div class="action-wrapper">
                                            <ul class="actions">
                                                <li><a class="btn btn-secondary" href="email_read.html"><i class="fa fa-paper-plane me-2"></i>send </a></li>
                                                <li><a class="btn btn-danger" href="index.html"> <i class="fa fa-times me-2"></i>cancel</a></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div> -->
        </div>
    </div>
</div>
<!-- Container-fluid Ends-->
</template>

<script>
// import { useDropzone } from "vue3-dropzone";

import sidePage from '../sidePage.vue'
import CKEditor from '@ckeditor/ckeditor5-vue';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
export default {
    name: 'composeView',
    components: {
        sidePage,
        ckeditor: CKEditor.component
    },
    data() {
        return {
            type: 'inbox',
            editor: ClassicEditor,
            editorData: '<p>Content of the editor.</p>',
            // editorConfig: {
            //     config: {
            //         height: '300px'
            //     }
            // },
            menutoogle: false,
        };
    },
    //     setup() {
    //     function onDrop(acceptFiles, rejectReasons) {
    //       console.log(acceptFiles);
    //       console.log(rejectReasons);
    //     }

    //     const { getRootProps, getInputProps, ...rest } = useDropzone({ onDrop });

    //     return {
    //       getRootProps,
    //       getInputProps,
    //       ...rest,
    //     };
    //   },
}
</script>
