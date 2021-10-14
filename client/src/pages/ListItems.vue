<template>
  <div>
    <div class="post-item">
    <PostItem :items="items"  />
  </div>
  <div class="item-container">
  <div v-for="item in items" :key="item.id">
    <ItemCard :item="item" @click="selectItem"/>
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
    selectItem(item){
      this.selectedItem = item
      // this.$route.push(`/listings/${id}`)
    
    }
  },
}
</script>

<style scoped>

</style>