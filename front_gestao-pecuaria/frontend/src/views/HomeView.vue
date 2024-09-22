<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> adicionar imagem aqui-->
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/TelaLogin.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
