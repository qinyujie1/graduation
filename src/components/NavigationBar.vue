<script lang="ts">
import loginForm from "./LoginForm.vue";
import router from "../router/index";
import {useRouter} from "vue-router";
import {RouteLocationNormalizedLoaded} from 'vue-router';

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
    const userName=localStorage.getItem('userName');
    return {userName};
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
        "key": "d184dbb323d449eb8322027e7fd0728d"
      }
    };
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = "https://widget.qweather.net/simple/static/js/he-simple-common.js?v=2.0";
    document.getElementsByTagName('head')[0].appendChild(script);
  },

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
        <el-menu active-text-color="#409Eff"
                 background-color="#545c64"
                 text-color="#fff"
                 default-active="2"
                 class="el-menu-vertical-demo"
        >
          <el-menu-item index="1">
            <router-link to="/list">
              <el-icon>
                <location/>
              </el-icon>
              <span style="color: white">
              服装列表
            </span>
            </router-link>
          </el-menu-item>
          <el-menu-item index="2">
            <router-link to="/mylove">
              <el-icon>
                <icon-menu/>
              </el-icon>
              <span style="color:white;">我的喜欢</span>
            </router-link>
          </el-menu-item>
          <el-menu-item index="4">
            <el-icon>
              <setting/>
            </el-icon>
            <span style="color:white;"> ->待定待定<- </span>
          </el-menu-item>
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
            <el-dropdown-item>Action 1</el-dropdown-item>
            <el-dropdown-item>Action 2</el-dropdown-item>
            <el-dropdown-item>Action 3</el-dropdown-item>
            <el-dropdown-item disabled>Action 4</el-dropdown-item>
            <el-dropdown-item divided>Action 5</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>

      <!--头像-->
      <div class="avatar">
        <el-avatar
            src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
        />
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

/* 在线链接服务仅供平台体验和调试使用，平台不承诺服务的稳定性，企业客户需下载字体包自行发布使用并做好备份。 */
@font-face {
  font-family: "阿里妈妈东方大楷 Regular";
  font-weight: 400;
  src: url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/PsJFfMkc9tcD.woff2") format("woff2"),
  url("//at.alicdn.com/wf/webfont/h2kiuecLB7qy/x0fgZmDTPiBY.woff") format("woff");
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

.avatar {
  position: absolute;
  right: 50px;
  top: 5px;
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
  left: -1px;
}

</style>