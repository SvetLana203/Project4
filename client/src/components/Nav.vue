<template>
<!-- <nav> -->
<!-- <v-app-bar  app>
  <v-app-bar-nav-icon class="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon>
<v-toolbar-title class="text-uppercase grey-text">
  <span class="font-weight-light">ZeroWaste</span>
</v-toolbar-title>
</v-app-bar> -->

<v-navigation-drawer  clipped
        
        width=240 absolute permanent>
  <v-list
            flat dense nav class="py-1"
        >
        <v-list-item-group color='primary' mandatory>
  <v-toolbar-title><router-link  to="/">Home</router-link></v-toolbar-title>
  <v-toolbar-title><router-link  to="/listings">Listings</router-link></v-toolbar-title>
  <v-toolbar-title><router-link  to="/register">Register</router-link></v-toolbar-title>
  <v-toolbar-title><router-link  to="/profile" v-if="authenticated">{{ name }}'s Profile</router-link></v-toolbar-title>
  <v-btn v-if="authenticated" @click="signOut">Sign Out</v-btn>
  </v-list-item-group>
  </v-list>
</v-navigation-drawer>
<!-- </nav> -->
</template>

<script>
export default {
  name: "Nav",
  data: () => ({
    authenticated: false,
    name: ""
  }),
  mounted: function () {
    const authenticated = localStorage.getItem("authenticated");
    if (authenticated) {
      this.name = localStorage.getItem("name");
      this.authenticated = true;
    }
  },
  methods: {
    signOut() {
      this.authenticated = false;
      this.name = "";
      this.$emit("signOut");
    },
  },
}
</script>


<style scoped>

</style>