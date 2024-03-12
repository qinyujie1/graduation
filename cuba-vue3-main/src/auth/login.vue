<template>
  <div>
    <!-- page-wrapper Start-->
    <div class="container-fluid">
      <div class="row ">
        <div class="col-12 p-0">
          <div class="login-card">
            <div>
              <div>
                <a class="logo">
                  <img
                    class="img-fluid for-light"
                    src="../assets/images/logo/logo.png"
                    alt="looginpage"
                  />
                  <img
                    class="img-fluid for-dark"
                    src="../assets/images/logo/logo_dark.png"
                    alt="looginpage"
                  />
                </a>
              </div>
              <div class="login-main">
                <form class="theme-form">
                  <h4>Sign in to account</h4>
                  <p>Enter your email & password to login</p>
                  <div class="form-group">
                    <label class="col-form-label">Email Address</label>
                    <input class="form-control" type="email" required="" placeholder="Test@gmail.com" v-model="user.email.value">
                    <span class="validate-error" v-if="!user.email.value || !validEmail(user.email.value) ">{{ user.email.errormsg }}</span>

                  </div>
                  <div class="form-group">
                    <label class="col-form-label">Password</label>
                    <div class="form-input position-relative">
                      <input class="form-control" type="password" name="login[password]" required="" placeholder="*********" v-model="user.password.value">
                      <span class="validate-error" v-if="user.password.value.length < 7">{{ user.password.errormsg }}</span>
                      
                      <div class="show-hide"><span class="show">                         </span></div>
                    </div>
                  </div>
                  <div class="form-group mb-0">
                    <div class="checkbox p-0">
                      <input id="checkbox1" type="checkbox">
                      <label class="text-muted" for="checkbox1">Remember password</label>
                    </div><a class="link" href="forget-password.html">Forgot password?</a>
                    <div class="text-end mt-3">
                      <button class="btn btn-primary btn-block w-100" type="submit" @click.prevent="login">Sign in</button>
                    </div>
                  </div>
                  <h6 class="text-muted mt-4 or">Or Sign in with</h6>
                  <div class="social mt-4">
                    <div class="btn-showcase"><a class="btn btn-light" href="https://www.linkedin.com/login" target="_blank"><i class="txt-linkedin" data-feather="linkedin"></i> LinkedIn </a><a class="btn btn-light" href="https://twitter.com/login?lang=en" target="_blank"><i class="txt-twitter" data-feather="twitter"></i>twitter</a><a class="btn btn-light" href="https://www.facebook.com/" target="_blank"><i class="txt-fb" data-feather="facebook"></i>facebook</a></div>
                  </div>
                  <p class="mt-4 mb-0 text-center">Don't have account?<a class="ms-2" href="sign-up.html">Create Account</a></p>
                </form>
                <!-- <b-card no-body>
                  <b-tabs pills vertical>
                    <b-tab active>
                      <template #title>
                        <img
                          src="../assets/images/login/firebase.svg"
                          id="firebase-tooltip"
                        />
                        <span>Firebase Login</span>
                      </template>
                      <b-card-text>
                        <form class="theme-form">
                          <h4>Sign in to account</h4>
                          <p>Enter your email & password to login</p>
                          <div class="form-group">
                            <label class="col-form-label">Email Address</label>
                            <input
                              v-model="email"
                              class="form-control"
                              type="email"
                              required=""
                              placeholder="Test@gmail.com"
                              :class="{
                                'is-invalid': submitted && !email,
                              }"
                            />
                            <div
                              v-show="submitted && !email"
                              class="invalid-feedback"
                            >
                              Email is required
                            </div>
                          </div>
                          <div class="form-group">
                            <label class="col-form-label">Password</label>
                            <input
                              v-model="password"
                              autocomplete=""
                              class="form-control"
                              :type="type"
                              name="login[password]"
                              required=""
                              placeholder="*********"
                              :class="{
                                'is-invalid': submitted && !email,
                              }"
                            />
                            <div
                              v-show="submitted && !password"
                              class="invalid-feedback"
                            >
                              Email is required
                            </div>
                            <div class="show-hide" @click="showPassword">
                              <span class="show"></span>
                            </div>
                          </div>
                          <div class="form-group mb-0">
                            <div class="checkbox p-0">
                              <input id="checkbox1" type="checkbox" />
                              <label class="text-muted" for="checkbox1"
                                >Remember password</label
                              >
                            </div>
                            <button
                              class="btn btn-primary btn-block"
                              type="button"
                              @click="signUp"
                            >
                              Login
                            </button>
                          </div>
                          <h6 class="text-muted mt-4 or">Or Sign in with</h6>
                          <div class="social mt-4">
                            <div class="btn-showcase">
                              <a class="btn btn-light" @click="socialLogin">
                                <i class="fa fa-google txt-linkedin"></i>
                                Google
                              </a>
                              <a
                                class="btn btn-light"
                                @click="socialLoginTwitter"
                              >
                                <feather
                                  type="twitter"
                                  class="txt-twitter"
                                ></feather
                                >twitter</a
                              >
                              <a
                                class="btn btn-light"
                                @click="socialLoginFacebook"
                              >
                                <feather
                                  type="facebook"
                                  class="txt-fb"
                                ></feather
                                >facebook</a
                              >
                            </div>
                          </div>
                          <p class="mt-4 mb-0">
                            Don't have account?
                            <router-link
                              class="ms-2"
                              tag="a"
                              to="/auth/register"
                            >
                              Create Account
                            </router-link>
                          </p>
                        </form>
                      </b-card-text>
                    </b-tab>
                    <b-tab>
                      <template #title>
                        <img src="../assets/images/login/auth0.svg" />
                        <span>Auth0</span>
                      </template>
                      <b-card-text>
                        <form class="theme-form">
                          <img src="../assets/images/login/auth-img.svg" />
                          <h4>Sign in to Auth0 account</h4>
                          <p>
                            Lorem Ipsum is simply dummy text of the printing and
                            typesetting industry. Lorem Ipsum has been the
                            industry's standard dummy.
                          </p>
                          <div class="form-group mt-3 mb-0">
                            <button
                              @click="login"
                              class="btn btn-secondary btn-block"
                              type="button"
                            >
                              Login With Auth0
                            </button>
                          </div>
                          <p class="mt-4 mb-0">
                            Don't have account?<router-link
                              class="ms-2"
                              tag="a"
                              to="/auth/register"
                            >
                              Create Account
                            </router-link>
                          </p>
                        </form>
                      </b-card-text>
                    </b-tab>
                    <b-tab>
                      <template #title>
                        <img src="../assets/images/login/jwt.svg" />
                        <span>JWT</span>
                      </template>
                      <b-card-text>
                        <div class="alert alert-info">
                          Username: test<br />
                          Password: test
                        </div>
                        <form class="theme-form" @submit.prevent="handleSubmit">
                          <div class="form-group">
                            <label for="username">Username</label>
                            <input
                              type="text"
                              v-model="username"
                              name="username"
                              class="form-control"
                              :class="{ 'is-invalid': submitted && !username }"
                            />
                            <div
                              v-show="submitted && !username"
                              class="invalid-feedback"
                            >
                              Username is required
                            </div>
                          </div>
                          <div class="form-group">
                            <label htmlFor="password">Password</label>
                            <input
                              type="password"
                              v-model="passwordjwt"
                              name="password"
                              class="form-control"
                              :class="{
                                'is-invalid': submitted && !passwordjwt,
                              }"
                            />
                            <div
                              v-show="submitted && !passwordjwt"
                              class="invalid-feedback"
                            >
                              Password is required
                            </div>
                          </div>
                          <div class="form-group mt-3 mb-0">
                            <button
                              class="btn btn-primary btn-block"
                              :disabled="loggingIn"
                            >
                              Login
                            </button>
                          </div>
                          <p class="mt-4 mb-0">
                            Don't have account?
                            <router-link
                              class="ms-2"
                              tag="a"
                              to="/auth/register"
                            >
                              Create Account
                            </router-link>
                          </p>
                        </form>
                      </b-card-text>
                    </b-tab>
                  </b-tabs>
                </b-card> -->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- latest jquery-->
  </div>
</template>

<script>
  // import firebase from 'firebase';
  // import Userauth from '../auth/js/index';
  
  export default {
    name: 'login',
    data() {
      return {
        // type: 'password',
        // email: 'test@admin.com',
        // password: 'test@123456',
        // username: '',
        // passwordjwt: '',
        // submitted: false,
        result: {email:'',password:''},
            // logintitle: 'Login',
            // registertitle: 'New Customer',
            user: {
                email: {
                    value: 'test@admin.com',
                    errormsg: ''
                },
                password: {
                    value: 'test@123456',
                    errormsg: ''
                }
            }
      };
    },
    // computed: {
    //   // JWT authentication
    //   loggingIn() {
    //     return this.$store.state.authentication.status.loggingIn;
    //   },
    // },
    created() {
      // reset login status for JWT
      // this.$store.dispatch('authentication/logout');
    },
    methods: {
      // JWT authentication
      // handleSubmit() {
      //   this.submitted = true;
      //   const { username, passwordjwt } = this;
      //   const { dispatch } = this.$store;
      //   if (username && passwordjwt) {
      //     dispatch('authentication/login', { username, passwordjwt });
      //   }
      // },
      // // show/hide password
      // showPassword: function() {
      //   if (this.type === 'password') {
      //     this.type = 'text';
      //   } else {
      //     this.type = 'password';
      //   }
      // },
      // // Firebase login
      // signUp: function() {
      //   this.submitted = true;
      //   if (this.email === '' && this.password === '') {
      //     (this.email = 'test@admin.com'), (this.password = 'test@123456');
      //   } else {
      //     firebase
      //       .auth()
      //       .signInWithEmailAndPassword(this.email, this.password)
      //       .then(
      //         (result) => {
      //           Userauth.localLogin(result);
      //           this.$router.replace('/');
      //         },
      //         (err) => {
      //           (this.email = 'test@admin.com'), (this.password = 'test@123456');
      //           this.$toasted.show('Oops...' + err.message, {
      //             theme: 'bubble',
      //             position: 'bottom-right',
      //             type: 'error',
      //             duration: 2000,
      //           });
      //         }
      //       );
      //   }
      // },
      // // Social login
      // socialLogin() {
      //   const provider = new firebase.auth.GoogleAuthProvider();
      //   firebase
      //     .auth()
      //     .signInWithPopup(provider)
      //     .then((result) => {
      //       Userauth.localLogin(result);
      //       this.$router.replace('/');
      //     })
      //     .catch((err) => {
      //       alert('Oops. ' + err.message);
      //     });
      // },
      // socialLoginFacebook() {
      //   const provider = new firebase.auth.FacebookAuthProvider();
      //   firebase
      //     .auth()
      //     .signInWithPopup(provider)
      //     .then((result) => {
      //       Userauth.localLogin(result);
      //       this.$router.replace('/');
      //     })
      //     .catch((err) => {
      //       alert('Oops. ' + err.message);
      //     });
      // },
      // socialLoginTwitter() {
      //   const provider = new firebase.auth.TwitterAuthProvider();
      //   firebase
      //     .auth()
      //     .signInWithPopup(provider)
      //     .then((result) => {
      //       Userauth.localLogin(result);
      //       this.$router.replace('/');
      //     })
      //     .catch((err) => {
      //       alert('Oops. ' + err.message);
      //     });
      // },
      // socialLoginGit() {
      //   const provider = new firebase.auth.GithubAuthProvider();
      //   firebase
      //     .auth()
      //     .signInWithPopup(provider)
      //     .then((result) => {
      //       Userauth.localLogin(result);
      //       this.$router.replace('/');
      //     })
      //     .catch((err) => {
      //       alert('Oops. ' + err.message);
      //     });
      // },
      // Auth0 login
      // login() {
      //   // Userauth.login();
      //   if (this.email === '' && this.password === '') {
      //     (this.email = 'test@admin.com'), (this.password = 'test@123456');
      //   } 
      //   else{
      //     this.$router.replace('/');
      //   }
      // },
      login() {
            if (!this.user.password.value || this.user.password.value.length < 7) {
                this.user.password.errormsg = 'min length 7'
            }else{this.user.password.errormsg = ''}
            if (!this.user.email.value) {
                this.user.email.errormsg = 'empty not allowed'
            } else if (!this.validEmail(this.user.email.value)) {
              this.user.email.errormsg = 'Valid email required.'}
            else{
              this.user.email.errormsg=''
            }
             if(!this.user.email.errormsg && !this.user.password.errormsg && this.user.email.value != 'test@admin.com' || this.user.password.value != 'test@123456'){
                // useNuxtApp().$showToast({msg:"enter valid email and password",type:"info"})
                alert("wrong credenstials")
            }
            if(!this.user.email.errormsg && !this.user.password.errormsg && this.user.email.value == 'test@admin.com' && this.user.password.value== 'test@123456'){

                this.result ={email:this.user.email.value, password:this.user.password.value}
              //   Userauth.localLogin(this.result)
              //   if(this.cart.length>0){
              // this.$router.replace('/page/account/checkout')}
              localStorage.setItem('User',JSON.stringify({email:this.user.email.value,useer:true}))
              
              this.$router.push('/')
            }
          },
        validEmail: function (email) {
            const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            return re.test(email)
        }
    },
  };
</script>
