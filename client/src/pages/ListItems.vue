<template>
  <div>
    <div class="post-item">
    <PostItem :items="items"  />
  </div>
  <div class="item-container">
  <div >
    <ItemCard v-for="item in items" :key="item.id" :item="item" />
    
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
  mounted: function () {
    this.getItems();
  },
  methods: {
    async getItems() {
      const res = await GetItems();
      this.items = res.reverse();
    },
  
  },
}
</script>

<style scoped>

</style>