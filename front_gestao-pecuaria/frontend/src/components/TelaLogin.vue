<template>
  <div class="login">
    <h1>Login</h1>
    <input class="input" v-model="email" type="text" placeholder="email">
    <br>
    <input class="input" v-model="password" :type="passwordType" placeholder="Password">
    <span class="toggle-password" @click="togglePasswordVisibility">
      <i :class="passwordType === 'password' ? 'fas fa-eye' : 'fas fa-eye-slash'"></i>
    </span>
    <br>
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    <div class="cadastro">
      <button class="btn-cadastro" @click="redirectToCadastro">cadastre-se</button>
    </div>
    <div class="envio">
      <button class="btn-envio" @click="loginUsuario">enviar</button>
    </div>
  </div>
</template>


<script>
import api from '@/interceptadorAxios'; // Usa o interceptador configurado

export default {
  data() {
    return {
      email: '',
      password: '',
      passwordType: 'password', // Controle de visibilidade da senha
      errorMessage: '', // Mensagem de erro para o usuário
    };
  },
  methods: {
    // Método de login do usuário
    async loginUsuario() {
      this.errorMessage = ''; // Limpa a mensagem de erro antes do login

      try {
        // Faz a requisição de login utilizando o interceptador
        const response = await api.post('/autenticacao/token/', {
          email: this.email,
          password: this.password,
        });

        // Verifica se a resposta foi bem-sucedida e contém os tokens
        if (response.status === 200 && response.data.access && response.data.refresh) {
          const accessToken = response.data.access;
          const refreshToken = response.data.refresh;

          // Armazena os tokens no localStorage
          localStorage.setItem('access_token', accessToken);
          localStorage.setItem('refresh_token', refreshToken);

          // Busca e armazena o nome do usuário
          const nomeUsuario = await this.obterNomeUsuario();
          localStorage.setItem('nome_usuario', nomeUsuario);

          // Redireciona para a tela de usuário
          this.$router.push('/tela-usuario');
          window.location.href = '/tela-usuario';
        } else {
          this.errorMessage = 'Falha ao obter os tokens de autenticação.';
        }
      } catch (error) {
        console.error('Erro ao realizar login:', error);
        this.errorMessage = 'Erro no login. Verifique suas credenciais.';
      }
    },

    // Método para buscar o nome do usuário logado
    async obterNomeUsuario() {
      try {
        const response = await api.get('/autenticacao/meuperfil/');
        return response.data.nome || 'Usuário';
      } catch (error) {
        console.error('Erro ao obter dados do usuário:', error);
        return 'Usuário';
      }
    },

    // Método para redirecionar para a tela de cadastro
    redirectToCadastro() {
      this.$router.push('/tela-cadastro');
    },

    // Alterna a visibilidade da senha
    togglePasswordVisibility() {
      this.passwordType = this.passwordType === 'password' ? 'text' : 'password';
    }
  }
};
</script>

<style scoped>
/* Mantemos o CSS original, garantindo que a aparência não seja alterada */
.login {
  background-color: rgba(0, 0, 0, 0.9);  /* Cor de fundo escura e semi-transparente */
  position: absolute;  /* Posiciona o login de forma absoluta */
  top: 50%;  /* Centraliza verticalmente */
  left: 50%;  /* Centraliza horizontalmente */
  transform: translate(-50%, -50%);  /* Ajusta o centro da caixa */
  padding: 80px;  /* Adiciona espaço interno */
  border-radius: 20px;  /* Bordas arredondadas */
  color: white;  /* Cor do texto */
}
.input {
  padding: 15px;
  border: none;
  font-size: 15px;
  border-radius: 10px;
  width: 100%; /* Certifica-se que os inputs ocupem toda a largura */
  margin-bottom: 20px; /* Adiciona espaçamento inferior para melhor alinhamento */
  box-sizing: border-box; /* Inclui padding e borda no cálculo da largura */
}

.toggle-password {
  position: absolute; /* Coloca o ícone no campo de senha de forma relativa */
  margin-left: -30px; /* Ajusta o ícone dentro do campo */
  cursor: pointer;
}

.login input[type="text"],
.login input[type="password"] {
  width: calc(100% - 40px); /* Ajusta a largura dos inputs levando em conta o ícone de senha */
  padding-right: 40px; /* Adiciona espaço à direita para o ícone */
}
.envio {
  text-align: left;  /* Alinha texto à esquerda */
  margin-bottom: 20px;  /* Espaço inferior */
}
.btn-envio {
  background-color: #237837;  /* Cor de fundo do botão de envio */
  border: none;  /* Remove a borda do botão */
  padding: 15px;  /* Espaço interno do botão */
  width: 100%;  /* Largura total */
  border-radius: 10px;  /* Bordas arredondadas */
  font-size: 15px;  /* Tamanho da fonte */
  cursor: pointer;  /* Cursor como ponteiro */
}
.cadastro {
  text-align: left;  /* Alinha texto à esquerda */
  margin-bottom: 20px;  /* Espaço inferior */
}
.btn-cadastro {
  background-color: transparent;  /* Remove o fundo do botão */
  color: white;  /* Cor do texto */
  border: none;  /* Remove a borda do botão */
  width: 100%;  /* Largura total */
  font-size: 15px;  /* Tamanho da fonte */
  cursor: pointer;  /* Cursor como ponteiro */
}
.btn-cadastro:hover {
  color: #ddd;  /* Muda a cor do texto no hover */
}
.btn-envio:hover {
  background-color: #218838;  /* Muda a cor de fundo no hover */
}

/* Estilização do ícone de visibilidade da senha */
.toggle-password {
  cursor: pointer;
  margin-left: 10px;
}

.error-message {
  color: red; /* Cor da mensagem de erro */
  margin-top: 10px;
  font-size: 14px;
}
</style>
