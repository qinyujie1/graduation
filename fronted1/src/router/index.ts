import {createRouter, createWebHistory, RouteRecordRaw} from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes: Array<RouteRecordRaw> = [
    {
        path: '/',
        name: 'Index',
        component: () => import('../views/index.vue')
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('../views/LoginRegister.vue')
    },
    {
        path: '/:catchAll(.*)',
        name: '404',
        component: () => import('../views/404.vue')
    },
    {
        path: '/list',
        name: 'ListCloth',
        component: () => import('../views/ListCloth.vue')
    },
    {
        path: '/mylove',
        name: 'MyLove',
        component: () => import('../views/MyLove.vue')
    },
    {
        path: '/detail',
        name: 'Detail',
        component: () => import('../views/Detail.vue')
    },
    {
        path: '/recommend',
        name: 'Recommend',
        component: () => import('../views/Recommend.vue')
    },
    {
        path: '/dashboards',
        name: 'Dashboards',
        component: () => import('../views/Dashboards.vue')
    },
    {
        path: '/admindashboards',
        name: 'AdminDashboards',
        component: () => import('../views/AdminDashboards.vue')
    },
    {
        path: '/usermanage',
        name: 'UserManage',
        component: () => import('../views/UserManage.vue')
    },
    {
        path: '/createuser',
        name: 'CreateUser',
        component: () => import('../views/CreateUser.vue')
    },
    {
        path: '/edituser',
        name: 'EditUser',
        component: () => import('../views/EditUser.vue')
    },
    {
        path: '/inventorymanagement',
        name: 'InventoryManagement',
        component: () => import('../views/InventoryManagement.vue')
    },
    {
        path: '/createinventory',
        name: 'CreateInventory',
        component: () => import('../views/CreateInventory.vue')
    },
    {
        path: '/editinventory',
        name: 'EditInventory',
        component: () => import('../views/EditInventory.vue')
    },
    {
        path: '/bigdashboard',
        name: 'BigDashboard',
        component: () => import('../views/BigDashboard.vue')
    },

]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
