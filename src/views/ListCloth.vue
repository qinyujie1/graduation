<template>
  <navigation-bar></navigation-bar>

  <div class="card-container">
    <div v-for="item in displayedData" :key="item.id" class="card-wrapper">
      <el-card :body-style="{ padding: '0px', marginBottom: '1px' }">
        <img :src="item.img" class="image"/>
        <div class="column" style="padding: 14px">
          <span class="costume-name">{{ item.name }}</span>
          <span class="black-love">
            <img :src="item.heartImage" @click="changeHeartColor(item)">
          </span>
          <div class="bottom card-header">
            <el-button text class="button">{{ item.type }}</el-button>
          </div>
        </div>
      </el-card>
    </div>
  </div>
<!--分页-->
  <div class="pagination-container">
    <div class="pagination-wrapper">
      <el-button size="mini" @click="goToPage(1)" :disabled="currentPage === 1">首页</el-button>
      <el-pagination background layout="pager" :total="data.length" :page-size="pageSize" v-model="currentPage"
                     :page-count="pageCount" @current-change="goToPage" :current-page.sync="currentPage"
                     class="pagination">
        <template #pager>
          <span
              class="page-link"
              :class="{ active: page === currentPage }"
              v-if="page === -1"
          >
          ...
        </span>
          <span
              v-else-if="page !== -1"
              class="page-link"
              :class="{ active: page === currentPage }"
              @click="goToPage(page)"
          >
          {{ page }}
         </span>
        </template>

      </el-pagination>

      <el-button size="mini" @click="goToPage(pageCount)" :disabled="currentPage === pageCount">尾页</el-button>
    </div>
  </div>
</template>


<script lang="ts">
import NavigationBar from "@/components/NavigationBar.vue";
import {ref, onMounted, computed} from 'vue';
import axios from "axios";
import {ElMessage} from "element-plus";


export default {
  name: 'ListCloth',
  components: {NavigationBar},
  setup() {

    const data = ref([]);
    const currentPage = ref(1);

    onMounted(() => {
      // 发送 POST 请求
      axios
          .post("http://127.0.0.1:8000/api/list/")
          .then(response => {
            // 处理成功响应
            const postData = response.data;
            data.value = postData.map((item: any) => ({
              ...item,
              heartImage: require('@/assets/img/黑爱心.png'),
              isHeartSelected: false,
            }));
          })
          .catch(error => {
            // 处理错误
            console.log('POST 请求失败');
          });

      // 页面加载时获取数据
      axios
          .get("http://127.0.0.1:8000/api/list/")
          .then(response => {
            // 处理成功响应
            const responseData = response.data;
            console.log(responseData);
            for (let item of responseData) {
              if (item.isLiked == "true") {
                item.isHeartSelected = true;
                item.heartImage = require('@/assets/img/红爱心.png');
                console.log(item.heartImage)
              } else {
                item.isHeartSelected = false;
                item.heartImage = require('@/assets/img/黑爱心.png');
              }
            }

            data.value = responseData;
          })
          .catch(error => {
            // 处理错误
            console.log('获取服装列表失败');
            // 显示消息提示
            ElMessage({
              message: "获取服装列表失败",
              type: "error",
              duration: 2000 // 设置持续时间为2秒
            });
          });
    });




    const pageSize = 8; // 每页显示的数量

    const pageCount = computed(() => {
      return Math.ceil(data.value.length / pageSize); // 计算总页数
    });

    const displayedData = computed(() => {
      const startIndex = (currentPage.value - 1) * pageSize;
      const endIndex = Math.min(startIndex + pageSize, data.value.length);
      return data.value.slice(startIndex, endIndex);
    });


    const changeHeartColor = (item: { isHeartSelected: boolean; heartImage: any; name: string; type: any; detail: any; img: any; }) => {

      if (item.isHeartSelected) {
        // 取消发送
        item.isHeartSelected = false;
        item.heartImage = require('@/assets/img/黑爱心.png');
        axios.delete('http://127.0.0.1:8000/api/mylove/', {
          data: {
            name: item.name,
            type: item.type,
            detail: item.detail,
            img: item.img,
            isLiked: "false",
          }
        })
            .then(response => {
              // 处理删除成功响应
              console.log('删除【我的喜欢】成功');
              // 保存状态到localStorage
              localStorage.setItem(item.name, 'false');
              // 显示消息提示
              ElMessage({
                message: "删除【我的喜欢】成功",
                type: "success",
                duration: 2000 // 设置持续时间为2秒
              });
            })
            .catch(error => {
              // 处理删除失败
              console.log('删除【我的喜欢】失败');
              // 显示消息提示
              ElMessage({
                message: "删除【我的喜欢】失败",
                type: "error",
                duration: 2000 // 设置持续时间为2秒
              });
            });
      } else {
        // 发送
        item.isHeartSelected = true;
        item.heartImage = require('@/assets/img/红爱心.png');
        axios.post('http://127.0.0.1:8000/api/mylove/', {
          name: item.name,
          type: item.type,
          detail: item.detail,
          img: item.img,
          isLiked: "true",
        })
            .then(response => {
              // 处理成功响应
              console.log('添加【我的喜欢】成功');
              // 保存状态到localStorage
              localStorage.setItem(item.name, 'true');
              // 显示消息提示
              ElMessage({
                message: "添加【我的喜欢】成功",
                type: "success",
                duration: 2000 // 设置持续时间为2秒
              });
            })
            .catch(error => {
              // 处理错误
              console.log('添加【我的喜欢】失败');
              // 显示消息提示
              ElMessage({
                message: "添加【我的喜欢】失败",
                type: "error",
                duration: 2000 // 设置持续时间为2秒
              });
            });
      }
    };


    const nextPage = () => {
      if (currentPage.value < pageCount.value) {
        currentPage.value += 1;
      }
    };

    const previousPage = () => {
      if (currentPage.value > 1) {
        currentPage.value -= 1;
      }
    };

    const goToPage = (page: number) => {
      if (page >= 1 && page <= pageCount.value) {
        currentPage.value = page;
      }
    };


    return {
      data,
      currentPage,
      displayedData,
      pageCount,
      nextPage,
      previousPage,
      goToPage,
      changeHeartColor,
    };
  }
}
</script>


<style scoped>
.card-container[data-v-041d4952] {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  position: absolute;
  left: 250px;
  top: 80px;
}

.card-wrapper {

  padding: 10px;
}

.image {
  width: 200px;
  height: 250px;
}

.pagination-container {
  display: flex;
  justify-content: center;
  position: fixed;
  bottom: 30px;
  left: 50%;
}

.pagination-wrapper {
  transform: scale(1.3) translateX(-25%);
  display: flex;
  flex-wrap: nowrap;
}

.column {
  position: relative;
}

.costume-name {
  display: inline-block;
  max-width: 100px; /* 调整合适的宽度 */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.black-love img {
  display: inline-block;
  position: absolute;
  right: 10px;
  top: 2px;
  width: 35px;
}

</style>