<template>
  <div class="form-container">
    <h1>Cadastro de Usuários</h1>
    <form @submit.prevent="submitForm" class="user-form">
      <div class="form-group">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" v-model="formData.nome" class="form-control">
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="formData.email" class="form-control">
      </div>

      <div class="form-group">
        <label for="telefone">Telefone:</label>
        <input type="text" id="telefone" v-model="formData.telefone" class="form-control">
      </div>

      <div class="form-group">
        <label for="cpf">CPF:</label>
        <input type="text" id="cpf" v-model="formData.cpf" class="form-control">
      </div>

      <div class="form-group">
        <label for="senha">Senha:</label>
        <input type="password" id="senha" v-model="formData.senha" class="form-control">
      </div>

      <div class="form-group">
        <label for="creditos">Créditos:</label>
        <input type="number" id="creditos" v-model="formData.creditos" class="form-control">
      </div>

      <button type="submit" class="btn-submit">Enviar</button>
    </form>

    <div class="user-list">
      <h2>Lista de Usuários</h2>
      <ul>
        <li v-for="usuario in usuarios" :key="usuario.id" class="user-item">
          {{ usuario.nome }} - {{ usuario.email }} - {{ usuario.telefone }} - {{ usuario.cpf }} - {{ usuario.senha }} - {{ usuario.creditos }}
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.form-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 10px;
  background-color:whitesmoke;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.user-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.form-group {
  display:flex;
  flex-direction: column;
}

.form-control {
  padding: 5px;
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

.user-list {
  margin-top: 20px;
}

.user-item {
  background-color: #fff;
  padding: 10px;
  margin-bottom: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
</style>

  
  <script>
 import api from '@/interceptadorAxios';

  export default {
    data() {
      return {
        formData: {
          nome: '',
          email: '',
          telefone:'',
          cpf:'',
          senha:'',
          creditos:'',
        },
        usuarios: []
      };
    },
    methods: {
      async submitForm() {
        try {
          const response = await api.post('/usuarios/', this.formData);
          if (response.status === 201) {
            alert('Cadastro realizado com sucesso!');
            this.fetchUsuarios();
          } else {
            alert('Erro ao cadastrar usuário. Tente novamente mais tarde.');
          }
        } catch (error) {
          console.error('Erro ao enviar requisição:', error);
          alert('Erro ao enviar requisição. Verifique o console para mais detalhes.');
        }
      },
      async fetchUsuarios() {
        try {
          const response = await api.get('/usuarios/');
          this.usuarios = response.data;
        } catch (error) {
          console.error('Erro ao buscar usuários:', error);
        }
      }
    },
    created() {
      this.fetchUsuarios();
    }
  };
  </script>
  