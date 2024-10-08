<template>
  <div id="app">
    <nav v-if="isAuthenticated" class="nav-bar">
      <router-link v-if="!isAuthenticated" class="dropdown-item" to="/">Home</router-link>
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
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      currentName: '',
      isAuthenticated: false // Inicializa como falso
    };
  },
  watch: {
    $route(to) {
      this.currentName = to.name;
    }
  },
  mounted() {
    // Verifica se o token está presente no localStorage
    this.checkAuthentication();
    // Verifica a cada 3 segundos se o token ainda está presente
    this.authCheckInterval = setInterval(this.checkAuthentication, 3000);
  },
  beforeUnmount() {
    // Limpa o intervalo quando o componente é destruído
    clearInterval(this.authCheckInterval);
  },
  methods: {
    // Verifica se o token está presente no localStorage
    checkAuthentication() {
      this.isAuthenticated = !!localStorage.getItem('token');
    },
    // Método de logout
    logout() {
      localStorage.removeItem('token'); // Remove o token
      this.checkAuthentication(); // Atualiza o estado
      this.$router.push('/'); // Redireciona para a página inicial ou de login
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

.nav-bar {
  background-color: rgb(107, 99, 99); /* Cor escura para a barra */
  width: 100%;
  padding: 10px 0; /* Espaçamento na vertical */
}

.nav-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 0 30px; /* Ajuste de padding lateral */
}

.nav-button {
  background-color: black;
  color: white;
  border: none;
  margin-right: 10px;
}

.nav-button:hover {
  background-color: #666;
}

.current-name {
  margin-left: 10px;
  color: white;
  font-weight: bold;
}

.dropdown-menu {
  text-align: left;
}
</style>
