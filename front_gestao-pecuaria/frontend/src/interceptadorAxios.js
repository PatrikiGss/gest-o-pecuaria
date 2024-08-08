// src/api/interceptadorAxios.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/',  // Ajuste para o seu URL de backend
  // Outras configurações do Axios, se necessário
});

export default api;
