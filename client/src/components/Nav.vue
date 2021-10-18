<template>
<div>
  <v-app-bar-nav-icon class="grey--text"></v-app-bar-nav-icon>
<v-toolbar-title class="grey-text">
  <span class="font-weight-light">ZeroWaste</span>
</v-toolbar-title>
<nav>
<v-navigation-drawer permanent>
  <v-list >
  <v-list-item-group color='primary'>
  <router-link  class="text-decoration-none" to="/">Home</router-link>
  <router-link  class="text-decoration-none" to="/listings">Listings</router-link>
  <router-link  class="text-decoration-none" to="/register">Register</router-link>
  <router-link class="text-decoration-none" to="/profile" v-if="authenticated">{{ name }}'s Profile</router-link>
  <v-btn v-if="authenticated" @click="signOut">Sign Out</v-btn>
  </v-list-item-group>
  </v-list>
</v-navigation-drawer>
</nav>
</div>
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