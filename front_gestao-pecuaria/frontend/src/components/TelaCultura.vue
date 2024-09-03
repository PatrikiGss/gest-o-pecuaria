<template>
    <div class="form-container">
      <h1>Cadastro de cultura</h1>
      <form @submit.prevent="submitForm" class="producer-form">
        <div class="form-group">
          <label for="usuario">Usuário:</label>
          <select id="usuario" v-model="formData.usuario" class="form-control">
            <option v-for="usuario in usuarios" :key="usuario.id" :value="usuario.id">
              {{ usuario.nome }}
            </option>
          </select>
        </div>
  
        <div class="form-group">
          <label for="nome">Nome:</label>
          <input type="text" id="nome" v-model="formData.nome" class="form-control" placeholder=" ex: milho, batata, maça">
        </div>
      <button type="submit" class="btn-submit">Enviar</button>
      </form>
    </div>
  </template>
  
  <script>
  import api from '@/interceptadorAxios';
  
  export default {
    data() {
      return {
        formData: {
          usuario: null,
          nome: '',
        },
        usuarios: [],
        culturas: []
      };
    },
    methods: {
      async fetchUsuarios() {
        try {
          const response = await api.get('/usuarios/');
          this.usuarios = response.data;
        } catch (error) {
          console.error('Erro ao buscar usuários:', error);
        }
      },
      async submitForm() {
        try {
          const response = await api.post('/culturas/', this.formData);
          if (response.status === 201) {
            alert('cultura cadastrada com sucesso!');
            this.culturas.push(response.data);
          } else {
            alert('Erro ao cadastrar cultura. Tente novamente mais tarde.');
          }
        } catch (error) {
          console.error('Erro ao enviar requisição:', error);
          alert('Erro ao enviar requisição. Verifique o console para mais detalhes.');
        }
      }
    },
    created() {
      this.fetchUsuarios();
    }
  };
  </script>
  
  <style scoped>
  /* Estilos conforme sugerido anteriormente */
  .form-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .producer-form {
    display: flex;
    flex-direction: column;
    gap: 15px;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
  }
  
  .form-control {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .btn-submit {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .btn-submit:hover {
    background-color: #0056b3;
  }
  
  .producer-list {
    margin-top: 20px;
  }
  
  .producer-item {
    background-color: #fff;
    padding: 10px;
    margin-bottom: 5px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  </style>
  