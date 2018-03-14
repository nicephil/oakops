import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'
import './styles/element-variables.scss'
import store from './vuex/store'
import Vuex from 'vuex'
import 'font-awesome/css/font-awesome.min.css'
import AxiosPlugin from './common/AxiosPlugin'
import router from './routes'
// import BootstrapVue from 'bootstrap-vue'

// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
// import Mock from './mock'
// Mock.bootstrap();

Vue.use(ElementUI)
Vue.use(Vuex)
Vue.use(AxiosPlugin)
// Vue.use(BootstrapVue);

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

