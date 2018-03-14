import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'
import './styles/element-variables.scss'
import VueRouter from 'vue-router'
import store from './vuex/store'
import Vuex from 'vuex'
import routes from './routes'
import 'font-awesome/css/font-awesome.min.css'
import AxiosPlugin from './common/js/AxiosPlugin'

// import Mock from './mock'
// Mock.bootstrap();

Vue.use(ElementUI)
Vue.use(VueRouter)
Vue.use(Vuex)
Vue.use(AxiosPlugin)

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path == '/login') {
    sessionStorage.removeItem('user');
  }

  let user;
  try{
    user = JSON.parse(sessionStorage.getItem('user'));
  }catch(err){
    sessionStorage.removeItem('user');
  }
  
  if (!user && to.path != '/login') {
    next({ path: '/login' })
  } else {
    next()
  }
})

new Vue({
  //el: '#app',
  //template: '<App/>',
  router,
  store,
  //components: { App }
  render: h => h(App)
}).$mount('#app')

