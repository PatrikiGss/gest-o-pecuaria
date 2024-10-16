<template>
  <div id="app">
    <!-- Exibe a navbar se o usuário estiver autenticado -->
    <nav v-if="isAuthenticated" class="nav-bar">
      <div class="nav-container">
        <div class="dropdown">
          <button class="btn dropdown-toggle nav-button" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
            ☰
          </button>
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
        <span class="current-name">{{ currentName }}</span>
      </div>

      <div class="user-info">
        <!-- Exibe o nome do usuário autenticado -->
        <span class="user-name">{{ nome }}</span>
        <!-- Exibe o botão de logout com funcionalidade de confirmação -->
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
      nome: 'Usuário',  // Nome do usuário logado
      isAuthenticated: false  // Controle de autenticação
    };
  },
  watch: {
    // Atualiza o nome da rota quando a rota muda
    $route(to) {
      this.currentName = to.name;
    }
  },
  mounted() {
    // Verifica a autenticação ao carregar o componente
    this.checkAuthentication();
    // Recupera o nome do usuário do localStorage
    this.nome = localStorage.getItem('nome_usuario') || 'Usuário';
    // Revalida a cada 3 segundos para verificar se o token ainda está presente
    this.authCheckInterval = setInterval(this.checkAuthentication, 3000);
  },
  beforeUnmount() {
    // Limpa o intervalo quando o componente for destruído
    clearInterval(this.authCheckInterval);
  },
  methods: {
    // Verifica se o token de autenticação está presente no localStorage
    checkAuthentication() {
      this.isAuthenticated = !!localStorage.getItem('access_token');  // Verifica se o token de acesso existe
    },
    // Lógica para confirmar e realizar o logout
    confirmLogout() {
      if (confirm("Você deseja encerrar a sessão?")) {
        this.logoutUsuario();  // Executa o logout se o usuário confirmar
      }
    },
    // Lógica de logout
    logoutUsuario() {
      // Remove o token do localStorage
      localStorage.removeItem('access_token');
      localStorage.removeItem('nome_usuario');
      this.isAuthenticated = false;
      // Redireciona para a tela de login ou outra rota adequada
      this.$router.push('/');
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
  color: black !important; /* Força a cor preta no botão de logout */
  border: none;
  padding: 5px 10px;
  margin-right: 20px;
}

.logout-button:hover {
  background-color: #ff4d4d;
  color: rgb(32, 22, 22) !important; /* Muda a cor ao passar o mouse */
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
