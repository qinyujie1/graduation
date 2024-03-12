import { createWebHistory, createRouter } from "vue-router";
import Body from '../components/body';
import Auth from '../auth/auth';

/* Dashboards */
import Default from '../pages/dashboard/default';
import Ecommerce from '../pages/dashboard/ecommerce';
import Online from  '../pages/dashboard/online'
import Crypto from '../pages/dashboard/crypto'
import Social from '../pages/dashboard/social.vue'
// Widgets
import General from '../pages/widgets/general'
import Chart from '../pages/widgets/chart'
// pageLayout
import indexBoxed from '../pages/pageLayout/boxed/indexBoxed.vue'
import indexRTL from '../pages/pageLayout/RTL/indexRTL.vue'
import indexDarklayout from '../pages/pageLayout/darklayout/indexDarklayout.vue'
import indexFooterdark from '../pages/pageLayout/footerdark/indexFooterdark.vue'
import indexFooterfixed from '../pages/pageLayout/footerfixed/indexFooterfixed.vue'
import indexFooterlight from '../pages/pageLayout/footerlight/indexFooterlight.vue'
import indexHidenavscroll from '../pages/pageLayout/hidenavscroll/indexHidenavscroll.vue'
// project
import createProject from '../pages/project/createproject/createProject.vue'
import indexList from '../pages/project/projectlist/indexList.vue'
/* File Manager  */
import FileManager from '../pages/filemanager';
// kanban
import Kanban from '../pages/kanban/indexKanban.vue'
// ecoomerce
import indexProduct from '../pages/ecommerce/product/indexProduct.vue'
import productPage from '../pages/ecommerce/productpage/productPage.vue'
import productList from '../pages/ecommerce/list/productList.vue'
import paymentDetails from '../pages/ecommerce/payment/details/paymentDetails.vue'
import orderHistory from '../pages/ecommerce/order/history/orderHistory.vue'
import invoiceView from '../pages/ecommerce/invoice/invoiceView.vue'
import cartView from '../pages/ecommerce/cart/cartView.vue'
import wishlistView from '../pages/ecommerce/wishlist/wishlistView.vue'
import checkoutView from '../pages/ecommerce/checkout/checkoutView.vue'
import pricingView from '../pages/ecommerce/pricing/pricingView.vue'
// mail
import readMail from '../pages/email/readMail/readMail.vue'
import composeView from '../pages/email/compose/composeView.vue'
// chat
import chatApp from '../pages/chat/chatApp/chatApp.vue'
import videoChat from '../pages/chat/videoChat/videoChat copy.vue'
// user
import userProfile from '../pages/users/profile/userProfile.vue'
import userCards from '../pages/users/cards/userCards.vue'
import userEdit from '../pages/users/edit/userEdit.vue'
// forms
import formValidation from "../pages/forms/formValidetion/formValidation"
import base_Input from "../pages/forms/baseInput/base_Input"
import checkbox_radio from "../pages/forms/Checkbox&Radio/checkbox_radio"
import input_groups from "../pages/forms/InputGroup/input_groups"
import megaOptions from "../pages/forms/megaOptions/megaOptions"

// form widgets
import select2 from "../pages/formWidgets/select2/select2Page.vue"
import switch_From from "../pages/formWidgets/switch/switch_From"
import touchspin_Form from "../pages/formWidgets/touchspin/touchspin_Form"
import typeahead_Form from "../pages/formWidgets/typeahead/typeahead_Form"
import clipboard_Form from "../pages/formWidgets/clipboard/clipboard_Form"
import datepicker from "../pages/formWidgets/datepicker/datePicker.vue"
import timepicker from "../pages/formWidgets/timepicker/timePicker.vue"
import datetimepicker from "../pages/formWidgets/datetimepicker/dateTimePicker.vue"
import daterangepicker from "../pages/formWidgets/datetimerange/dateTimeRange.vue"
// form layput
import defaultforms from '../pages/formLayout/default/defaultFotrm.vue'
import form_wizard2 from "../pages/formLayout/formWizrd2/form_wizard.vue"
import form_wizard1 from '../pages/formLayout/formWizard1/form_wizard2.vue'
import form_wizard3 from "../pages/formLayout/formWizard3/form_wizard1.vue"

// uikits
import Scrollable from "../pages/advance/scollable/scrollable_advance.vue";
import Sweetalert from "../pages/advance/sweetalert/sweetAert.vue";
import Tree from "../pages/advance/tree/treeView.vue";
import Rating from "../pages/advance/rating/ratingView.vue";
import Pagination from "../pages/advance/pagination/pagination_advance.vue";
import Ribbons from "../pages/advance/ribbons/ribbons_advance.vue";
import Tour from "../pages/advance/tour/tourView.vue";

import Breadcrumb from "../pages/advance/breadcrumbs/breadCrumb.vue";

import Sticky from "../pages/advance/sticky/stickyView.vue";

import ImageCropper from "../pages/advance/image_cropper/cropper_advance.vue";
import Notify from '../pages/advance/notify/toaster_advance.vue'
import dropzone from '../pages/advance/dropzone/dropzoneView.vue';
import animatedModal from '../pages/advance/animatedModal/animatedModal.vue'
import owlCarousel from '../pages/advance/owlCarousel/owlCarousel.vue' 
import Rangeslider from '../pages/advance/range/rangeView.vue'
import BasicCard from '../pages/advance/basicCard/basicCard.vue'
import CreativeCard from '../pages/advance/creativeCard/creative_card.vue'
import DraggableCard from '../pages/advance/draggableCard/draggableCard.vue'
import TabbedCard from '../pages/advance/tabbedCard/tabbed_card.vue'
import timeLine from '../pages/advance/timeLine/timeLine.vue'
import timeLine2 from '../pages/advance/timeLine/timeLine2.vue'
/* FAQ */
import Faq from '../pages/faq/faqIndex.vue';
// uikits
import alert from '../pages/uikits/alert';
import Helperclasses from '../pages/uikits/helper_classes';
import Avatars from '../pages/uikits/avatars';
import Grid from '../pages/uikits/grid';
import Tagpills from '../pages/uikits/tag_pills';
import Typography from '../pages/uikits/typography';
import Progressbar from '../pages/uikits/progress_bar';
import Modal from '../pages/uikits/modal';
import Popover from '../pages/uikits/popover';
import Tooltip from '../pages/uikits/tooltip';
import Spinners from '../pages/uikits/loader';
import Dropdown from '../pages/uikits/dropdown';
import Accordion from '../pages/uikits/accordion';
import Boxshadow from '../pages/uikits/box_shadow';
import Lists from '../pages/uikits/lists';
import bootstraptabPage from "../pages/uikits/tabs/bootstraptab/bootstraptabPage.vue";
import linetabPage from "../pages/uikits/tabs/linetab/linetabPage.vue";
// animation
import animate from '../pages/animation/animate/animatePage.vue'
import aos from '../pages/animation/aos/aosPage.vue'
import scroll from '../pages/animation/scroll/scrollPage.vue'
// import tilt from '../pages/animation/tilt/tiltPage.vue'
import wow from '../pages/animation/wow/wowPage.vue'
import tilt from '../pages/animation/tilt.vue'
// builder
import form1 from '../pages/builder/formBuilder1.vue'
import form2 from '../pages/builder/formBuilder2.vue'
/* icons */
import Flag from '../pages/icons/flag';
import Ico from '../pages/icons/ico_icon';
import Themify from '../pages/icons/themify_icon';
import Fontawesome from '../pages/icons/font_awesome';
import FeatherIcon from '../pages/icons/feather_icon';
import WhetherIcon from '../pages/icons/weather';
/* Buttons */
import Default_buttons from '../pages/button/Default/default_button.vue';
import Flat_buttons from '../pages/button/Flat/flat_button.vue';
import Edge_buttons from '../pages/button/Edge/edge_button.vue';
import Raised_buttons from '../pages/button/Raised/raised_button.vue';
import Group_buttons from '../pages/button/ButtonGroup/button_group.vue'; 
/*charts*/ 
import google_chart from "../pages/charts/googleChart/google_chart"
import apex_chart from "../pages/charts/ApexChart/apex_chart"
// import sparkline from "../pages/charts/sparkline/sparklinePage.vue"
 import chartist_chart from "../pages/charts/chartist/chartist_chart.vue"
// knowledge
import knowledge from '../pages/Knowledgebase/index.vue'
import category_knowledge from '../pages/Knowledgebase/categoryKnowledge.vue'
import detail_knowledge from '../pages/Knowledgebase/detailsKnowledge.vue' 
// error
import Error400 from '../pages/error/error400';
import Error401 from '../pages/error/error401';
import Error403 from '../pages/error/error403';
import Error404 from '../pages/error/error404';
import Error500 from '../pages/error/error500';
import Error503 from '../pages/error/error503';

/* Support Ticket */
import Support from '../pages/support';

/* Editor */
import SimpleEditor from '../pages/editor/simple_editor';
import CkEditor from '../pages/editor/ckeditor.vue';
/* Maps */
import GoogleMaps from '../pages/maps/google_map.vue';
import VueLeaflet from '../pages/maps/vue_leaflet.vue';
// learning
import learning_list from "../pages/learning/learninglist/learning_list"
import coursedetailed from "../pages/learning/courseDetailed"
// job Search
import job_list from "../pages/job/job-list/job_list"
import job_details from "../pages/job/job_details/job_details"
import job_apply from "../pages/job/job_apply/job_apply"
import job_card from "../pages/job/job_card/cardJob.vue"
// blog
import blog_detail from "../pages/blog/blog-details/blog_detail"
import blog_single from "../pages/blog/blog-single/blog_single"
import blog_add from "../pages/blog/blog-add/addBlog.vue"
// GALLERY
import grid_gallery from "../pages/gallery/grid_gallery"
import grid_desc from "../pages/gallery/grid_desc"
import hover_gallery from "../pages/gallery/hover-gallery/hover_gallery"
import masonry_gallery from "../pages/gallery/masonry-gallery/masonry_gallery"
import masonary_desc from "../pages/gallery/masonary_desc.vue"
/* Authentication */
import LoginOne from '../pages/authentication/login_one';
import LoginTwo from '../pages/authentication/login_two';
import LoginValidate from '../pages/authentication/login_validation.vue';
import LoginTooltip from '../pages/authentication/login_tooltip.vue'
import LoginSweetalert from '../pages/authentication/login_sweetalert.vue'

import RegisterImage from '../pages/authentication/register_image';
import RegisterImage2 from '../pages/authentication/register_image2';
import RegisterWizard from '../pages/authentication/register_wizard.vue'
import Unlock from '../pages/authentication/unlock';
import ForgetPassword from '../pages/authentication/forget_password';
import ResetPassword from '../pages/authentication/reset_password';
import Maintenance from '../pages/authentication/maintenance.vue'
/* Auth */
import login from '../auth/login';
import Register from '../auth/register';
// comingsoon
import ComingsoonImage from '../pages/comingsoon/comingsoon_image';
import ComingsoonSimple from '../pages/comingsoon/comingsoon_simple';
import ComingsoonVideo from '../pages/comingsoon/comingsoon_video';
// SAMPLE PAGE
import sample_page from "../pages/sample_page"
/* bootstrap tables */
import BootstrapBasic from "../pages/tables/bootstrapTable/basicTables/basic_tables.vue";
import tableComponent from "../pages/tables/bootstrapTable/stylingtable/styling_table.vue"
import DatatableBasic from "../pages/tables/dataTable/BasicInit/basic_Init.vue"
// searchPage
import serchIndex from "../pages/search/serchIndex.vue"
// bookmark
import Bookmark from "../pages/bookmark/bookMark.vue"
// contact 
import contactView from "../pages/contact/contactView.vue"
// task
import Task from "../pages/task/indexPage.vue"
// calendar
import Calendar from "../pages/calenderView.vue"
// social app
import socialPage from "../pages/socialApp/socialApp.vue"
// todo
import Todo from "../pages/todo/index.vue"
const routes = [
    {
        path: '/',
        component: Body,
    
        children: [
          {
            path: '',
            name: 'defaultRoot',
            component: Default,
          },
    
        ]
      },
    {
        path: '/dashboard',
        component: Body,
        meta: {
          requiresAuth: true
        },
        children: [
        {
          path: 'default',
          name: 'default',
          component: Default,
          meta: {
            title: 'Default Dashboard | Cuba - Premium Admin Template',
          }
        },
        {
          path: 'ecommerce',
          name: 'ecommerce',
          component: Ecommerce,
          meta: {
            title: 'Ecommerce Dashboard | Cuba - Premium Admin Template',
          }
        },
        {
          path: 'online',
          name: 'online',
          component: Online,
          meta: {
            title: 'Online Dashboard | Cuba - Premium Admin Template',
          }
        },
        {
          path: 'crypto',
          name: 'crypto',
          component: Crypto,
          meta: {
            title: 'Crypto Dashboard | Cuba - Premium Admin Template',
          }
        },
        {
          path: 'social',
          name: 'social',
          component: Social,
          meta: {
            title: 'Social Dashboard | Cuba - Premium Admin Template',
          }
        }
        ]
      },
      {
        path: '/widgets',
        component: Body,
        meta: {
          requiresAuth: true
        },
        children: [
        {
          path: 'general',
          name: 'general',
          component: General,
          meta: {
            title: 'general Dashboard | Cuba - Premium Admin Template',
          }
        },
        {
          path: 'chart',
          name: 'chart',
          component: Chart,
          meta: {
            title: 'chart Dashboard | Cuba - Premium Admin Template',
          }
        },
        ]
      },
      {
        path: '/pageLayout',
        component: Body,
        children: [
          {
            path: 'boxed',
            name: 'boxed',
            component: indexBoxed
          },
          {
            path: 'darklayout',
            name: 'darklayout',
            component: indexDarklayout
          }
          ,
          {
            path: 'footerdark',
            name: 'footerdark',
            component: indexFooterdark
          }
          ,
          {
            path: 'footerlight',
            name: 'footerlight',
            component: indexFooterlight
          }
          ,
          {
            path: 'footerfixed',
            name: 'footerfixed',
            component: indexFooterfixed
          }
          ,
          {
            path: 'hidenavscroll',
            name: 'hidenavscroll',
            component: indexHidenavscroll
          }
          ,
          {
            path: 'RTL',
            name: 'RTL',
            component: indexRTL
          }
        ]
      },
      {
        path: '/project',
        component: Body,
        children: [
          {
            path: 'projectlist',
            name: 'projectlist',
            component: indexList
          },
          {
            path: 'create-project',
            name: 'createProject',
            component: createProject
          }
        ]
      },
      {
        path: '/app',
        component: Body,
        children: [
          {
            path: 'socialPage',
            name: 'socialPage',
            component: socialPage,
             meta: {
                title: 'Social App, | Cuba - Premium Admin Template',
              }
          },
        {
          path: 'todo',
          name: 'todo',
          component: Todo,
           meta: {
              title: 'Todo | Cuba - Premium Admin Template',
            }
        },
        // {
        //   path: 'firebase-todo',
        //   name: 'FirebaseTodo',
        //   component: FirebaseTodo,
        //    meta: {
        //       title: 'FirebaseTodo | Cuba - Premium Admin Template',
        //     }
        // },
        {
          path: 'chat',
          name: 'chat',
          component: chatApp,
           meta: {
              title: 'Chat | Cuba - Premium Admin Template',
            }
        },
        {
          path: 'videochat',
          name: 'Video chat',
          component: videoChat,
           meta: {
              title: 'Video Chat | Cuba - Premium Admin Template',
            }
        },
        // {
        //   path: 'email',
        //   name: 'Email',
        //   component: Email,
        //    meta: {
        //       title: 'Email, | Cuba - Premium Admin Template',
        //     }
        // },
        {
          path: 'filemanager',
          name: 'File Manager',
          component: FileManager,
           meta: {
              title: 'File Manager, | Cuba - Premium Admin Template',
            }
        },
        {
          path: 'kanban',
          name: 'Kanban Board',
          component: Kanban,
           meta: {
              title: 'Kanban Board, | Cuba - Premium Admin Template',
            }
        },
        {
          path: 'contact',
          component: contactView,
          name: 'contactView'
        },
        {
          path:'bookmark',
          name:'Bookmark',
          component:Bookmark,
          meta: {
            title: 'Bookmark | Cuba - Premium Admin Template',
          }
        },
        {
          path:'task',
          name:'Task',
          component:Task,
          meta: {
            title: 'Task | Cuba - Premium Admin Template',
          }
        },
        {
          path:'calendar',
          name:'Calendar',
          component:Calendar,
          meta: {
            title: 'Calendar | Cuba - Premium Admin Template',
          }
        }
        ]
      },
      {
        path: "/ecommerce",
        component: Body,
        children: [
          {
            path: "product",
            name: "Product",
            component: indexProduct,
            meta: {
              title: "Products | koho - Premium Admin Template",
            },
          },
          {
            path: "product/page/:id",
            name: "ProductPage",
            component: productPage,
            meta: {
              title: "Products Page | koho - Premium Admin Template",
            },
          },
          {
            path: "product/list",
            name: "productList",
            component: productList,
            meta: {
              title: "Products list | koho - Premium Admin Template",
            },
          },
          {
            path: "payment/details",
            name: "paymentDetails",
            component: paymentDetails,
            meta: {
              title: "Payment Details | koho - Premium Admin Template",
            },
          },
          {
            path: "order/history",
            name: "Order History",
            component: orderHistory,
            meta: {
              title: "OrderHistory | koho - Premium Admin Template",
            },
          },
          {
            path: "invoice",
            name: "Invoice",
            component: invoiceView,
            meta: {
              title: "Invoice | koho - Premium Admin Template",
            },
          },
          {
            path: "cart",
            name: "Cart",
            component: cartView,
            meta: {
              title: "Cart | koho - Premium Admin Template", 
            },
          },
          {
            path: "wishlist",
            name: "Wishlist",
            component: wishlistView,
            meta: {
              title: "Wishlist | koho - Premium Admin Template",
            },
          },
          {
            path: "checkout",
            name: "Checkout",
            component: checkoutView,
            meta: {
              title: "Checkout | koho - Premium Admin Template",
            },
          },
          {
            path: "pricing",
            name: "pricing",
            component: pricingView,
            meta: {
              title: "pricingView | koho - Premium Admin Template",
            },
          },
    
    
        ],
      },
      {
        path: '/email',
        component: Body,
        children: [
          {
            path: "readMail",
            name: "readMail",
            component: readMail
          },
          {
            path: "compose",
            name: "compose",
            component: composeView
          }
        ]
      },
      {
        path: '/users',
        component: Body,
        children: [
          {
            path: "profile",
            name: "profile",
            component: userProfile
          },
          {
            path: "edit",
            name: "edit",
            component: userEdit
          },
          {
            path: "cards",
            name: "cards",
            component: userCards
          }
        ]
      },
      {
        path:"/form",
        component:Body,
        children:[
          {
            path:"validation",
            name:"formValidation",
            component:formValidation
          },
          {
            path:"inputs",
            name:"basicInput",
            component:base_Input
          },
          {
            path:"checkbox-radio",
            name:"checkbox & radio",
            component:checkbox_radio
          },
          {
            path:"input-groups",
            name:"input Groups",
            component:input_groups
          },
          {
            path:"mega-options",
            name:"megaOptions",
            component:megaOptions
          },
          {
            path:"select2",
            name:"select2",
            component:select2
          },
          {
            path:"switch",
            name:"switch",
            component:switch_From
          },
          {
            path:"touchspin",
            name:"touchspin",
            component:touchspin_Form
          },
          {
            path:"typeahead",
            name:"typeahead",
            component:typeahead_Form
          },
          {
            path:"clipboard",
            name:"clipboard",
            component:clipboard_Form
          },
          {
            path:"wizard2",
            name:"form_wizard2",
            component:form_wizard2
          },
          {
            path:"wizard1",
            name:"formwizard",
            component:form_wizard1
          },
          {
            path:"wizard3",
            name:"formwizard3",
            component:form_wizard3
          },
          {
            path:"defaultforms",
            name:"defaultforms",
            component:defaultforms
          },
          {
            path:"datepicker",
            name:"datepicker",
            component:datepicker
          },
          {
            path:"timepicker",
            name:"timepicker",
            component:timepicker
          },
          {
            path:"datetimepicker",
            name:"datetimepicker",
            component:datetimepicker
          },
          {
            path:"daterangepicker",
            name:"daterangepicker",
            component:daterangepicker
          }
        ]
      },
      {
        path: "/advance",
        component: Body,
        children: [
            {
                path: "scrollable",
                name: "Scrollable",
                component: Scrollable,
                meta: {
                    title: "Scrollable | Cuba - Premium Admin Template",
                },
            },
            {
              path: "treeView",
              name: "Tree",
              component: Tree,
              meta: {
                  title: "Tree | Cuba - Premium Admin Template",
              },
          },
            {
              path: "notify",
              name: "notify",
              component: Notify,
              meta: {
                  title: "Scrollable | Cuba - Premium Admin Template",
              },
            },
            {
              path: "rating",
              name: "Rating",
              component: Rating,
              meta: {
                  title: "Rating | Cuba - Premium Admin Template",
              },
          },
          {
            path: "dropzone",
            name: "dropzone",
            component: dropzone,
            meta: {
                title: "dropzone | Cuba - Premium Admin Template",
            },
        },
        {
          path: "tour",
          name: "Tour",
          component: Tour,
          meta: {
              title: "Tour | Cuba - Premium Admin Template",
          },
      },
            {
                path: "sweetalert",
                name: "Sweetalert",
                component: Sweetalert,
                meta: {
                    title: "Sweetalert | Cuba - Premium Admin Template",
                },
            },
            {
              path: "animatedModal",
              name: "animatedModal",
              component: animatedModal,
              meta: {
                  title: "Sweetalert | Cuba - Premium Admin Template",
              },
          },
          {
            path: "owlCarousel",
            name: "owlCarousel",
            component: owlCarousel,
            meta: {
                title: "Sweetalert | Cuba - Premium Admin Template",
            },
        },
           
            {
                path: "ribbons",
                name: "Ribbons",
                component: Ribbons,
                meta: {
                    title: "Ribbons | Cuba - Premium Admin Template",
                },
            },
            {
              path: "pagination",
              name: "Pagination",
              component: Pagination,
              meta: {
                  title: "Pagination | Cuba - Premium Admin Template",
              },
          },
          {
            path: "breadcrumb",
            name: "Breadcrumb",
            component: Breadcrumb,
            meta: {
                title: "Breadcrumb | Cuba - Premium Admin Template",
            },
        },
            {
                path: "range-slider",
                name: "Rangeslider",
                component: Rangeslider,
                meta: {
                    title: "Rangeslider | Cuba - Premium Admin Template",
                },
            },
            {
              path: "image-cropper",
              name: "ImageCropper",
              component: ImageCropper,
              meta: {
                  title: "ImageCropper | Cuba - Premium Admin Template",
              },
          },
            
            {
                path: "sticky",
                name: "Sticky",
                component: Sticky,
                meta: {
                    title: "Sticky | Cuba - Premium Admin Template",
                },
            },
            {
              path: "basicCard",
              name: "basicCard",
              component: BasicCard,
              meta: {
                  title: "Sticky | Cuba - Premium Admin Template",
              },
          },
          {
            path: "creativeCard",
            name: "creativeCard",
            component: CreativeCard,
            meta: {
                title: "Sticky | Cuba - Premium Admin Template",
            },
        },
        {
          path: "TabbedCard",
          name: "TabbedCard",
          component: TabbedCard,
          meta: {
              title: "Sticky | Cuba - Premium Admin Template",
          },
      },
      {
        path: "DraggableCard",
        name: "DraggableCard",
        component: DraggableCard,
        meta: {
            title: "Sticky | Cuba - Premium Admin Template",
        },
    },
            {
                path: "timeline1",
                name: "timeline",
                component: timeLine,
                meta: {
                    title: "Toastr | Cuba - Premium Admin Template",
                },
            },
            {
              path: "timeline2",
              name: "timeline2",
              component: timeLine2,
              meta: {
                  title: "Toastr | Cuba - Premium Admin Template",
              },
          },
            
        ],
    },
    {
      path:"/chart",
      component:Body,
      children:[
        {
          path:"google",
          name:"googlechart",
          component:google_chart
        },
        {
          path:"apexChart",
          name:"apexchart",
          component:apex_chart
        },
        {
          path:"chartist",
          name:"chartist",
          component:chartist_chart
        },
        // {
        //   path:"sparkLine",
        //   name:"sparkline",
        //   component:sparkline
        // }
      ]
    },
    {
      path: '/pages',
      component: Body,
      children:[
        {
          path:'/pages/faq',
          name:'Faq',
          component:Faq,
          meta: {
          title: 'Faq | Cuba - Premium Admin Template',
        }
        },
          {
            path:'/pages/support',
            name:'Support',
            component:Support,
            meta: {
            title: 'Support | Cuba - Premium Admin Template',
          }
          },
          {
            path:'sample-page',
            name:'sample-page',
            component:sample_page,
            meta: {
                title: 'sample-page | Cuba - Premium Admin Template',
              }
          },
          {
      path:"search",
      name:"search",
      component:serchIndex
    },
          // {
          //   path:'/pages/social-app',
          //   name:'Social',
          //   component:Social,
          //   meta: {
          //   title: 'Social | Cuba - Premium Admin Template',
          // }
          // }
      ]
    },
    {
      path: '/uikits',
      component: Body,
      children: [
      {
        path: 'alert',
        name: 'alert',
        component: alert,
        meta: {
          title: 'Alert | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'helper-classes',
        name: 'Helperclasses',
        component: Helperclasses,
        meta: {
          title: 'Helperclasses | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'avatars',
        name: 'Avatars',
        component: Avatars,
        meta: {
          title: 'Avatars | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'grid',
        name: 'Grid',
        component: Grid,
        meta: {
          title: 'Grid | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'tag-pills',
        name: 'Tagpills',
        component: Tagpills,
        meta: {
          title: 'Tagpills | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'typography',
        name: 'Typography',
        component: Typography,
        meta: {
          title: 'Typography | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'progress-bar',
        name: 'Progressbar',
        component: Progressbar,
        meta: {
          title: 'Progressbar | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'modal',
        name: 'Modal',
        component: Modal,
        meta: {
          title: 'Modal | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'popover',
        name: 'Popover',
        component: Popover,
        meta: {
          title: 'Popover | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'tooltip',
        name: 'Tooltip',
        component: Tooltip,
        meta: {
          title: 'Tooltip | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'loader',
        name: 'Spinners',
        component: Spinners,
        meta: {
          title: 'Spinners | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'dropdown',
        name: 'Dropdown',
        component: Dropdown,
        meta: {
          title: 'Dropdown | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'accordion',
        name: 'Accordion',
        component: Accordion,
        meta: {
          title: 'Accordion | Cuba - Premium Admin Template',
        }
      },
      {
        path: "bootstraptab",
        name: "bootstraptabPage",
        component: bootstraptabPage,
        meta: {
          title: "tab | Cuba - Premium Admin Template",
        },
      },
      {
        path: "linetab",
        name: "linetabPage",
        component: linetabPage,
        meta: {
          title: "Accordion | Cuba - Premium Admin Template",
        },
      },
      {
        path: 'box-shadow',
        name: 'Boxshadow',
        component: Boxshadow,
        meta: {
          title: 'Boxshadow | Cuba - Premium Admin Template',
        }
      },
      {
        path: 'lists',
        name: 'Lists',
        component: Lists,
        meta: {
          title: 'Lists | Cuba - Premium Admin Template',
        }
      }
      ]
    },
    {
      path: "/animation",
      component: Body,
      children: [
          {
              path: "animate",
              name: "animate",
              component: animate,
              meta: {
                  title: "animate | Cuba - Premium Admin Template",
              },
          },
          {
            path: "scroll",
            name: "scroll",
            component: scroll,
            meta: {
                title: "scroll | Cuba - Premium Admin Template",
            },
        },
          {
            path: "AOS",
            name: "aos",
            component: aos,
            meta: {
                title: "aos | Cuba - Premium Admin Template",
            },
          },
        //   {
        //     path: "tilt",
        //     name: "tilt",
        //     component: tilt,
        //     meta: {
        //         title: "tilt | Cuba - Premium Admin Template",
        //     },
        // },
        {
          path: "wow",
          name: "wow",
          component: wow,
          meta: {
              title: "wow | Cuba - Premium Admin Template",
          },
      },
      {
        path: "tilt",
        name: "tilt",
        component: tilt,
        meta: {
            title: "tilt | Cuba - Premium Admin Template",
        },
    },
        ],
    },
    {
      path:"/builder",
      component: Body,
      children:[
        {
          path: "form1",
          name: "Form Builder1",
          component: form1,
          meta: {
            title: "from1 | Cuba - Premium Admin Template",
          },
        },
        {
          path: "form2",
          name: "Form Builder2",
          component: form2,
          meta: {
            title: "from2 | Cuba - Premium Admin Template",
          },
        }
      ]
    },
    {
      path: '/icons',
      component: Body,
      children:[
      {
        path: 'flag',
        name: 'Flag',
        component: Flag,
         meta: {
            title: 'Flag | Cuba - Premium Admin Template',
          }
      },
      {
        path: 'ico',
        name: 'Ico',
        component: Ico,
         meta: {
            title: 'Ico | Cuba - Premium Admin Template',
          }
      },
      {
        path: 'themify',
        name: 'Themify',
        component: Themify,
         meta: {
            title: 'Themify | Cuba - Premium Admin Template',
          }
      },
      {
        path: 'fontawesome',
        name: 'Fontawesome',
        component: Fontawesome,
         meta: {
            title: 'Fontawesome | Cuba - Premium Admin Template',
          }
      },
      {
        path: 'feather_icon',
        name: 'FeatherIcon',
        component: FeatherIcon,
         meta: {
            title: 'FeatherIcon | Cuba - Premium Admin Template',
          }
      },
      {
        path: 'whether',
        name: 'WhetherIcon',
        component: WhetherIcon,
         meta: {
            title: 'WhetherIcon | Cuba - Premium Admin Template',
          }
      }
      ]
    },
    {
      path: '/buttons',
      component: Body,
      children:[
      {
        path: 'default',
        name: 'default_buttons',
        component: Default_buttons,
         meta: {
            title: 'Default_buttons | Cuba - Premium Admin Template',
          }
      },
      {
        path: 'flat',
        name: 'flat_buttons',
        component: Flat_buttons,
         meta: {
            title: 'Flat_buttons | Cuba - Premium Admin Template',
          }
      },
      {
        path: 'edge',
        name: 'edge_buttons',
        component: Edge_buttons,
         meta: {
            title: 'Edge_buttons | Cuba - Premium Admin Template',
          }
      },
      {
        path: 'raised',
        name: 'raised_buttons',
        component: Raised_buttons,
         meta: {
            title: 'Raised_buttons | Cuba - Premium Admin Template',
          }
      },
      {
        path: 'group',
        name: 'group_buttons',
        component: Group_buttons,
         meta: {
            title: 'Group_buttons | Cuba - Premium Admin Template',
          }
      }
      ]
    },
    {
      path: '/knowledgebase',
      component: Body,
      children: [
        {
          path: "knowledgebase",
          name: 'knowledge',
          component: knowledge
        },
        {
          path: 'category',
          name: 'category_knowledge',
          component: category_knowledge
        },
        {
          path: 'detail',
          name: 'detail_knowledge',
          component: detail_knowledge
        }
      ]
    },
    {
      path:'/error-400',
      name:'Error400',
      component:Error400,
      meta: {
          title: 'Error400 | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/error-401',
      name:'Error401',
      component:Error401,
      meta: {
          title: 'Error401 | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/error-403',
      name:'Error403',
      component:Error403,
      meta: {
          title: 'Error403 | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/error-404',
      name:'Error404',
      component:Error404,
      meta: {
          title: 'Error404 | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/error-500',
      name:'Error500',
      component:Error500,
      meta: {
          title: 'Error500 | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/error-503',
      name:'Error503',
      component:Error503,
      meta: {
          title: 'Error503 | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/login/one',
      name:'LoginOne',
      component:LoginOne,
      meta: {
          title: 'LoginOne | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/login/two',
      name:'LoginTwo',
      component:LoginTwo,
      meta: {
          title: 'LoginTwo | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/login/validate',
      name:'LoginValidate',
      component:LoginValidate,
      meta: {
          title: 'LoginValidate | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/login/tooltip',
      name:'LoginValidate',
      component:LoginTooltip,
      meta: {
          title: 'LoginTooltip | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/login/sweetalert',
      name:'LoginValidate',
      component:LoginSweetalert,
      meta: {
          title: 'LoginTooltip | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/register/image',
      name:'RegisterImage',
      component:RegisterImage,
      meta: {
          title: 'RegisterImage | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/register/image2',
      name:'RegisterImage2',
      component:RegisterImage2,
      meta: {
          title: 'RegisterImage2 | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/register/wizard',
      name:'RegisterWizard',
      component:RegisterWizard,
      meta: {
          title: 'RegisterWizard | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/unlockuser',
      name:'Unlock',
      component:Unlock,
      meta: {
          title: 'Unlock | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/forgetpassword',
      name:'ForgetPassword',
      component:ForgetPassword,
      meta: {
          title: 'ForgetPassword | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/resetpassword',
      name:'ResetPassword',
      component:ResetPassword,
      meta: {
          title: 'ResetPassword | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/authentication/maintenance',
      name:'Maintenance',
      component:Maintenance,
      meta: {
          title: 'ResetPassword | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/comingsoon/comingsoon-image',
      name:'ComingsoonImage',
      component:ComingsoonImage,
      meta: {
          title: 'ComingsoonImage | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/comingsoon/comingsoon-simple',
      name:'ComingsoonSimple',
      component:ComingsoonSimple,
      meta: {
          title: 'ComingsoonSimple | Cuba - Premium Admin Template',
        }
    },
    {
      path:'/comingsoon/comingsoon-video',
      name:'ComingsoonVideo',
      component:ComingsoonVideo,
      meta: {
          title: 'ComingsoonVideo | Cuba - Premium Admin Template',
        }
    },
 
    {
      path: '/editor',
      component: Body,
      children:[
        {
          path: 'simple-editor',
          name: 'SimpleEditor',
          component:SimpleEditor,
          meta: {
            title: 'SimpleEditor | Cuba - Premium Admin Template',
          }
        },
        {
          path: 'ck-editor',
          name: 'CkEditor',
          component:CkEditor,
           meta: {
            title: 'CkEditor | Cuba - Premium Admin Template',
          }
          
        }
      ]
    },
    {
      path:'/maps',
      component: Body,
      children:[
        {
          path: 'vue-google-maps',
          name: 'GoogleMaps',
          component:GoogleMaps,
           meta: {
            title: 'oogleMaps | Cuba - Premium Admin Template',
          }
        },
        {
          path: 'vue-leaflet-maps',
          name: 'VueLeaflet',
          component:VueLeaflet,
           meta: {
            title: 'ueLeaflet | Cuba - Premium Admin Template',
          }
        }
      ]
    },
    {
      path:"/learning",
      component:Body,
      children:[
        {
          path:"list",
          name:"learninglist",
          component:learning_list
        },
        {
          path:"details/:id",
          name:"coursedetailed",
          component:coursedetailed
        }
      ]
    },
    {
      path:"/job",
      component:Body,
      children:[
        {
          path:"card",
          name:"cardview",
          component:job_card
        },
        {
          path:"list",
          name:"listview",
          component:job_list
        },
        {
          path:"/job/details/:id",
          name:"jobdetails",
          component:job_details,
          props:true
        },
        {
          path:"apply/:id",
          name:"jobapply",
          component:job_apply
        }
      ]},
      {
        path:"/blog",
        component:Body,
        children:[
          {
            path:"details",
            name:"blog-detail",
            component:blog_detail
          },
          {
            path:"single",
            name:"blog_single",
            component:blog_single
          },
          {
            path:"add",
            name:"blog_add",
            component:blog_add
          }
          
        ]
      },
      {
        path:"/gallery",
        component:Body,
        children:[
          {
            path:"grid-gallery",
            name:"gridgallery",
            component:grid_gallery
          },
          {
            path:"gallery-desc",
            name:"griddesc",
            component:grid_desc
          },
          {
            path:"hover-effect",
            name:"hovergallery",
            component:hover_gallery
          },
          {
            path:"gallery-masonary",
            name:"masonry-gallery",
            component:masonry_gallery
          },
          {
            path:"gallery-masonary-desc",
            name:"masonary-desc",
            component:masonary_desc
          }
      
        ]
      },
      {
        path: '/auth',
        component: Auth,
        children: [
        {
          path: 'login',
          name: 'Login 1',
          component: login,
          meta: {
            title: ' login | Cuba - Premium Admin Template',
          }
        },
        {
          path: 'register',
          name: 'register 1',
          component: Register,
          meta: {
            title: ' Register | Cuba - Premium Admin Template',
          }
        }
        ]
      },
      {
        path:"/table",
        component:Body,
        children:[
          {
            path:"basic",
            name:"basic1",
            component:BootstrapBasic
          },
          {
            path:"tableComponent",
            name:"tableComponent",
            component:tableComponent
          },
          
          {
            path:"/datatable-basic",
            name:"datatable",
            component:DatatableBasic
          },
          // {
          //   path:"/datatable-export",
          //   name:"dataexport",
          //   component:data_export
          // },
          // {
          //   path:"/filter-table",
          //   name:"filter",
          //   component:filter_table
          // },
          // {
          //   path:"/datatable-select-delete",
          //   name:"select_delete",
          //   component:DatatableSelect
          // },
          // {
          //   path:"smarttable",
          //   name:"basic",
          //   component:smart_table
          // }
        ]
      },
]
const router = createRouter({
    history: createWebHistory(),
    routes,
    // base: process.env.BASE_URL,
  })
  router.beforeEach((to, from, next) => {

    const  path = ['/auth/login','/auth/register'];
     if(path.includes(to.path) || localStorage.getItem('User')){
      return next();
     }
     next('/auth/login');
});
  export default router