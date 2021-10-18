<template>
<v-app class="cyan lighten-5">
  <v-card class="cyan lighten-5 text-center">
    <h3>Account</h3>
    <h4>User: {{ user.name }}</h4>
    <h4>Email: {{ user.email }}</h4>
    <v-card class="cyan lighten-5">
    <PostItem :items="items"  @addItem="addItem"/>
    </v-card>
  </v-card>
    <h3 class="profile-title text-center">Products</h3>
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
    items: [],
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
    addItem(item) {
    this.items.unshift(item)
  }
  },
};
</script>


<style scoped>

</style>