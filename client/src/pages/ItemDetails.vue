<template>
  <div class="item-card">
      <img :src="itemDetails.image" alt=""/> 
    <div class="content">
      <h3>{{itemDetails.name}}</h3>
      <h3>{{itemDetails.description}}</h3>
    </div>
    <button class="delete" @click="deleteItem">Delete</button>
    <button class="edit" >Edit</button>
    <button class="add">Add to cart</button>
    
  </div>
</template>

<script>
import {DeleteItem,GetItemById,} from "../services/ItemServices"
export default {
  name: "ItemCard",
  components: {},
  // props:["item"],
  data: () => ({
    itemDetails: {}
  }),
  mounted(){
    console.log(this.$route)
    this.itemDetails = { ...this.item };
    this.viewDetails(this.$route.params.item_id)
    
  },
  methods: {
    
    async viewDetails(id){
      const res = await GetItemById(id)
      console.log (">> params",id)
      console.log(res)
      this.itemDetails = res
    },
    async deleteItem(){
      const res = await DeleteItem(this.$route.params.item_id);
      console.log("res >> ", res)
      this.itemDetails = ""
    },
  }
}
</script>

<style scoped>

</style>