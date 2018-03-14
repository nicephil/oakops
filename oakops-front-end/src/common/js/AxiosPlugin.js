// require('es6-promise').polyfill() // 引入一次就行
import axios from 'axios'
import { Message } from "element-ui";
import routes from './../../routes'

export const Axios = axios.create({
  baseURL: 'http://localhost:5000/', 
  timeout: 5000,
})

Axios.interceptors.request.use(config => {        
    if (sessionStorage.getItem("user")) {   
        let user = JSON.parse(sessionStorage.getItem('user'));        
        config.headers.Authorization = 'Bearer ' + user.access_token
    }
    return config
},error =>{
    return Promise.reject(error)
})

Axios.interceptors.response.use(res =>{
     if(res.data.error_code != 0){
        return Promise.reject(res)
     }
     return res
 }, error => {
    // Message({
    //     message: '警告哦，这是一条警告消息',
    //     type: 'warning'
    // });
     if(error.response.status === 401) {    
        routes.push({
            path: "/login"
        });
     } else if (error.response.status === 500) {
        return Promise.reject(error.response.data)
     }
     return Promise.reject(error.response.data)
 })

export default {
  install(Vue) {
    Object.defineProperty(Vue.prototype, '$http', { value: Axios })
  }
}