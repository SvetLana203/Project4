<template>
<nav>
  <p class="link icon">ZeroWaste</p>
  <router-link class="link home" to="/">Home</router-link>
  <router-link class="link home" to="/listings">Listings</router-link>
  <router-link class="link home" to="/register">Register</router-link>
  <router-link class="link home" to="/profile" v-if="authenticated">{{ name }}'s Profile</router-link>
  <button v-if="authenticated" @click="signOut">Sign Out</button>
  
</nav>
</template>

<script>
export default {
  name: "Nav",
  data: () => ({
    authenticated: false,
    name: "",
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