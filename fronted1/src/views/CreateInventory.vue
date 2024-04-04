<template>
  <div>
    <AdminNavigationBar></AdminNavigationBar>
    <el-form :model="newUserForm" ref="newUserForm" label-width="80px" class="main">
      <el-form-item label="服装ID">
        <input type="text" v-model="newUserForm.id" class="input-field" disabled></input>
      </el-form-item>
      <el-form-item label="名字" prop="name">
        <input type="text" v-model="newUserForm.name" class="input-field"></input>
      </el-form-item>
      <el-form-item label="类型" prop="type">
        <input type="text" v-model="newUserForm.type" class="input-field"></input>
      </el-form-item>
      <el-form-item label="生产地" prop="procity">
        <input type="text" v-model="newUserForm.procity" class="input-field"></input>
      </el-form-item>
      <el-form-item label="适用年龄" prop="applicable_age">
        <input type="text" v-model="newUserForm.applicable_age" class="input-field"></input>
      </el-form-item>
      <el-form-item label="面料" prop="fabric">
        <input type="text" v-model="newUserForm.fabric" class="input-field"></input>
      </el-form-item>
      <el-form-item label="适用季节" prop="season">
        <input type="text" v-model="newUserForm.season" class="input-field"></input>
      </el-form-item>
      <el-form-item label="价格" prop="price">
        <input type="text" v-model="newUserForm.price" class="input-field"></input>
      </el-form-item>
      <el-form-item label="图片" prop="img">
        <input type="text" v-model="newUserForm.img" disabled class="input-field" placeholder="https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/709048633/O1CN015QjYca2Ddy7uH259j_!!709048633.jpg">
      </el-form-item>
      <el-form-item class="create">
        <el-button type="primary" size="large" @click="createUser">确认</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import AdminNavigationBar from "@/components/AdminNavigationBar.vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { ElMessage } from "element-plus";

export default defineComponent({
  components: { AdminNavigationBar },
  name: "CreateInventory",
  setup() {
    const newUserForm = ref({
      name: '',
      type: '',
      procity: '',
      applicable_age: '',
      fabric: '',
      season: '',
      price: '',
      img: 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/709048633/O1CN015QjYca2Ddy7uH259j_!!709048633.jpg' // 默认图片链接
    });

    const router = useRouter();

    const createUser = () => {
      // 在这里处理创建用户的逻辑，包括发送服装信息到后端
      axios
        .post('http://127.0.0.1:8000/api/inventory_management/', newUserForm.value)
        .then(response => {
          console.log('User created successfully:', response.data);
          ElMessage.success('您已成功创建新服装！');
          router.push('/inventorymanagement');
        })
        .catch(error => {
          console.error('Error creating user:', error);
        });
    };
    const handleFileUpload = (event) => {
      newUserForm.img = event.target.files[0];
    };

    return {
      newUserForm,
      createUser,
      handleFileUpload
    };
  }
});
</script>

<style scoped>
.main {
  width: 70%;
  position: absolute;
  top: 100px;
  left: 270px;
  right: 50px;
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
}

.main:hover {
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
}

.el-form-item__label {
  font-weight: bold;
}

.input-field,
.select-field {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.select-field {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  background-position: right 10px top 50%;
  background-size: 1em;
}

.el-button {
  margin-top: 20px;
  font-size: 18px;
  width: 100%;
}

.create {
  text-align: center;
}
</style>
