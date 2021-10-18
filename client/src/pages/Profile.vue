<template>
  <v-card class="cyan lighten-5">
      <h3>Profile</h3>
      <h4>User Name: {{ user.name }}</h4>
      <h4>Email: {{ user.email }}</h4>
      <h3 class="profile-title">Products</h3>
    <v-card v-for="item in user.items" :key="item.id">
        <ItemCard :item="item" :owner="user.name" />
    </v-card>
  </v-card>
</template>

<script>
import ItemCard from "../components/ItemCard.vue";
import { GetUser } from "../services/UserServices";

export default {
  name: "Profile",
  components: {
    ItemCard,
  },
  data: () => ({
    user: {},
  }),
  mounted: function () {
    this.$emit("checkRegistration");
    this.getUser();
  },
  methods: {
    async getUser() {
      const userId = localStorage.getItem("user_id");
      if (userId) {
        const res = await GetUser(userId);
        console.log(res);
        this.user = res;
      }
    },
  },
};
</script>


<style scoped>

</style>