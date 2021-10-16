<template>
  <div class="item-card">
      <img :src="item.image" alt=""/>
    <div class="content">
      <h3>{{item.name}}</h3>
      <h3>{{item.description}}</h3>
      <h3>posted by {{itemUser}}</h3>
    </div>
    <!-- <ItemDetails v-for="item in items" :key="item.id" :item="item" @click.native="selectItem(item.id)"/> -->
    <!-- <div v-for="item in items" :key="item.id" :item="item"></div> -->
    <button class="view-details" @click="selectItem(item.id)" >View Details</button>
    <button class="add">Add to cart</button>
    
  </div>
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