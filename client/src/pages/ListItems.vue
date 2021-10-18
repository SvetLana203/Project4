<template>
  <div>
    <v-card>
    <PostItem :items="items"  @addItem="addItem"/>
    </v-card>
    <v-card class="d-flex justify-center flex-wrap mb-6 cyan lighten-5"
    flat
    tile>
    <v-card v-for="item in items" :key="item.id" class="pa-2"
    outlined
    tile>
    <ItemCard :item="item" :owner="item.user.name"/>
    </v-card>
    </v-card>
  </div>
</template>

<script>
import PostItem from "../components/PostItem.vue"
import ItemCard from "../components/ItemCard.vue"
import {GetItems} from "../services/ItemServices"
export default {
  name: "ListItems",
  components: {
    PostItem,
    ItemCard
  },
  data: () => ({
    items:[],
    selectedItem: null
  }),
  mounted() {
    this.$emit("checkRegistration")
    this.getItems();
  },
  methods: {
    async getItems() {
      const res = await GetItems();
      this.items = res.reverse();
    },
  addItem(item) {
    this.items.unshift(item)
  }
  },
}
</script>

<style scoped>

</style>