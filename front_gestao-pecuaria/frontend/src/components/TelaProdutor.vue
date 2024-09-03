<template>
  <div class="form-container">
    <h1>Cadastro de Produtores</h1>
    <!-- Formulário para criação de um novo produtor -->
    <form @submit.prevent="submitForm" class="producer-form">
      <div class="form-group">
        <label for="usuario">Usuário:</label>
        <select id="usuario" v-model="formData.usuario" class="form-control" required>
          <option disabled value="">Selecione um usuário</option>
          <option v-for="usuario in usuarios" :key="usuario.id" :value="usuario.id">
            {{ usuario.nome }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="cpf">CPF:</label>
        <input type="text" id="cpf" v-model="formData.cpf" class="form-control" placeholder="Digite apenas os números" required />
      </div>
      <div class="form-group">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" v-model="formData.nome" class="form-control" placeholder="Digite seu nome completo" required />
      </div>
      <div class="form-group">
        <label for="telefone">Telefone:</label>
        <input type="text" id="telefone" v-model="formData.telefone" class="form-control" placeholder="Ex: (49)123112233" required />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="formData.email" class="form-control" placeholder="Ex: email@gmail.com" required />
      </div>
      <button type="submit" class="btn-submit">Enviar</button>
    </form>

    <!-- Lista de produtores com opções de editar e deletar -->
    <div class="producer-list">
      <h1>Lista de Produtores</h1>
      <div v-if="produtores.length">
        <div v-for="produtor in produtores" :key="produtor.id" class="produtor-item">
          <div v-if="editProdutor === produtor.id">
            <!-- Formulário de Edição -->
            <div class="form-group">
              <label for="usuario">Usuário:</label>
              <select id="usuario" v-model="editFormData.usuario" class="form-control" required>
                <option disabled value="">Selecione um usuário</option>
                <option v-for="usuario in usuarios" :key="usuario.id" :value="usuario.id">
                  {{ usuario.nome }}
                </option>
              </select>
            </div>
            <div class="form-group">
              <label for="cpf">CPF:</label>
              <input type="text" v-model="editFormData.cpf" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="nome">Nome:</label>
              <input type="text" v-model="editFormData.nome" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="telefone">Telefone:</label>
              <input type="text" v-model="editFormData.telefone" class="form-control" required />
            </div>
            <div class="form-group">
              <label for="email">Email:</label>
              <input type="email" v-model="editFormData.email" class="form-control" required />
            </div>
            <button @click="saveProdutor(produtor.id)" class="btn-submit">Salvar</button>
            <button @click="cancelEdit" class="btn-cancel">Cancelar</button>
          </div>
          <div v-else>
            <!-- Exibição dos Dados -->
            <p><strong>Usuário:</strong> {{ getUsuarioNome(produtor.usuario) }}</p>
            <p><strong>CPF:</strong> {{ produtor.cpf }}</p>
            <p><strong>Nome:</strong> {{ produtor.nome }}</p>
            <p><strong>Telefone:</strong> {{ produtor.telefone }}</p>
            <p><strong>Email:</strong> {{ produtor.email }}</p>
            <button @click="startEditing(produtor)" class="btn-edit">🖊️</button>
            <button @click="deleteProdutor(produtor.id)" class="btn-delete">🗑️</button>
          </div>
        </div>
      </div>
      <div v-else>
        <p>Nenhum produtor encontrado.</p>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/interceptadorAxios';

export default {
  data() {
    return {
      formData: {
        usuario: '',
        cpf: '',
        nome: '',
        telefone: '',
        email: ''
      },
      editFormData: {
        usuario: '',
        cpf: '',
        nome: '',
        telefone: '',
        email: ''
      },
      usuarios: [],
      produtores: [],
      editProdutor: null,
    };
  },
  methods: {
    // Método para obter o nome do usuário a partir do ID
    getUsuarioNome(usuarioId) {
      const usuario = this.usuarios.find(u => u.id === usuarioId);
      return usuario ? usuario.nome : 'Desconhecido';
    },
    // Busca todos os produtores
    async fetchProdutores() {
      try {
        const response = await api.get('/produtores/');
        this.produtores = response.data;
      } catch (error) {
        console.error('Erro ao buscar produtores:', error);
        alert('Erro ao buscar produtores. Verifique o console para mais detalhes.');
      }
    },
    // Busca todos os usuários
    async fetchUsuarios() {
      try {
        const response = await api.get('/usuarios/');
        this.usuarios = response.data;
      } catch (error) {
        console.error('Erro ao buscar usuários:', error);
        alert('Erro ao buscar usuários. Verifique o console para mais detalhes.');
      }
    },
    // Envia o formulário para criar um novo produtor
    async submitForm() {
      try {
        const response = await api.post('/produtores/', this.formData);
        if (response.status === 201) {
          alert('Produtor cadastrado com sucesso!');
          this.produtores.push(response.data);
          // Limpa o formulário
          this.formData = { usuario: '', cpf: '', nome: '', telefone: '', email: '' };
        } else {
          alert('Erro ao cadastrar produtor. Tente novamente mais tarde.');
        }
      } catch (error) {
        console.error('Erro ao enviar requisição:', error);
        alert('Erro ao enviar requisição. Verifique o console para mais detalhes.');
      }
    },
    // Inicia a edição de um produtor
    startEditing(produtor) {
      this.editProdutor = produtor.id;
      this.editFormData = { ...produtor };
    },
    // Cancela a edição
    cancelEdit() {
      this.editProdutor = null;
      this.editFormData = { usuario: '', cpf: '', nome: '', telefone: '', email: '' };
    },
    // Salva as alterações de um produtor
    async saveProdutor(produtorId) {
      try {
        const response = await api.put(`/produtores/${produtorId}/`, this.editFormData);
        if (response.status === 200) {
          alert('Produtor atualizado com sucesso!');
          this.fetchProdutores();
          this.cancelEdit();
        } else {
          alert('Erro ao atualizar produtor.');
        }
      } catch (error) {
        console.error('Erro ao atualizar produtor:', error);
        alert('Erro ao atualizar produtor. Verifique o console para mais detalhes.');
      }
    },
    // Deleta um produtor
    async deleteProdutor(produtorId) {
      if (!confirm('Tem certeza que deseja deletar este produtor?')) {
        return;
      }
      try {
        const response = await api.delete(`/produtores/${produtorId}/`);
        if (response.status === 204) {
          alert('Produtor deletado com sucesso!');
          this.fetchProdutores();
        } else {
          alert('Erro ao deletar produtor.');
        }
      } catch (error) {
        console.error('Erro ao deletar produtor:', error);
        alert('Erro ao deletar produtor. Verifique o console para mais detalhes.');
      }
    },
  },
  created() {
    this.fetchUsuarios();
    this.fetchProdutores();
  }
};
</script>

<style scoped>
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

.btn-submit, .btn-cancel, .btn-edit, .btn-delete {
  padding: 10px 15px;
  margin-top: 10px;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

.btn-submit {
  background-color: #007bff;
}

.btn-cancel {
  background-color: #ffc107;
  color: #212529;
}

.btn-edit {
  background-color: #28a745;
}

.btn-delete {
  background-color: #dc3545;
}

.btn-submit:hover {
  background-color: #0056b3;
}

.btn-cancel:hover {
  background-color: #e0a800;
}

.btn-edit:hover {
  background-color: #218838;
}

.btn-delete:hover {
  background-color: #c82333;
}

.producer-list {
  margin-top: 20px;
}

.produtor-item {
  background-color: #fff;
  padding: 15px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.produtor-item p {
  margin: 5px 0;
}

.produtor-item button {
  margin-right: 10px;
}
</style>
