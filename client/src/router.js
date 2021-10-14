import VueRouter from 'vue-router'
import Home from './pages/Home'
import Profile from './pages/Profile'
import Register from './pages/Register'
import ListItems from './pages/ListItems'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/profile', component: Profile, name: 'Profile' },
  { path: '/register', component: Register, name: 'Register' },
  { path: '/listings', component: ListItems, name: 'ListItems' }
]

export default new VueRouter({ routes, mode: 'history' })
