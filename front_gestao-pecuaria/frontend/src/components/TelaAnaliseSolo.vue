<template>
  <div>
    <br>
    <br>
    <h1 v-if="!showForm" class="mt-4"><br>Lista de Analises de Solo</h1>
    <br>
    <div br class="form-container"><br>
      <h1></h1>
      
      <!-- Formulário de cadastro/edição de analises de solo -->
      <div v-if="showForm" class="form-container1">
        <h1>{{ editingSolo ? 'editar analise de solo': 'cadastro de analise de solo' }}</h1>
        <form @submit.prevent="submitForm" class="lab-form">
        <!-- Campo para o laboratorio -->
        <div class="mb-3">
          <label for="laboratorio" class="form-label">laboratorio</label>
          <select id="laboratorio" v-model="formData.laboratorio" class="form-control" required>
            <option disabled value="">Selecione um laboratorio</option>
            <option v-for="laboratorio in laboratorios" :key="laboratorio.id" :value="laboratorio.id">
              {{ laboratorio.nome }}
            </option>
          </select>
        </div>
                <!-- Campo para o propriedade -->
                <div class="mb-3">
          <label for="propriedade" class="form-label">propriedade</label>
          <select id="propriedade" v-model="formData.propriedade" class="form-control" required>
            <option disabled value="">Selecione uma propriedade</option>
            <option v-for="propriedade in propriedades" :key="propriedade.id" :value="propriedade.id">
              {{ propriedade.nome }}
            </option>
          </select>
        </div>
                <!-- Campo para o cultura -->
                <div class="mb-3">
          <label for="cultura" class="form-label">cultura</label>
          <select id="cultura" v-model="formData.cultura" class="form-control" required>
            <option disabled value="">Selecione uma cultura</option>
            <option v-for="cultura in culturas" :key="cultura.id" :value="cultura.id">
              {{ cultura.nome }}
            </option>
          </select>
        </div>
        <!-- Campo para o data -->
          <div class="mb-3">
          <label for="data" class="form-label">Data</label>
          <input type="date" class="form-control" id="data" v-model="formData.data" required />
        </div>
        <!-- Campo para o gleba -->
          <div class="mb-3">
          <label for="gleba" class="form-label">Gleba</label>
          <input type="text" class="form-control" id="gleba" v-model="formData.gleba" placeholder="Ex: Gleba A" required />
        </div>
        <!-- Campo para o area -->
        <div class="mb-3">
          <label for="area" class="form-label">Area</label>
          <input type="number" step="0.1" id="area" v-model="formData.area" placeholder="Ex: 10.50" required />
        </div>
        <div class="mb-3">
          <label for="laudo" class="form-label">laudo</label>
          <input type="laudo" id="laudo" v-model="formData.laudo" placeholder="Insira o laudo" required />
        </div>
        <!-- Campo para o ph_h2o -->
         <div class="mb-3">
          <label for="ph_h2o" class="form-label">pH em H2O</label>
          <input type="number" step="0.01" id="ph_h2o" v-model="formData.ph_h2o" placeholder="Ex: 5.5" required />
        </div>
        <!-- Campo para o s -->
        <div class="mb-3">
          <label for="s" class="form-label">Enxofre (S)</label>
          <input type="number" step="0.01" id="s" v-model="formData.s" placeholder="Ex: 12.5" required />
        </div>
        <!-- Campo para o p -->
        <div class="mb-3">
          <label for="p" class="form-label">Potássio (K)</label>
          <input type="number" step="0.01" id="p" v-model="formData.p" placeholder="Ex: 0.05" required />
        </div>
        <!-- Campo para o K -->
        <div class="mb-3">
          <label for="k" class="form-label">Fósforo (P)</label>
          <input type="number" step="0.01" id="k" v-model="formData.k" placeholder="Ex: 5.0" required />
        </div>
      <!-- Campo para o ca -->
      <div class="mb-3">
          <label for="ca" class="form-label">Cálcio (Ca)</label>
          <input type="number" step="0.01" id="ca" v-model="formData.ca" placeholder="Ex: 3.0" required />
        </div>
     <!-- Campo para o mg -->
      <div class="mb-3">
          <label for="mg" class="form-label">Magnésio (Mg)</label>
          <input type="number" step="0.01" id="mg" v-model="formData.mg" placeholder="Ex: 1.5" required />
        </div>
        <!-- Campo para o na -->
      <div class="mb-3">
          <label for="na" class="form-label">Sódio (Na)</label>
          <input type="number" step="0.01" id="na" v-model="formData.na" placeholder="Ex: 0.5" required />
        </div>
        <!-- Campo para o al -->
      <div class="mb-3">
          <label for="al" class="form-label">Alumínio (Al)</label>
          <input type="number" step="0.01" id="al" v-model="formData.al" placeholder="Ex: 0.2" required />
        </div>
        <!-- Campo para o h -->
      <div class="mb-3">
          <label for="h" class="form-label">Hidrogenio (H)</label>
          <input type="number" step="0.01" id="h" v-model="formData.h" placeholder="Ex: 1.0" required />
        </div>
        <!-- Campo para o materia organica -->
      <div class="mb-3">
          <label for="materia_organica" class="form-label">Matéria Orgânica</label>
          <input type="number" step="0.01" id="materia_organica" v-model="formData.materia_organica" placeholder="Ex: 2.0" required />
        </div>
        <!-- Campo para o areia -->
      <div class="mb-3">
          <label for="areia" class="form-label">Areia</label>
          <input type="number" step="0.01" id="areia" v-model="formData.areia" placeholder="Ex: 45.0" required />
        </div>
        <!-- Campo para o silte -->
      <div class="mb-3">
          <label for="silte" class="form-label">Silte</label>
          <input type="number" step="0.01" id="silte" v-model="formData.silte" placeholder="Ex: 30.0" required />
        </div>
        <!-- Campo para o argila -->
      <div class="mb-3">
          <label for="mn" class="form-label">Manganês (Mn)</label>
          <input type="number" step="0.01" id="mn" v-model="formData.mn" placeholder="Ex: 0.02" required />
        </div>
        <!-- Campo para o argila -->
      <div class="mb-3">
          <label for="argila" class="form-label">Argila</label>
          <input type="number" step="0.01" id="argila" v-model="formData.argila" placeholder="Ex: 25.0" required />
        </div>
        <!-- Campo para o fe -->
      <div class="mb-3">
          <label for="fe" class="form-label">Ferro (Fe)</label>
          <input type="number" step="0.01" id="fe" v-model="formData.fe" placeholder="Ex: 0.10" required />
        </div>
        <!-- Campo para o cu -->
      <div class="mb-3">
          <label for="cu" class="form-label">Cobre (Cu)</label>
          <input type="number" step="0.01" id="cu" v-model="formData.cu" placeholder="Ex: 0.05" required />
        </div>
        <!-- Campo para o zn -->
      <div class="mb-3">
          <label for="zn" class="form-label">Zinco (Zn)</label>
          <input type="number" step="0.01" id="zn" v-model="formData.zn" placeholder="Ex: 0.10" required />
        </div>
        <!-- Campo para o b -->
      <div class="mb-3">
          <label for="b" class="form-label">Boro (B)</label>
          <input type="number" step="0.01" id="b" v-model="formData.b" placeholder="Ex: 0.02" required />
        </div>
            <!-- Botões de ação -->
            <div class="button-group">
          <button @click="toggleForm" class="btn-back">Voltar</button>
          <button type="submit" class="btn-submit">{{ editingSolo ? 'Salvar' : 'Cadastrar' }}</button>
        </div>
      </form>
    </div>
        <!-- Botão para abrir o formulário de cadastro, sempre visível -->
    <div v-if="!showForm" class="button-container">
      <button @click="toggleForm" class="btn-submit">Cadastrar nova analise de solo</button>
    </div>

    <!-- Lista de Análises de Solo, oculta quando o formulário está ativo -->
    <div v-if="!showForm && analisesSolo.length" class="table-responsive mt-5">
      <table class="table table-bordered table-hover">
        <thead class="thead-dark">
          <tr>
            <th>Laboratório</th>
            <th>Propriedade</th>
            <th>Cultura</th>
            <th>Data</th>
            <th>Gleba</th>
            <th>Área</th>
            <th>Laudo</th>
            <th>pH H2O</th>
            <th>S (Enxofre)</th>
            <th>K (Potássio)</th>
            <th>P (Fósforo)</th>
            <th>Ca (Cálcio)</th>
            <th>Mg (Magnésio)</th>
            <th>Na (Sódio)</th>
            <th>Al (Alumínio)</th>
            <th>H (Hidrogênio)</th>
            <th>Matéria Orgânica</th>
            <th>Areia</th>
            <th>Silte</th>
            <th>Argila</th>
            <th>Mn (Manganês)</th>
            <th>Fe (Ferro)</th>
            <th>Cu (Cobre)</th>
            <th>Zn (Zinco)</th>
            <th>B (Boro)</th>
            <th>Ação</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="analisesolo in analisesSolo" :key="analisesolo.id">
            <td>{{ getlaboratorioNome(analisesolo.laboratorio) }}</td>
            <td>{{ getpropriedadeNome(analisesolo.propriedade) }}</td>
            <td>{{ getculturaNome(analisesolo.cultura) }}</td>
            <td>{{ analisesolo.data }}</td>
            <td>{{ analisesolo.gleba }}</td>
            <td>{{ analisesolo.area }}</td>
            <td>{{ analisesolo.laudo }}</td>
            <td>{{ analisesolo.ph_h2o }}</td>
            <td>{{ analisesolo.s }}</td>
            <td>{{ analisesolo.p }}</td>
            <td>{{ analisesolo.k }}</td>
            <td>{{ analisesolo.ca }}</td>
            <td>{{ analisesolo.mg }}</td>
            <td>{{ analisesolo.na }}</td>
            <td>{{ analisesolo.al }}</td>
            <td>{{ analisesolo.h }}</td>
            <td>{{ analisesolo.materia_organica }}</td>
            <td>{{ analisesolo.areia }}</td>
            <td>{{ analisesolo.silte }}</td>
            <td>{{ analisesolo.argila }}</td>
            <td>{{ analisesolo.mn }}</td>
            <td>{{ analisesolo.fe }}</td>
            <td>{{ analisesolo.cu }}</td>
            <td>{{ analisesolo.zn }}</td>
            <td>{{ analisesolo.b }}</td>
            <td>
              <button @click="startEditing(analisesolo)" class="btn-edit">🖊️</button>
              <button @click="deleteSolo(analisesolo.id)" class="btn-delete">🗑️</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="!showForm && !analisesSolo.length" class="mt-5">
      <p>Nenhuma análise de solo cadastrada.</p>
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
      showForm: false,
      editingSolo: false,
    };
  },
  methods: {
    // Alterna a exibição do formulário e reseta os dados
    toggleForm() {
      this.showForm = !this.showForm;
      this.editingSolo = false;
      this.formData = {
        laboratorio: '',
        propriedade: '',
        cultura: '',
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
      };
    },
    // Obtém o nome do laboratório a partir do ID
    getlaboratorioNome(laboratorioId) {
      const laboratorio = this.laboratorios.find(u => u.id === laboratorioId);
      return laboratorio ? laboratorio.nome : 'Desconhecido';
    },
    // Obtém o nome da propriedade a partir do ID
    getpropriedadeNome(propriedadeId) {
      const propriedade = this.propriedades.find(u => u.id === propriedadeId);
      return propriedade ? propriedade.nome : 'Desconhecido';
    },
    // Obtém o nome da cultura a partir do ID
    getculturaNome(culturaId) {
      const cultura = this.culturas.find(u => u.id === culturaId);
      return cultura ? cultura.nome : 'Desconhecido';
    },
    // Busca os dados dos laboratórios
    async fetchLaboratorios() {
      try {
        const response = await api.get('/laboratorios/');
        this.laboratorios = response.data;
      } catch (error) {
        console.error('Erro ao buscar laboratórios:', error);
      }
    },
    // Busca os dados das propriedades
    async fetchPropriedades() {
      try {
        const response = await api.get('/propriedades/');
        this.propriedades = response.data;
      } catch (error) {
        console.error('Erro ao buscar propriedades:', error);
      }
    },
    // Busca os dados das culturas
    async fetchCulturas() {
      try {
        const response = await api.get('/culturas/');
        this.culturas = response.data;
      } catch (error) {
        console.error('Erro ao buscar culturas:', error);
      }
    },
    // Busca as análises de solo
    async fetchAnaliseSolo() {
      try {
        const response = await api.get('/analisesolo/');
        this.analisesSolo = response.data;
      } catch (error) {
        console.error('Erro ao buscar análises de solo:', error);
      }
    },
    // Envia os dados do formulário
    async submitForm() {
      try {
        if (this.editingSolo) {
          const response = await api.put(`/analisesolo/${this.formData.id}/`, this.formData);
          if (response.status === 200) {
            alert('Análise de solo atualizada com sucesso!');
            this.fetchAnaliseSolo();
            this.toggleForm();
          } else {
            alert('Erro ao atualizar análise de solo.');
          }
        } else {
          const response = await api.post('/analisesolo/', this.formData);
          if (response.status === 201) {
            alert('Análise de solo cadastrada com sucesso!');
            this.analisesSolo.push(response.data);
            this.toggleForm();
          } else {
            alert('Erro ao cadastrar análise de solo. Tente novamente mais tarde.');
          }
        }
      } catch (error) {
        console.error('Erro ao enviar requisição:', error);
        alert('Erro ao enviar requisição. Verifique o console para mais detalhes.');
      }
    },
    // Inicia o modo de edição
    startEditing(analisesolo) {
      this.formData = { ...analisesolo };
      this.showForm = true;
      this.editingSolo = true;
    },
    // Deleta uma análise de solo
    async deleteSolo(analisesoloId) {
      if (!confirm('Tem certeza que deseja deletar esta análise de solo?')) return;
      try {
        const response = await api.delete(`/analisesolo/${analisesoloId}/`);
        if (response.status === 204) {
          alert('Análise de solo deletada com sucesso!');
          this.fetchAnaliseSolo();
        } else {
          alert('Erro ao deletar análise de solo.');
        }
      } catch (error) {
        console.error('Erro ao deletar análise de solo:', error);
        alert('Erro ao deletar análise de solo. Verifique o console para mais detalhes.');
      }
    },
  },
  mounted() {
    this.fetchLaboratorios();
    this.fetchPropriedades();
    this.fetchCulturas();
    this.fetchAnaliseSolo();
  }
};
</script>


<style scoped>

/* Container do formulário com sombra e borda */
.form-container {
  width: 100%;
  padding: 0 20px;
  background-color: whitesmoke;
  border: 2px solid grey;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Estilo do formulário de laboratório */
.lab-form {
  display: flex;
  flex-direction: column;
}

/* Estilo das linhas do formulário */
.form-row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

/* Grupo de campos do formulário, ajusta o tamanho das colunas */
.form-group {
  flex: 1 1 150px;
  min-width: 150px;
}

/* Grupo de botões, alinha os botões ao final */
.button-group {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}

/* Container de botões, alinha o texto à esquerda */
.button-container {
  text-align: left;
  margin-bottom: 20px;
}

/* Estilo das linhas da lista de usuários */
.user-info {
  display: flex;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid #ddd;
  position: relative;
}

/* Linha dos usuários, separadores entre colunas */
.user-info > div {
  position: relative;
  padding-right: 10px;
}

.user-info > div:not(:last-child)::after {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 1px;
  background-color: grey;
}

/* Botões estilizados para ações de formulário e lista */
.btn-submit, .btn-edit, .btn-delete, .btn-cancel, .btn-back {
  padding: 8px 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  margin-right: 5px;
}

/* Estilo dos botões de submit, back e edit */
.btn-submit, .btn-back, .btn-edit {
  background-color: #237837;
  color: white;
}

.btn-submit:hover, .btn-back:hover, .btn-edit:hover {
  background-color: #218838;
}

/* Estilo do botão de delete */
.btn-delete {
  background-color: #dc3545;
  color: white;
}

.btn-delete:hover {
  background-color: #c82333;
}

/* Estilo do botão de cancel */
.btn-cancel {
  background-color: #6c757d;
  color: white;
}

.btn-cancel:hover {
  background-color: #5a6268;
}

/* Estilo das labels dos campos do formulário */
.form-label {
  text-align: left;
  display: block;
  margin-bottom: 0.5rem;
}

/* Faz com que todos os inputs de texto e número ocupem 100% da largura */
.form-container input[type="text"],
.form-container input[type="number"],
.form-container input[type="date"],
.form-container select {
  width: 100%;
  box-sizing: border-box; /* Inclui padding e border na largura total */
}

/* Certifica-se de que os campos de formulário ocupem o máximo de espaço horizontal */
.lab-form .mb-3 {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.table-responsive {
  margin-top: 20px;
}
.table {
  border: 1px solid grey;
  background-color: whitesmoke;
}
.thead-dark th {
  background-color: whitesmoke;
  color: black;
}
</style>