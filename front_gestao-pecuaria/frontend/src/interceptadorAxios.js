import axios from 'axios';

// Cria uma instância do Axios com a URL base do backend
const api = axios.create({
  baseURL: 'http://localhost:8000', // Substitua pela URL do seu backend
});

// Adiciona um interceptor de requisição para incluir o token JWT
api.interceptors.request.use(
  (config) => {
    // Obtém o token JWT do localStorage ou sessionStorage
    const token = localStorage.getItem('token') || sessionStorage.getItem('token');
    console.log('Token:', token);
    if (token) {
      // Define o cabeçalho Authorization com o token
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    // Lida com erros na requisição
    return Promise.reject(error);
  }
);

// Interceptor de resposta para lidar com erros de autenticação
api.interceptors.response.use(
  (response) => response, // Retorna a resposta diretamente se estiver tudo ok
  (error) => {
    if (error.response && error.response.status === 401) {
      // Exibe uma mensagem para o usuário e redireciona para a página de login
      alert("Sessão expirada. Por favor, faça login novamente.");
      // Remove o token e redireciona para a página de login
      localStorage.removeItem('token');
      sessionStorage.removeItem('token');
      window.location.href = '/login';  // Redireciona para a tela de login
    }
    return Promise.reject(error); // Propaga o erro para ser tratado pela chamada original
  }
);

export default api;
