<template>
  <div class="item-card">
      <img :src="item.image" alt=""/>
    <div class="content">
      <h3>{{item.name}}</h3>
      <h3>{{item.description}}</h3>
    </div>
    <button class="delete" @click="deleteItem">Delete</button>
    <button class="edit" @click="updateItem">Edit</button>
    <button class="add">Add to cart</button>
    
  </div>
</template>

<script>

import { DeleteItem } from '../services/ItemServices';
export default {
  name: "ItemCard",
  components: {},
  props:["item"],
  data: () => ({
    itemDetails: {}
  }),
  mounted(){
    this.itemDetails = { ...this.item };
  },
  methods: {
    async deleteItem(){
      const res = await DeleteItem(this.itemDetails.id);
      console.log("res :>> ", res)
    },
  }
}
</script>

<style scoped>

</style>