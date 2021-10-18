<template>
<v-app class="cyan lighten-5">
  <v-card class="cyan lighten-5 text-center">
    <h3>Account</h3>
    <h4>User Name: {{ user.name }}</h4>
    <h4>Email: {{ user.email }}</h4>
    <v-card>
    <PostItem :items="items"  @addItem="addItem"/>
    </v-card>
  </v-card>
    <h3 class="profile-title">Products</h3>
    <v-card class="cyan lighten-5" v-for="item in user.items" :key="item.id">
    <ItemCard :item="item" :owner="user.name" />
  </v-card>
  </v-app>
</template>

<script>
import ItemCard from "../components/ItemCard.vue";
import PostItem from "../components/PostItem.vue";
import { GetUser } from "../services/UserServices";

export default {
  name: "Profile",
  components: {
    ItemCard,
    PostItem
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