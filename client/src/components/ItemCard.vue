<template>
  <v-card class="mx-auto" max-width="400">
      <v-img class="white--text align-end" height="200px" :src="item.image" alt=""/>
    <v-card-text class="text--primary">
      <h3>{{item.name}}</h3>
      <h3>{{item.description}}</h3>
      <h3>owner {{itemUser}}</h3>
    </v-card-text>
    <!-- <ItemDetails v-for="item in items" :key="item.id" :item="item" @click.native="selectItem(item.id)"/> -->
    <!-- <div v-for="item in items" :key="item.id" :item="item"></div> -->
    <v-btn color="orange" text @click="selectItem(item.id)" >View Details</v-btn>
    <v-btn color="orange" text>Add to cart</v-btn>
    
  </v-card>
</template>

<script>
// import ItemDetails from "./ItemDetails.vue"
export default {
  name: "ItemCard",
  // components: {ItemDetails},
  props:["item", "owner"],
  data: () => ({
    itemDetails: {},
    itemUser: ""
  }),
  mounted(){
    this.itemDetails = { ...this.item }
    this.itemUser = this.owner
  },
  methods: {
    // async viewDetails(id){
    //   this.$router.push(`/listings/${id}`)
    //   const res = await FindItemById(this.item.id)
    //   console.log(res)
    // }
    // selectItem(id){
      
    //   this.$router.push(`${this.$route.params.item_id}`)
    //    console.log("itemcard ",id)
    // },
      selectItem(id){
      console.log(id)
      this.$router.push(`listings/${id}`)
    },
    
  }
}
</script>

<style scoped>

</style>