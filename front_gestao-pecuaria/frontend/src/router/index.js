import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TelaUsuario from '../components/TelaUsuario.vue'
import TelaProdutor from '../components/TelaProdutor.vue'
import TelaPropriedade from '@/components/TelaPropriedade.vue'
import TelaLaboratorio from '@/components/TelaLaboratorio.vue'
import TelaCultura from '@/components/TelaCultura.vue'
import TelaAnaliseSolo from '../components/TelaAnaliseSolo.vue'
import TelaRecomendações from '@/components/TelaRecomendações.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/tela-usuario',
    name: 'Usuario',
    component: TelaUsuario
  },
  {
    path: '/tela-produtor',
    name: 'Produtor',
    component: TelaProdutor
  },
  {
    path: '/tela-Propriedade',
    name: 'Propriedade',
   component: TelaPropriedade
  },
    {
    path: '/tela-Laboratorio',
    name: 'Laboratorio',
    component: TelaLaboratorio
    },
      {
   path: '/tela-Cultura',
   name: 'Cultura',
 component: TelaCultura
  },
  {
    path: '/tela-Analise-Solo',
   name: 'AnaliseSolo',
   component: TelaAnaliseSolo
  },
  {
    path: '/tela-recomendação',
    name: 'Recomendações',
    component: TelaRecomendações,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
