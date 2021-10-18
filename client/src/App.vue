<template>
  <v-app>
    <Nav/>
    <v-app-bar>
   
      <v-spacer></v-spacer>
        <v-icon></v-icon>
    </v-app-bar>
    <v-main>
    <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

import Nav from "./components/Nav.vue"
export default {
  name: 'App',

  components: {
  Nav
  },

  data: () => ({
    //
  }),
};
</script>
