<script lang="ts">
import loginForm from "./LoginForm.vue";
import router from "../router/index";
import {useRouter} from "vue-router";
import {RouteLocationNormalizedLoaded} from 'vue-router';
import axios from "axios";

declare global {
  interface Window {
    WIDGET: any;
  }
}
export default {
  name: 'NavigationBar',
  components: {
    loginForm,
  },

  setup() {
    const userName = localStorage.getItem('userName');
    return {userName};
  },
  data() {
    return {
      activeIndex: null
    };
  },


  created() {
    window.WIDGET = {
      "CONFIG": {
        "modules": "01234",
        "background": "3",
        "tmpColor": "FFFFFF",
        "tmpSize": "16",
        "cityColor": "FFFFFF",
        "citySize": "16",
        "aqiColor": "FFFFFF",
        "aqiSize": "16",
        "weatherIconSize": "24",
        "alertIconSize": "18",
        "padding": "17px 10px 17px 10px",
        "shadow": "0",
        "language": "auto",
        "fixed": "false",
        "vertical": "top",
        "horizontal": "left",
        "borderRadius": "20",
        "key": "f5eed6ba4ddd4a4995f050010d8d58be"
      }
    };
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = "https://widget.qweather.net/simple/static/js/he-simple-common.js?v=2.0";
    document.getElementsByTagName('head')[0].appendChild(script);
  },
  methods: {
    logout() {
      axios.get('http://127.0.0.1:8000/api/logout/')
        .then(response => {
          // 处理退出登录成功的逻辑，例如清除本地存储的用户信息等
          console.log(response.data);
          // 重新加载页面或跳转到登录页面
          router.push({path: '/login'});
        })
        .catch(error => {
          console.error(error);
        });
    }
  }

}


</script>
<!--导航栏组件-->
<template>
  <!--      左边导航栏-->
  <el-aside>
    <el-row class="tac">
      <el-col :span="12">
        <router-link to="/">
          <h5 class="mb-2" style="color: white">
            <img src="../assets/img/服装.png" style=" width:20px;" alt="图标">
            服装小屋
          </h5>
        </router-link>
        <el-menu active-text-color="#ccc" text-color="#fff" default-active="2" class="el-menu-vertical-demo">
          <router-link to="/list">
            <el-menu-item index="1" v-bind:style="{ color: activeIndex === 1 ? 'black' : 'white' }"
                          @mouseover="activeIndex = 1" @mouseleave="activeIndex = null">

              <span style="padding-left: 45px" class="font1">服装列表</span>

            </el-menu-item>
          </router-link>
          <router-link to="/mylove">
            <el-menu-item index="2" v-bind:style="{ color: activeIndex === 2 ? 'black' : 'white' }"
                          @mouseover="activeIndex = 2" @mouseleave="activeIndex = null">
              <span style="padding-left: 45px" class="font2">我的喜欢</span>
            </el-menu-item>
          </router-link>
        </el-menu>
      </el-col>
    </el-row>

  </el-aside>
  <!--      整个右边-->
  <el-container>
    <!--        头部-->
    <el-header>

      <!--    天气  -->
      <div class="weather">
        <div id="he-plugin-simple"></div>
      </div>

      <!--用户登录下拉框-->
      <el-dropdown>
        <span class="el-dropdown-link">
              {{ userName }}
          <el-icon class="el-icon--right">
            <arrow-down/>
          </el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>

      <!--头像.png-->
      <div class="avatar">
        <img src="../assets/img/头像.png">
      </div>
    </el-header>
  </el-container>
</template>

<style scoped>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  border: none;
}

.el-aside {
  border-radius: 20px;
}

.el-aside .el-menu {
  background-color: #313743;
}

.el-header {
  border-radius: 50px;
}

.mb-2 {
  font-family: "cloth_icon";
  font-size: 22px;
}

/* 在线链接服务仅供平台体验和调试使用，平台不承诺服务的稳定性，企业客户需下载字体包自行发布使用并做好备份。 */
@font-face {
  font-family: "cloth_icon1";
  font-weight: 400;
  src: url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/DPJSqY1pXw80.woff2") format("woff2"),
  url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/AEV2FaJJD8aM.woff") format("woff");
  font-display: swap;
}

.font1 {
  font-family: "cloth_icon1";
  font-size: 18px;
}
/* 在线链接服务仅供平台体验和调试使用，平台不承诺服务的稳定性，企业客户需下载字体包自行发布使用并做好备份。 */
@font-face {
  font-family: "cloth_icon3";
  font-weight: 400;
  src: url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/J8pYtJKbKVw0.woff2") format("woff2"),
  url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/nShi6sWndFFc.woff") format("woff");
  font-display: swap;
}
/* 在线链接服务仅供平台体验和调试使用，平台不承诺服务的稳定性，企业客户需下载字体包自行发布使用并做好备份。 */
@font-face {
  font-family: "cloth_icon2";
  font-weight: 400;
  src: url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/xJpO6iZH9Cvf.woff2") format("woff2"),
  url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/tTe2uKbVS5Bt.woff") format("woff");
  font-display: swap;
}

.font2 {
  font-family: "cloth_icon2";
  font-size: 18px;
}
.font3 {
  font-family: "cloth_icon3";
  font-size: 18px;
}

/* 在线链接服务仅供平台体验和调试使用，平台不承诺服务的稳定性，企业客户需下载字体包自行发布使用并做好备份。 */
@font-face {
  font-family: "阿里妈妈东方大楷 Regular";
  font-weight: 400;
  src: url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/PsJFfMkc9tcD.woff2") format("woff2"),
  url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/x0fgZmDTPiBY.woff") format("woff");
  font-display: swap;
}

/* 在线链接服务仅供平台体验和调试使用，平台不承诺服务的稳定性，企业客户需下载字体包自行发布使用并做好备份。 */
@font-face {
  font-family: "cloth_icon";
  font-weight: 400;
  src: url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/5YcOZhLQbDoj.woff2") format("woff2"),
  url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/o5FNP9ZUydfs.woff") format("woff");
  font-display: swap;
}

.el-container {
  position: relative;
}

.el-aside {
  position: fixed;
  background-color: #313743;
  color: #fff;
  border: 0;
  height: 100vh;
  width: 200px;
}


.el-header {
  background-color: #363d40;
  width: 85%;
  position: fixed;
  color: #fff;
  left: 200px;
  top: 0px;
  z-index: 2;
}

.el-row {
  position: relative;
  display: contents;
}

.el-col-12 {
  max-width: 100%;
}

.mb-2 {
  height: 60px;
  text-align: center;
  line-height: 60px;
}

.avatar img{
  position: absolute;
  right: 50px;
  top: 0px;
  width: 60px;
}

.el-dropdown {
  right: 100px;
  height: 60px;
  line-height: 60px;
  position: absolute;
  color: #fff;
}

.el-dropdown-menu {
  border: 0;
}

.weather {
  position: absolute;
  width: 300px;
  z-index: 2;
  left: 25px;
}

/* 悬停状态下的菜单项字体颜色为黑色 */
.el-menu-vertical-demo .el-menu-item:hover {
  color: #000;
}

</style>