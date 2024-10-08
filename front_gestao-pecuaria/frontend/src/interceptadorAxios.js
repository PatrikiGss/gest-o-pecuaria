// src/api/interceptadorAxios.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/',  // Ajuste para o seu URL de backend
  // Outras configurações do Axios, se necessário
});

// Interceptor para adicionar o token JWT a cada requisição, se estiver disponível
api.interceptors.request.use(config => {
  const token = localStorage.getItem('token'); // Ou sessionStorage
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;  // Retorna a configuração após adicionar o token
}, error => {
  return Promise.reject(error);
});

// Interceptor de resposta para tratar erros
api.interceptors.response.use(
  response => response,  // Retorna a resposta diretamente se estiver tudo ok
  error => {
    if (error.response && error.response.status === 401) {
      // Redirecionar para a página de login ou outra ação se o token for inválido ou expirado
      console.log("Token inválido ou expirado. Faça login novamente.");
      // Por exemplo, você pode redirecionar para a página de login:
       window.location.href = '/';
    }
    return Promise.reject(error);  // Propaga o erro para que possa ser tratado na chamada original
  }
);

export default api;

