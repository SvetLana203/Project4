<template>
  <div>
    <v-card>
    <div class="post-item">
    <PostItem :items="items"  @addItem="addItem"/>
    
  </div>
  </v-card>
  <div class="item-container">
  <div v-for="item in items" :key="item.id">
    <ItemCard :item="item" :owner="item.user.name"/>
    
  </div>
</div>
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