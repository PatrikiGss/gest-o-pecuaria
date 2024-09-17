<template>
  <div class="container-fluid">
    <!-- Título da página -->
    <h1></h1>
    <!-- Exibe o título "Lista de recomendações" se o formulário não estiver sendo exibido -->
    <h1 v-if="!showForm"><br>Lista de Recomendações </h1>
    <h1 v-if="!showForm"><br></h1>
    <!--formulario de cadastro/edição de recomendação-->
    <div v-if="showForm" class="form-container">
      <h1>{{ editingRec ? 'Editar Recomendação' : 'Cadastro de Recomendação' }}</h1>
      <form @submit.prevent="submitForm" class="recomendação-form">
        <!--campo para analise de solo-->
        <div class="mb-3">
          <label for="analisesolo" class="form-label">Analise de Solo</label>
          <select id="analisesolo" v-model="formData.analise_solo" class="form-control" required>
            <option v-for="analise in analise_solo" :key="analise.id" :value="analise.id">
              {{ analise.laudo }}
            </option>
          </select>
        </div>

        <!-- Campos para os dados da recomendação -->
        <div class="mb-3">
          <label for="camada_correcao" class="form-label">Camada de Correção</label>
          <input type="text" class="form-control" id="camada_correcao" v-model="formData.camada_correcao"
            placeholder="Informe a camada de correção">
        </div>

        <div class="mb-3">
          <label for="calcario_calcitico" class="form-label">Calcário Calcítico</label>
          <input type="text" class="form-control" id="calcario_calcitico" v-model="formData.calcario_calcitico"
            placeholder="Informe a quantidade de calcário calcítico">
        </div>

        <div class="mb-3">
          <label for="calcario_dolomitico" class="form-label">Calcário Dolomítico</label>
          <input type="text" class="form-control" id="calcario_dolomitico" v-model="formData.calcario_dolomitico"
            placeholder="Informe a quantidade de calcário dolomítico">
        </div>

        <div class="mb-3">
          <label for="calcario_magnesiano" class="form-label">Calcário Magnesiano</label>
          <input type="text" class="form-control" id="calcario_magnesiano" v-model="formData.calcario_magnesiano"
            placeholder="Informe a quantidade de calcário magnesiano">
        </div>

        <div class="mb-3">
          <label for="gesso" class="form-label">Gesso</label>
          <input type="text" class="form-control" id="gesso" v-model="formData.gesso"
            placeholder="Informe a quantidade de gesso">
        </div>

        <div class="mb-3">
          <label for="kcl" class="form-label">KCl</label>
          <input type="text" class="form-control" id="kcl" v-model="formData.kcl"
            placeholder="Informe a quantidade de KCl">
        </div>

        <div class="mb-3">
          <label for="p2o5" class="form-label">P2O5</label>
          <input type="text" class="form-control" id="p2o5" v-model="formData.p2o5"
            placeholder="Informe a quantidade de P2O5">
        </div>

        <div class="mb-3">
          <label for="n" class="form-label">Nitrogênio (N)</label>
          <input type="text" class="form-control" id="n" v-model="formData.n"
            placeholder="Informe a quantidade de Nitrogênio (N)">
        </div>

        <div class="mb-3">
          <label for="s" class="form-label">Enxofre (S)</label>
          <input type="text" class="form-control" id="s" v-model="formData.s"
            placeholder="Informe a quantidade de Enxofre (S)">
        </div>

        <!-- Grupo de botões -->
        <div class="button-group">
          <!-- Botão para voltar sem salvar alterações -->
          <button @click="toggleForm" class="btn-back">Voltar</button>
          <!-- Botão para enviar ou atualizar o formulário -->
          <button type="submit" class="btn-submit">{{ editingRec ? 'Atualizar' : 'Enviar' }}</button>
        </div>
      </form>
    </div>

    <!-- Lista de recomendações cadastradas -->
    <div v-else class="recomendacao-list-container">
      <!-- Botão para abrir o formulário de cadastro -->
      <div class="button-container">
        <button @click="toggleForm" class="btn-submit">Cadastrar Nova Recomendação</button>
      </div>

      <!-- Verifica se há recomendações para exibir -->
      <div v-if="recomendacoes.length">
        <div class="container-fluid">
          <!-- Cabeçalho da tabela de recomendações -->
          <div class="row font-weight-bold mb-2">
            <div class="col-12 col-sm-6 col-md-4 col-lg-2">Análise de Solo</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">Camada de Correção</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">Calcário Calcítico</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">Calcario Dolomitico</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">Calcario Magnesiano</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">Gesso</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">kcl</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">p2o5</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">n</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">s</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">Ações</div>
          </div>
          <!-- Loop para exibir cada recomendação na tabela -->
          <div v-for="recomendacao in recomendacoes" :key="recomendacao.id" class="row recomendacao-info mb-2">
            <div class="col-12 col-sm-6 col-md-4 col-lg-2">
              {{ getLaudoByAnaliseSoloId(recomendacao.analise_solo) }}
            </div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">{{ recomendacao.camada_correcao }}</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">{{ recomendacao.calcario_calcitico }}</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">{{ recomendacao.calcario_dolomitico }}</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">{{ recomendacao.calcario_magnesiano }}</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">{{ recomendacao.gesso }}</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">{{ recomendacao.kcl }}</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">{{ recomendacao.p2o5 }}</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">{{ recomendacao.n }}</div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">{{ recomendacao.s }}</div>
            <!-- Botões para editar e excluir recomendações -->
            <div class="col-12 col-sm-6 col-md-4 col-lg-1">
              <button @click="editRec(recomendacao)" class="btn-edit">🖊️</button>
              <button @click="deleteRec(recomendacao.id)" class="btn-delete">🗑️</button>
            </div>
          </div>
        </div>
      </div>
      <!-- Exibe mensagem se não houver recomendações cadastradas -->
      <div v-else>
        <p>Nenhuma recomendação encontrada.</p>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/interceptadorAxios'; // Importa o módulo para fazer requisições HTTP com Axios
export default {
  data() {
    return {
      showForm: false,
      formData: {  // Era FormData
        analisesolo: null,
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
      analisesolo: [],  // Lista de analises de solo
      recomendacoes: [],  // Lista de recomendações
      editingRec: null,  // Mantém o ID da recomendação que está sendo editada
    };
  }
  ,
  methods: {
    // Alterna a exibição do formulário de usuário
    toggleForm() {
      this.showForm = !this.showForm; // Inverte o estado do formulário
      this.clearForm(); // Limpa os dados do formulário
    },

    getLaudoByAnaliseSoloId(analisesoloId) {
      console.log('ID da análise de solo recebido:', analisesoloId);

      // Verifica se o array de análises de solo está carregado e contém elementos
      if (!Array.isArray(this.analise_solo) || this.analise_solo.length === 0) {
        console.log('Array analise_solo não carregado ou vazio');
        return 'desconhecido';  // Retorna um valor padrão
      }

      // Verifica se o ID da análise de solo é válido
      if (!analisesoloId) {
        console.log('ID da análise de solo não fornecido ou inválido');
        return 'ID inválido';  // Retorna mensagem para ID inválido
      }

      // Busca a análise de solo no array com base no ID fornecido
      const analise = this.analise_solo.find(a => {
        console.log(`Comparando ${String(a.id)} com ${String(analisesoloId)}`);
        return String(a.id) === String(analisesoloId);  // Converte ambos para string
      });

      // Se a análise for encontrada, retorna o laudo ou uma mensagem padrão se estiver ausente
      if (analise) {
        console.log('Laudo encontrado:', analise.laudo);
        return analise.laudo || 'Laudo não disponível';  // Retorna o laudo ou mensagem padrão
      } else {
        console.log('Análise de solo não encontrada para o ID:', analisesoloId);
        return 'Análise não encontrada';  // Mensagem padrão quando o ID não é encontrado
      }
    },




    // Busca todas as analises de solo
    async fetchAnaliseSolo() {
      try {
        const response = await api.get('/analisesolo/');
        console.log('Dados recebidos:', response.data);  // Debug para ver os dados recebidos
        this.analise_solo = response.data;  // Certifique-se de que os dados estão sendo atribuídos
      } catch (error) {
        console.error('Erro ao buscar análises de solo: ', error);
      }
    },
    // Busca todas as recomendações
    async fetchRecomendação() {
      try {
        const response = await api.get('/recomendacoes/');
        this.recomendacoes = response.data;
      } catch (error) {
        console.error('erro ao buscae recomendações: ', error);
      }
    },
    // Método para enviar o formulário
    async submitForm() {
      try {
        if (this.editingRec) {
          //atualiza uma recomendação ja existente
          const response = await api.put(`/recomendacoes/${this.editingRec}/`, this.formData);
          if (response.status === 200) {
            alert('recomendação atualizada com sucesso!');
          } else {
            alert('erro ao atualizar a recomendação.')
          }
        } else {
          // Cadastra uma nova recomendação
          const response = await api.post('/recomendacoes/', this.formData);
          if (response.status === 201) {
            alert(' recomendação foi cadastrada com sucesso!');
          } else {
            alert('recomendação nao pode ser cadastrada.');
          }
        }
        this.fetchRecomendação();// Atualiza a liste recoemndação
        this.showForm = false;// Oculta o formulário após o cadastro ou atualização
      } catch (error) {
        console.error('erro ao enviuar requisição:', error);
        alert('erro ao enviar requisauição. verifique o console')
      }
    },
    // Método para editar uma recomendação
    editRec(recomendacoes) {
      this.editingRec = recomendacoes.id;// Armazena o ID da recomendação que está sendo editada
      this.formData = { ...recomendacoes }; // Preenche o formulário com os dados da recomendação
      this.showForm = true; // Exibe o formulário para edição
    },
    // Método para limpar o formulário
    clearForm() {
      // Limpa os dados do formulário
      this.formData = {
        analisesolo: null,
        camada_correcao: '',
        calcario_calcitico: '',
        calcario_dolomitico: '',
        calcario_magnesiano: '',
        gesso: '',
        kcl: '',
        p2o5: '',
        n: '',
        s: '',
      };
      this.editingRec = null; //reseta estado da edição
    },
    // Método para excluir uma recomendação
    async deleteRec(id) {
      if (confirm('tem certeza que deseja excluir esta recomendação?')) {
        try {
          const response = await api.delete(`/recomendacoes/${id}/`);
          if (response.status === 204) {  // Status 204 indica sucesso sem conteúdo
            alert('Recomendação excluída com sucesso!');
            this.fetchRecomendação();  // Atualiza a lista após a exclusão
          } else {
            alert('Erro ao tentar excluir a recomendação.');
          }
        } catch (error) {
          console.error('Erro ao excluir a recomendação:', error);
          alert('Erro ao excluir a recomendação. Verifique o console.');
        }
      }
    }
  },
  mounted() {
    this.fetchAnaliseSolo();// Busca a lista de analises de solo quando o componente é criado
    this.fetchRecomendação();// Busca a lista de recomendações quando o componente é criado
  }
};
</script>

<style scoped>
/* Estilos do container principal */
.container-fluid {
  width: 100%;
  padding: 0 15px;
}

/* Estilos dos botões */
.button-container {
  text-align: left;
  margin-bottom: 20px;
}

/* Estilo para o container do formulário e da lista de usuários */
.form-container,
.recomendacao-list-container {
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  background-color: whitesmoke;
  border: 2px solid grey;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Estilos para a exibição das informações dos usuários */
.recomendacao-info {
  display: flex;
  align-items: center;
  padding: 10px 0;
  border-bottom: 1px solid #ddd;
  position: relative;
}

.recomendacao-info>div {
  position: relative;
  padding-right: 10px;
}

/* Linha vertical entre as colunas */
.recomendacao-info>div:not(:last-child)::after {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
  width: 1px;
  background-color: grey;
}

/* Estilos dos botões */
.btn-submit,
.btn-edit,
.btn-delete,
.btn-cancel,
.btn-back {
  padding: 8px 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  margin-right: 5px;
}

.btn-submit,
.btn-back,
.btn-edit {
  background-color: #237837;
  color: white;
}

.btn-submit:hover,
.btn-back:hover,
.btn-edit:hover {
  background-color: #218838;
}

.btn-delete {
  background-color: #dc3545;
  color: white;
}

.btn-delete:hover {
  background-color: #c82333;
}

/* Estilos do botão de cancelar */
.btn-cancel {
  background-color: #6c757d;
  color: white;
}

.btn-cancel:hover {
  background-color: #5a6268;
}

/* Estilos das labels do formulário */
.form-label {
  text-align: left;
  display: block;
  margin-bottom: 0.5rem;
}

/* Grupo de botões do formulário */
.button-group {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}

.button-group .btn-back {
  margin-right: 10px;
}
</style>
