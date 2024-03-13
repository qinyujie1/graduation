<template>

  <div class="common-layout">
    <el-container>
      <!--      导航栏-->
      <navigation-bar></navigation-bar>

      <!--        主体-->
      <el-main>


        <!--模特图+主体-->
        <div class="block text-center">
          <!--          走马灯幻灯片-->
          <el-carousel height="330px" class="carousel-with-shadow">
            <el-carousel-item>
              <img width="20%" height="330px" src="../assets/img/1.png" alt="Image 1">
              <img width="20%" height="330px" src="../assets/img/2.png" alt="Image 2">
              <img width="20%" height="330px" src="../assets/img/3.png" alt="Image 3">
              <img width="20%" height="330px" src="../assets/img/4.png" alt="Image 4">
              <img width="20%" height="330px" src="../assets/img/5.png" alt="Image 5">
            </el-carousel-item>
            <el-carousel-item>
              <img width="20%" height="330px" src="../assets/img/6.png" alt="Image 6">
              <img width="20%" height="330px" src="../assets/img/7.png" alt="Image 7">
              <img width="20%" height="330px" src="../assets/img/8.png" alt="Image 8">
              <img width="20%" height="330px" src="../assets/img/9.png" alt="Image 9">
              <img width="20%" height="330px" src="../assets/img/10.png" alt="Image 10">
            </el-carousel-item>
            <el-carousel-item>
              <img width="20%" height="330px" src="../assets/img/11.png" alt="Image 11">
              <img width="20%" height="330px" src="../assets/img/12.png" alt="Image 12">
              <img width="20%" height="330px" src="../assets/img/13.png" alt="Image 13">
              <img width="20%" height="330px" src="../assets/img/14.png" alt="Image 14">
              <img width="20%" height="330px" src="../assets/img/15.png" alt="Image 15">
            </el-carousel-item>
            <el-carousel-item>
              <img width="20%" height="330px" src="../assets/img/16.png" alt="Image 16">
              <img width="20%" height="330px" src="../assets/img/17.png" alt="Image 17">
              <img width="20%" height="330px" src="../assets/img/18.png" alt="Image 18">
              <img width="20%" height="330px" src="../assets/img/19.png" alt="Image 19">
              <img width="20%" height="330px" src="../assets/img/20.png" alt="Image 20">
            </el-carousel-item>
          </el-carousel>
        </div>

        <!--春夏秋冬-->
        <div class="reason">

        </div>


      </el-main>

    </el-container>
  </div>


</template>

// 在组件脚本中
<script lang="ts">
import {onMounted, onUnmounted, ref,} from 'vue';
import NavigationBar from '@/components/NavigationBar.vue';
import * as echarts from 'echarts/core';
import {TitleComponent, TooltipComponent, GridComponent} from 'echarts/components';
import {CanvasRenderer} from 'echarts/renderers';
import {BarChart} from "echarts/charts";

echarts.use([TitleComponent, TooltipComponent, GridComponent, CanvasRenderer, BarChart]);

export default {
  name: 'Index',
  components: {NavigationBar},


}

</script>


<style scoped>

.el-main {
  background-color: #e9edf1;
  position: absolute;
  top: 60px;
  left: 200px;
  width: 83.5%;
  height: 100%;

}


.demonstration {
  color: var(--el-text-color-secondary);
}

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.example-showcase .el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}

.carousel-with-shadow {
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
  border-radius: 50px;
  border: 2px solid darkred;
  top: 80px;
}

.el-row:last-child {
  margin-bottom: 0;

}

.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

/*这里开始炫酷按钮*/
.reason {
  position: absolute;
  top: 350px;
  margin: 0 150px;

}

.el-button {
  font-family: "阿里妈妈东方大楷 Regular";
  width: 150px;
  height: 50px;
  font-size: 40px;
}
</style>