import VueRouter from 'vue-router'
import Home from './pages/Home'
import Profile from './pages/Profile'
import Register from './pages/Register'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/profile', component: Profile, name: 'Profile' },
  { path: '/register', component: Register, name: 'Register' }
]

export default new VueRouter({ routes, mode: 'history' })
