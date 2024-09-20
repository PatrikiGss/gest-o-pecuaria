// src/api/interceptadorAxios.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/',  // Ajuste para o seu URL de backend
  // Outras configurações do Axios, se necessário
});

// // Adiciona o token JWT a cada requisição, se estiver disponível
// api.interceptors.request.use(config => {
//   const token = localStorage.getItem('token'); // Ou sessionStorage
//   if (token) {
//     config.headers.Authorization = `Bearer ${token}`;
//   }
//   return config;
// });

export default api;
