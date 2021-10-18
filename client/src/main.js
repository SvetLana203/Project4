import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import vuetify from './plugins/vuetify'
import Vuetify from 'vuetify/lib'

Vue.config.productionTip = false
Vue.use(VueRouter, Vuetify)
new Vue({
  render: h => h(App),
  vuetify,
  router
}).$mount('#app')
