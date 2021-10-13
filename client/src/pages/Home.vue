<template>
<div class="home">
  <div class="post-item">
    <PostItem :items="items" @addItem="addItem" />
  </div>
<div class="item-container">
  <div v-for="item in items" :key="item.id">
    <ItemCard :item="item" />
  </div>
</div>
</div>
</template>

<script>
import {GetItems} from "../services/ItemServices"
import PostItem from "../components/PostItem.vue"
import ItemCard from "../components/ItemCard.vue"
export default {
  name: "Home",
  components: {
    ItemCard,
    PostItem
  },
  data: () => ({
    items: []
  }),
  mounted: function () {
    this.$emit("checkRegistration");
    this.getItems();
  },
  methods: {
    async getItems() {
      const res = await GetItems();
      this.items = res.reverse();
    },
    addItem(item) {
      this.items.unshift(item);
    },
  },
}
</script>

<style scoped>

</style>