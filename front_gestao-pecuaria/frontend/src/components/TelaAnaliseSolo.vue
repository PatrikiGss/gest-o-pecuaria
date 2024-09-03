<template>
  <div class="form-container">
    <h1>Cadastro de Análise de Solo</h1>
    <form @submit.prevent="submitForm" class="analise-solo-form">
      <div class="form-group">
        <label for="laboratorio">Laboratório:</label>
        <select id="laboratorio" v-model="formData.laboratorio" class="form-control">
          <option v-for="laboratorio in laboratorios" :key="laboratorio.id" :value="laboratorio.id">
            {{ laboratorio.nome }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="propriedade">Propriedade:</label>
        <select id="propriedade" v-model="formData.propriedade" class="form-control">
          <option v-for="propriedade in propriedades" :key="propriedade.id" :value="propriedade.id">
            {{ propriedade.nome }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="cultura">Cultura:</label>
        <select id="cultura" v-model="formData.cultura" class="form-control">
          <option v-for="cultura in culturas" :key="cultura.id" :value="cultura.id">
            {{ cultura.nome }}
          </option>
        </select>
      </div>

      <div class="form-group">
    <label for="data">Data:</label>
    <input type="date" id="data" v-model="formData.data" class="form-control">
  </div>

      <div class="form-group">
        <label for="gleba">Gleba:</label>
        <input type="text" id="gleba" v-model="formData.gleba" class="form-control" placeholder="Ex: Gleba A">
      </div>

      <div class="form-group">
        <label for="area">Área (hectares):</label>
        <input type="number" step="0.01" id="area" v-model="formData.area" class="form-control" placeholder="Ex: 10.50">
      </div>

      <div class="form-group">
        <label for="laudo">Laudo:</label>
        <textarea id="laudo" v-model="formData.laudo" class="form-control" placeholder="Insira o laudo"></textarea>
      </div>

      <div class="form-group">
        <label for="ph_h2o">pH em H2O:</label>
        <input type="number" step="0.01" id="ph_h2o" v-model="formData.ph_h2o" class="form-control" placeholder="Ex: 5.5">
      </div>

      <div class="form-group">
        <label for="s">Enxofre (S):</label>
        <input type="number" step="0.01" id="s" v-model="formData.s" class="form-control" placeholder="Ex: 12.5">
      </div>

      <div class="form-group">
        <label for="p">Fósforo (P):</label>
        <input type="number" step="0.01" id="p" v-model="formData.p" class="form-control" placeholder="Ex: 5.0">
      </div>

      <div class="form-group">
      <label for="k">Potássio (K):</label>
      <input type="number" step="0.01" id="k" v-model="formData.k" class="form-control" placeholder="Ex: 0.05">
      </div>


      <div class="form-group">
        <label for="ca">Cálcio (Ca):</label>
        <input type="number" step="0.01" id="ca" v-model="formData.ca" class="form-control" placeholder="Ex: 3.0">
      </div>

      <div class="form-group">
      <label for="mg">Magnésio (Mg):</label>
      <input type="number" step="0.01" id="mg" v-model="formData.mg" class="form-control" placeholder="Ex: 1.5">
    </div>

    <div class="form-group">
      <label for="na">Sódio (Na):</label>
      <input type="number" step="0.01" id="na" v-model="formData.na" class="form-control" placeholder="Ex: 0.5">
    </div>

    <div class="form-group">
      <label for="al">Alumínio (Al):</label>
      <input type="number" step="0.01" id="al" v-model="formData.al" class="form-control" placeholder="Ex: 0.2">
    </div>

    <div class="form-group">
      <label for="h">H:</label>
      <input type="number" step="0.01" id="h" v-model="formData.h" class="form-control" placeholder="Ex: 1.0">
    </div>

    <div class="form-group">
      <label for="materia_organica">Matéria Orgânica:</label>
      <input type="number" step="0.01" id="materia_organica" v-model="formData.materia_organica" class="form-control" placeholder="Ex: 2.0">
    </div>

    <div class="form-group">
      <label for="areia">Areia:</label>
      <input type="number" step="0.01" id="areia" v-model="formData.areia" class="form-control" placeholder="Ex: 45.0">
    </div>

    <div class="form-group">
      <label for="silte">Silte:</label>
      <input type="number" step="0.01" id="silte" v-model="formData.silte" class="form-control" placeholder="Ex: 30.0">
    </div>

    <div class="form-group">
      <label for="argila">Argila:</label>
      <input type="number" step="0.01" id="argila" v-model="formData.argila" class="form-control" placeholder="Ex: 25.0">
    </div>

    <div class="form-group">
      <label for="mn">Manganês (Mn):</label>
      <input type="number" step="0.01" id="mn" v-model="formData.mn" class="form-control" placeholder="Ex: 0.02">
    </div>

    <div class="form-group">
      <label for="fe">Ferro (Fe):</label>
      <input type="number" step="0.01" id="fe" v-model="formData.fe" class="form-control" placeholder="Ex: 0.10">
    </div>

    <div class="form-group">
      <label for="cu">Cobre (Cu):</label>
      <input type="number" step="0.01" id="cu" v-model="formData.cu" class="form-control" placeholder="Ex: 0.05">
    </div>

    <div class="form-group">
      <label for="zn">Zinco (Zn):</label>
      <input type="number" step="0.01" id="zn" v-model="formData.zn" class="form-control" placeholder="Ex: 0.10">
    </div>

    <div class="form-group">
      <label for="b">Boro (B):</label>
      <input type="number" step="0.01" id="b" v-model="formData.b" class="form-control" placeholder="Ex: 0.02">
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
      laboratorio: null,
      propriedade: null,
      cultura: null,
      data: '',
      gleba: '',
      area: '',
      laudo: '',
      ph_h2o: '',
      s: '',
      p: '',
      k: '',
      ca: '',
      mg: '',
      na: '',
      al: '',
      h: '',
      materia_organica: '',
      areia: '',
      silte: '',
      argila: '',
      mn: '',
      fe: '',
      cu: '',
      zn: '',
      b: '',
    },
    analisesSolo: [],
    laboratorios: [],
    propriedades: [],
    culturas: [],
  };
},
  methods: {
    async fetchLaboratorios() {
      try {
        const response = await api.get('/laboratorios/');
        this.laboratorios = response.data;
      } catch (error) {
        console.error('Erro ao buscar laboratórios:', error);
      }
    },
    async fetchPropriedades() {
      try {
        const response = await api.get('/propriedades/');
        this.propriedades = response.data;
      } catch (error) {
        console.error('Erro ao buscar propriedades:', error);
      }
    },
    async fetchCulturas() {
      try {
        const response = await api.get('/culturas/');
        this.culturas = response.data;
      } catch (error) {
        console.error('Erro ao buscar culturas:', error);
      }
    },
    async submitForm() {
      try {
        const response = await api.post('/analisesolo/', this.formData);
        if (response.status === 201) {
          alert('Análise de Solo cadastrada com sucesso!');
          this.analisesSolo.push(response.data);
        } else {
          alert('Erro ao cadastrar análise de solo. Tente novamente mais tarde.');
        }
      } catch (error) {
        console.error('Erro ao enviar requisição:', error);
        alert('Erro ao enviar requisição. Verifique o console para mais detalhes.');
      }
    },
  },
  created() {
    this.fetchLaboratorios();
    this.fetchPropriedades();
    this.fetchCulturas();
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

.analise-solo-list {
  margin-top: 20px;
}

.analise-item {
  background-color: #fff;
  padding: 10px;
  margin-bottom: 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
</style>