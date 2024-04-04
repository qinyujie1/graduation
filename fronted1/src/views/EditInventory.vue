<template>
  <div>
    <AdminNavigationBar></AdminNavigationBar>

    <form @submit.prevent="updateUser" class="main">
      <div class="form-row">
        <label for="name">名字:</label>
        <input type="text" id="name" v-model="editUserForm.name">
      </div>

      <div class="form-row">
        <label for="type">类型:</label>
        <input type="text" id="type" v-model="editUserForm.type">
      </div>


      <div class="form-row">
        <label for="procity">产地:</label>
        <input type="text" id="procity" v-model="editUserForm.procity">
      </div>

      <div class="form-row">
        <label for="applicable_age">适用年龄:</label>
        <input type="text" id="applicable_age" v-model="editUserForm.applicable_age">
      </div>

      <div class="form-row">
        <label for="fabric">材质:</label>
        <input type="text" id="fabric" v-model="editUserForm.fabric">
      </div>

      <div class="form-row">
        <label for="season">季节:</label>
        <input type="text" id="season" v-model="editUserForm.season">
      </div>

      <div class="form-row">
        <label for="price">价格:</label>
        <input type="text" id="price" v-model="editUserForm.price">
      </div>


      <button type="submit">更新服装信息</button>
    </form>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref, onMounted} from 'vue';
import {useRouter} from 'vue-router';
import AdminNavigationBar from "@/components/AdminNavigationBar.vue";
import axios from "axios";
import {ElMessage} from "element-plus";

export default defineComponent({
  components: {AdminNavigationBar},
  name: "EditInventory",
  setup() {
    const $router = useRouter();
    const editUserForm = ref({
      name: '',
      type: '',
      procity: '',
      applicable_age: '',
      fabric: '',
      season: '',
      price: '',
    });
    const router = useRouter();
    const updateUser = () => {
      const clothId = $router.currentRoute.value.query.clothId;
      const userData = {
        name: editUserForm.value.name,
        type: editUserForm.value.type,
        procity: editUserForm.value.procity,
        applicable_age: editUserForm.value.applicable_age,
        fabric: editUserForm.value.fabric,
        season: editUserForm.value.season,
        price: editUserForm.value.price,

      };

      axios
          .put(`http://127.0.0.1:8000/api/inventory_management/${clothId}/`, userData)
          .then(response => {
            // 更新表单数据
            editUserForm.value.name = response.data.name;
            editUserForm.value.type = response.data.type;
            editUserForm.value.procity = response.data.procity;
            editUserForm.value.applicable_age = response.data.applicable_age;
            editUserForm.value.fabric = response.data.fabric;
            editUserForm.value.season = response.data.season;
            editUserForm.value.price = response.data.price;


            ElMessage.success('您已成功更新服装信息！');
            router.push('/inventorymanagement');
          })
          .catch(error => {
            console.error('Error:', error);
          });
    };

    onMounted(() => {
      const clothId = $router.currentRoute.value.query.clothId;
      console.log(clothId)
      axios
          .get(`http://127.0.0.1:8000/api/inventory_management/${clothId}/`)
          .then(response => {
            editUserForm.value.name = response.data.name;
            editUserForm.value.type = response.data.type;
            editUserForm.value.procity = response.data.procity;
            editUserForm.value.applicable_age = response.data.applicable_age;
            editUserForm.value.fabric = response.data.fabric;
            editUserForm.value.season = response.data.season;
            editUserForm.value.price = response.data.price;
          })
          .catch(error => {
            console.error('Error fetching user data:', error);
          });
    });

    return {
      editUserForm,
      updateUser
    };
  }
});
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border: 1px solid #ccc;
  width: 40%;
  margin: 100px auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
  margin-left: 400px;
}

.main:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.form-row {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

label {
  margin-right: 10px;
  width: 86px;
  font-size: 14px; /* 将标签字体大小改为14px */
  color: #333; /* 修改标签颜色 */
}

input {
  padding: 8px;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
}

input:focus {
  outline: none;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  background: linear-gradient(to right, #007bff, #0056b3); /* 使用渐变背景色 */
  color: white;
  border: none;
  cursor: pointer;
  transition: background 0.3s;
  border-radius: 5px; /* 添加按钮圆角 */
}

button:hover {
  background: linear-gradient(to right, #0056b3, #003c7e); /* 悬停时渐变背景色 */
}
</style>
