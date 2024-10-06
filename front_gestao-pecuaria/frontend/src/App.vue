<template>
  <div id="app">
    <!-- v-if="isAuthenticated" adicionar essa lionha no nav quando a auntenticação estiver funcionando-->
     <nav class="nav-bar" > 
      <div class="nav-container">
        <div class="dropdown">
          <button class="btn dropdown-toggle nav-button" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
            ☰
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <li><router-link class="dropdown-item" to="/">Home</router-link></li>
            <!--<li><router-link class="dropdown-item" to="/about">About</router-link></li>-->
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
      currentName: ''
    };
  },
  watch: {
    $route(to) {
      this.currentName = to.name;
    }
  },
  mounted() {
    this.currentPath = this.$route.path;
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
