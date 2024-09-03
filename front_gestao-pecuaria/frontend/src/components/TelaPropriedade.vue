<template>
  <div class="form-container">
    <h1>Cadastro de Propriedades</h1>
    <form @submit.prevent="submitForm" class="producer-form">
      <div class="form-group">
        <label for="produtor">Produtor:</label>
        <select id="produtor" v-model="formData.produtor" class="form-control">
          <option v-for="produtor in produtores" :key="produtor.id" :value="produtor.id">
            {{ produtor.nome }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" v-model="formData.nome" class="form-control" placeholder="nome da propiedade:">
      </div>

      <div class="form-group">
        <label for="longitude">Longitude:</label>
        <input type="text" id="longitude" v-model="formData.longitude" class="form-control" placeholder="ex: 12.3456789">
      </div>

      <div class="form-group">
        <label for="latitude">Latitude:</label>
        <input type="text" id="latitude" v-model="formData.latitude" class="form-control"  placeholder="ex: 98.7654321">
      </div>

      <div class="form-group">
        <label for="endereco">Endereço:</label>
        <input type="text" id="endereco" v-model="formData.endereco" class="form-control" placeholder="digite o endereço:">
      </div>

      <div class="form-group">
        <label for="cidade">Cidade:</label>
        <input type="text" id="cidade" v-model="formData.cidade" class="form-control" placeholder=" digite a cidade: ">
      </div>

      <div class="form-group">
        <label for="estado">Estado:</label>
        <input type="text" id="estado" v-model="formData.estado" class="form-control" placeholder=" ex: SC, PR, ES, SP">
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
        produtor: null,
        nome: '',
        longitude: '',
        latitude: '',
        endereco: '',
        cidade: '',
        estado: '',
      },
      propriedades: [],
      produtores: [],
    };
  },
  methods: {
    async fetchProdutores() {
      try {
        const response = await api.get('/produtores/');
        this.produtores = response.data;
      } catch (error) {
        console.error('Erro ao buscar produtores:', error);
      }
    },
    async submitForm() {
    try {
        console.log('Dados a serem enviados:', this.formData);
        const response = await api.post('/propriedades/', this.formData);
        if (response.status === 201) {
            alert('Propriedade cadastrada com sucesso!');
            this.propriedades.push(response.data);
        } else {
            alert('Erro ao cadastrar propriedade.');
        }
    } catch (error) {
        console.error('Erro ao enviar requisição:', error.response.data);
        alert('Erro ao enviar requisição. Verifique o console para mais detalhes.');
    }
}

  },
  created() {
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

.properties-list {
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
