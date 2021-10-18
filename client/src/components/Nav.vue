<template>
<!-- <div>
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
</div> -->
<v-card>
  <v-toolbar
  color="cyan"
  dark
  flat>
    <v-app-bar-nav-icon ></v-app-bar-nav-icon>
    <v-toolbar-title>ZeroWaste</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
    </v-btn>
        <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
      <template v-slot:extension>
        <v-tabs
          show-arrows
          fixed-tabs>
        <v-tabs-slider color="yellow"></v-tabs-slider>
        <v-tab><router-link  class="text-decoration-none" to="/">Home</router-link></v-tab>
        <v-tab><router-link  class="text-decoration-none" to="/listings">Listings</router-link></v-tab>
        <v-tab><router-link  class="text-decoration-none" to="/register">Register</router-link></v-tab>
        <v-tab> <router-link class="text-decoration-none" to="/profile" v-if="authenticated">{{ name }}'s Profile</router-link></v-tab>
        <v-tab> <v-btn v-if="authenticated" @click="signOut">Sign Out</v-btn></v-tab>
        </v-tabs>
      </template>
  </v-toolbar>
</v-card>
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