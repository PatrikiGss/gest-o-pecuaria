import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TelaUsuario from '../components/TelaUsuario.vue'
import TelaProdutor from '../components/TelaProdutor.vue'
import TelaPropriedade from '@/components/TelaPropriedade.vue'
import TelaLaboratorio from '@/components/TelaLaboratorio.vue'
import TelaCultura from '@/components/TelaCultura.vue'
import TelaAnaliseSolo from '../components/TelaAnaliseSolo.vue'
import TelaRecomendacoes from '@/components/TelaRecomendacoes.vue'
import TelaCadastro from '@/components/TelaCadastro.vue'
import TelaEdicaoSenha from '@/components/TelaEdiçaoSenha.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/tela-usuario',
    name: 'usuario',
    component: TelaUsuario
  },
  {
    path: '/tela-produtor',
    name: 'produtor',
    component: TelaProdutor
  },
  {
    path: '/tela-propriedade',
    name: 'propriedade',
    component: TelaPropriedade
  },
  {
    path: '/tela-laboratorio',
    name: 'laboratorio',
    component: TelaLaboratorio
  },
  {
    path: '/tela-cultura',
    name: 'cultura',
    component: TelaCultura
  },
  {
    path: '/tela-analise-solo',
    name: 'analiseSolo',
    component: TelaAnaliseSolo
  },
  {
    path: '/tela-recomendacoes',
    name: 'recomendação',
    component: TelaRecomendacoes
  },
  {
    path: '/tela-cadastro',
    name: 'cadastro',
    component: TelaCadastro
  },
  {
    path: '/tela-edicao',
    name: 'edicaoSenha',
    component: TelaEdicaoSenha
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
