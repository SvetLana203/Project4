<template>
  <v-card class="mx-auto" max-width="400">
      <v-img :src="itemDetails.image" alt=""/> 
    <v-card-text>
      <h3>{{itemDetails.name}}</h3>
      <h3>{{itemDetails.description}}</h3>
    </v-card-text>
    <v-btn color="blue" text @click="deleteItem">Delete</v-btn>
    <router-link  :to="`/edit/${itemDetails.id}`">EDIT</router-link>
    <v-btn color="blue" text>Add to cart</v-btn>
  </v-card>
</template>

<script>
import {DeleteItem,GetItemById} from "../services/ItemServices"
export default {
  name: "ItemCard",
  components: {},
  // props:["item"],
  data: () => ({
    itemDetails: {},
    
  }),
  mounted(){
    console.log(this.$route)
    this.itemDetails = { ...this.item };
    this.viewDetails(this.$route.params.item_id)
    
  },
  methods: {
    async viewDetails(id){
      const res = await GetItemById(id)
      //console.log ("params",id)
      console.log("viewing",res)
      this.itemDetails = res
    },
    async deleteItem(){
      const res = await DeleteItem(this.$route.params.item_id);
      console.log("deleted", res)
      this.itemDetails = ""
      this.$router.push("/listings")
    },
    // handleItemChange(e){
    //   this[e.target.name] = e.target.value
    // },
    // async updateItem(){
    //   // e.preventDefault()
    //   const newUpdatedItem = {
    //     name: this.name,
    //     image: this.image,
    //     description: this.description
    //   }
    //   const res = await UpdateItem(newUpdatedItem)
    //   console.log("updated", res)
    //   this.$emit("handleItemChange")
    // }
  }
}
</script>

<style scoped>

</style>