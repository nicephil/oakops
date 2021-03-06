import Vue from "vue";
import VueRouter from 'vue-router';
import Login from './views/Login.vue'
import Organization from './views/orgmgr/Organization.vue'


import NotFound from './views/404.vue'
import Home from './views/Home.vue'
import Main from './views/Main.vue'
import echarts from './views/charts/echarts.vue'

// import Table from './views/nav1/Table.vue'
// import Form from './views/nav1/Form.vue'
// import user from './views/nav1/user.vue'
// import Page4 from './views/nav2/Page4.vue'
// import Page5 from './views/nav2/Page5.vue'
// import Page6 from './views/nav3/Page6.vue'

Vue.use(VueRouter);

let routes = [
    {
        path: '/login',
        component: Login,
        name: '',
        hidden: true
    },
    {
        path: '/404',
        component: NotFound,
        name: '',
        hidden: true
    },
    //{ path: '/main', component: Main },
    {
        path: '/',
        component: Home,
        name: '',
        iconCls: 'fa fa-address-card',
        leaf: true,//只有一个节点
        children: [        
            { path: '/echarts', component: echarts, name: '首页' }
        ]
    },    
    {
        path: '/',
        component: Home,
        name: '企业站点管理',
        iconCls: 'fa fa-id-card-o',
        children: [            
            { path: '/organization', component: Organization, name: '企业站点列表' },
        ]
    },
    {
        path: '*',
        hidden: true,
        redirect: { path: '/404' }
    }
];

const router = new VueRouter({
    routes
})

export default router;