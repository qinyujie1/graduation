import { reactive  } from 'vue'

interface RegisterUser{
  name:string;
  password: string;
  password2: string;
  role:string
}

// 登录表单
export const registerUser = reactive<RegisterUser>({
  name:'',
  password: '',
  password2: '',
  role:''
})

interface RegisterRules{
  name: {
    required: boolean;
    message: string;
    trigger: string;
}[];

  password: ({
      required: boolean;
      message: string;
      trigger: string;
  } | {
      min: number;
      max: number;
      message: string;
      trigger: string;
  })[];
  password2: ({
      required: boolean;
      message: string;
      trigger: string;
  } | {
      min: number;
      max: number;
      message: string;
      trigger: string;
  } | {
    validator:(rule: RegisterRules, value: string, callback: any)=>any;
    trigger:string
  })[];
  role: {
    required: boolean;
    message: string;
    trigger: string;
}[];
}

const validatePass2 = (rule: RegisterRules, value: string, callback: any) => {
  if (value === '') {
    callback(new Error('请再次输入密码'))
  } else if (value !== registerUser.password) {
    callback(new Error("两次输入的密码不一致!"))
  } else {
    callback()
  }
}

// 校验规则
export const registerRules = reactive<RegisterRules>({
  name: [
    {
      required: true,
      message: '用户名不得为空',
      trigger: 'blur'
    }
  ],

  password: [
    { required: true, message: '密码不得为空', trigger: 'blur' },
    { min: 6, max: 30, message: '密码长度必须在6到30之间', trigger: 'blur' }
  ],
  password2: [
    { required: true, message: '确认密码不得为空', trigger: 'blur' },
    { min: 6, max: 30, message: '密码长度必须在6到30之间', trigger: 'blur' },
    { validator: validatePass2, trigger: 'blur' }
  ],
  role: [
    {
      required: true,
      message: '角色不得为空',
      trigger: 'blur'
    }
  ],
})
