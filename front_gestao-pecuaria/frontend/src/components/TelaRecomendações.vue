<template>
  <div class="form-container">
    <h1>Cadastro da Recomendação</h1>
    <form @submit.prevent="submitForm" class="analise-solo-form">
      <div class="form-group">
        <label for="analisesSolo">Análise de Solo:</label>
        <select id="analisesSolo" v-model="formData.analiseSolo" class="form-control">
          <option v-for="analiseSolo in analisesSolo" :key="analiseSolo.id" :value="analiseSolo.id">
            {{ analiseSolo.id }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="camada_correcao">Camada de Correção:</label>
        <input type="text" id="camada_correcao" v-model="formData.camada_correcao" class="form-control" placeholder="Ex: Camada 1">
      </div>

      <div class="form-group">
        <label for="calcario_calcitico">Calcário Calcitico:</label>
        <input type="number" step="0.01" id="calcario_calcitico" v-model="formData.calcario_calcitico" class="form-control" placeholder="Ex: 10.50">
      </div>

      <div class="form-group">
        <label for="calcario_dolomitico">Calcário Dolomítico:</label>
        <input type="number" step="0.01" id="calcario_dolomitico" v-model="formData.calcario_dolomitico" class="form-control" placeholder="Ex: 10.50">
      </div>

      <div class="form-group">
        <label for="calcario_magnesiano">Calcário Magnesiano:</label>
        <input type="number" step="0.01" id="calcario_magnesiano" v-model="formData.calcario_magnesiano" class="form-control" placeholder="Ex: 10.50">
      </div>

      <div class="form-group">
        <label for="gesso">Gesso:</label>
        <input type="number" step="0.01" id="gesso" v-model="formData.gesso" class="form-control" placeholder="Ex: 10.50">
      </div>

      <div class="form-group">
        <label for="kcl">KCl:</label>
        <input type="number" step="0.01" id="kcl" v-model="formData.kcl" class="form-control" placeholder="Ex: 10.50">
      </div>

      <div class="form-group">
        <label for="p2o5">P2O5:</label>
        <input type="number" step="0.01" id="p2o5" v-model="formData.p2o5" class="form-control" placeholder="Ex: 10.50">
      </div>

      <div class="form-group">
        <label for="n">N:</label>
        <input type="number" step="0.01" id="n" v-model="formData.n" class="form-control" placeholder="Ex: 10.50">
      </div>

      <div class="form-group">
        <label for="s">S:</label>
        <input type="number" step="0.01" id="s" v-model="formData.s" class="form-control" placeholder="Ex: 10.50">
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
        analiseSolo: null,
        camada_correcao: '',
        calcario_calcitico: '',
        calcario_dolomitico: '',
        calcario_magnesiano: '',
        gesso: '',
        kcl: '',
        p2o5: '',
        n: '',
        s: '',
      },
      analisesSolo: [],
      recomendacoes: [],
    };
  },
  methods: {
    async fetchAnalisesSolo() {
      try {
        const response = await api.get('/analisesolo/');
        this.analisesSolo = response.data;
      } catch (error) {
        console.error('Erro ao buscar análises de solo:', error);
      }
    },
    async submitForm() {
      try {
    const response = await api.post('/recomendacoes/', this.formData);
    if (response.status === 201) {
      alert('Recomendação cadastrada com sucesso!');
      this.recomendacoes.push(response.data);
    } else {
      alert('Erro ao cadastrar a recomendação. Tente novamente mais tarde.');
    }
  } catch (error) {
    console.error('Erro ao enviar requisição:', error);
    alert('Erro ao enviar requisição. Verifique o console para mais detalhes.');
      }
    },
  },
  created() {
    this.fetchAnalisesSolo();
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

.analise-solo-form {
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
</style>
