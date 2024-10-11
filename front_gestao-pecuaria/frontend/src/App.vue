<template>
  <div id="app">
    <nav v-if="isAuthenticated" class="nav-bar">
      <!-- Container para o dropdown e nome da rota atual -->
      <div class="nav-container">
        <div class="dropdown">
          <!-- Botão de dropdown com o ícone de menu -->
          <button class="btn dropdown-toggle nav-button" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
            ☰
          </button>
          <!-- Itens do dropdown -->
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <li><router-link class="dropdown-item" to="/">Home</router-link></li>
            <li><router-link class="dropdown-item" to="/tela-usuario">Usuário</router-link></li>
            <li><router-link class="dropdown-item" to="/tela-produtor">Produtor</router-link></li>
            <li><router-link class="dropdown-item" to="/tela-Propriedade">Propriedade</router-link></li>
            <li><router-link class="dropdown-item" to="/tela-Laboratorio">Laboratório</router-link></li>
            <li><router-link class="dropdown-item" to="/tela-cultura">Cultura</router-link></li>
            <li><router-link class="dropdown-item" to="/tela-analise-solo">Análise Solo</router-link></li>
            <li><router-link class="dropdown-item" to="/tela-recomendação">Recomendação</router-link></li>
          </ul>
        </div>
        <!-- Exibição do nome da rota atual -->
        <span class="current-name">{{ currentName }}</span>
      </div>

      <!-- Container para o nome do usuário e botão de logout -->
      <div class="user-info">
        <!-- Nome do usuário logado -->
        <span class="user-name">{{ nome }}</span>
        <!-- Botão de logout -->
        <button class="btn logout-button" @click="confirmLogout">Logout</button>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      currentName: '',  // Armazena o nome da rota atual
      nome: 'Usuario',  // Armazena o nome do usuário da sessão
      isAuthenticated: false  // Indica se o usuário está autenticado
    };
  },
  watch: {
    // Atualiza o nome da rota quando a rota muda
    $route(to) {
      this.currentName = to.name;
    }
  },
  mounted() {
    // Verifica se o token de autenticação está no localStorage
    this.checkAuthentication();
    // Recupera o nome do usuário do localStorage (ou usa "Usuário" como padrão)
    this.userName = localStorage.getItem('nome') || 'Usuário';
    // Verifica a cada 3 segundos se o token de autenticação ainda está presente
    this.authCheckInterval = setInterval(this.checkAuthentication, 3000);
  },
  beforeUnmount() {
    // Limpa o intervalo quando o componente é destruído
    clearInterval(this.authCheckInterval);
  },
  methods: {
    // Verifica se o token de autenticação está no localStorage
    checkAuthentication() {
      this.isAuthenticated = !!localStorage.getItem('token');
    },
    // Método para confirmar o logout
    confirmLogout() {
      if (window.confirm('Você realmente deseja fazer logout?')) {
        this.logout();
      }
    },
    // Realiza o logout removendo o token e redirecionando para a página inicial nao usando a rota de logout
    logout() {
      localStorage.removeItem('token');  // Remove o token
      this.checkAuthentication();  // Atualiza o estado de autenticação
      this.$router.push('/');  // Redireciona para a página de login
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

/* Barra de navegação */
.nav-bar {
  background-color: rgb(107, 99, 99); /* Cor escura para a barra */
  width: 100%;
  padding: 10px 0; /* Espaçamento na vertical */
  display: flex;
  justify-content: space-between; /* Coloca os itens nas extremidades */
  align-items: center; /* Centraliza verticalmente */
}

/* Container do dropdown e nome da rota */
.nav-container {
  display: flex;
  align-items: center;
}

/* Botão de navegação (dropdown) */
.nav-button {
  background-color: black;
  color: white;
  border: none;
  margin-left: 20px;
}

.nav-button:hover {
  background-color: #666;
}

/* Container para o nome do usuário e botão de logout */
.user-info {
  display: flex;
  align-items: center;
}

/* Nome do usuário */
.user-name {
  margin-right: 10px;
  color: white;
  font-weight: bold;
}

/* Botão de logout */
.logout-button {
  background-color: transparent;
  color: black !important; /* Força a cor branca no botão de logout */
  border: none;
  padding: 5px 10px;
  margin-right: 20px;
}

.logout-button:hover {
  background-color: #ff4d4d;
  color: rgb(32, 22, 22) !important; /* Força a cor branca ao passar o mouse */
}

/* Nome da rota atual */
.current-name {
  margin-left: 10px;
  color: white;
  font-weight: bold;
}

/* Estilo do dropdown */
.dropdown-menu {
  text-align: left;
}
</style>
