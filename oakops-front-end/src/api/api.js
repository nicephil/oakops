import axios from 'axios';

let base = 'http://localhost:5000';
// var user = sessionStorage.getItem('user');
// let auth_config = {
//     headers: {
//       "Authorization": "Bearer " + JSON.parse(user).access_token
//     }
//   }
// console.log("HEADER", auth_config)

export const requestLogin = params => { return axios.post(`${base}/login`, params).then(res => res.data); };

export const requestLogout = params => { return axios.post(`${base}/logout`, params).then(res => res.data); };

export const refreshToken = params => { return axios.post(`${base}/refreshtoken`, params).then(res => res.data); };

export const getOrganiztionList = params => { return axios.get(`${base}/organize/list`, { params: params }); };

export const getDemoData = params => { return axios.get(`${base}/my`, {}); };



// export const getUserListPage = params => { return axios.get(`${base}/user/listpage`, { params: params }); };

// export const removeUser = params => { return axios.get(`${base}/user/remove`, { params: params }); };

// export const batchRemoveUser = params => { return axios.get(`${base}/user/batchremove`, { params: params }); };

// export const editUser = params => { return axios.get(`${base}/user/edit`, { params: params }); };

// export const addUser = params => { return axios.get(`${base}/user/add`, { params: params }); };