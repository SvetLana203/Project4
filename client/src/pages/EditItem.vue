<template>
  <v-card class="mx-auto" max-width="400">
    <v-card-text>
  <v-form  class="edit-item">
      <!-- <input
      type="file"
      placeholder="product image"
      accept="image/*"
      @input="handleItemChange"
      /> -->
      
    <v-img class="white--text align-end" height="200px" :src="itemEdit.image" alt=""/>
    <v-text-field v-model="itemEdit.image"  label="image" prepend-icon="mdi-image"/>
    <v-text-field v-model="itemEdit.name"  label="product" prepend-icon="mdi-edit"/>
    <v-text-field v-model="itemEdit.description"  label="description" prepend-icon="mdi-edit"/>
    <v-card-actions>
    <v-btn color="orange" text @click="updateItem">Edit</v-btn>
    </v-card-actions>
  </v-form> 
  </v-card-text>
      
    
  </v-card>
</template>

<script>
import { UpdateItem, GetItemById } from '../services/ItemServices'
export default {
  name: "EditItem",
  // props:["item"],
  data: ()=> ({
    itemEdit: {name:"",image:"",
    description:""}
    // user_id:""
    //updatedItem:{}
  }),
  mounted() {
  this.getItems()
  //this.newUpdatedItem()
    },
  methods:{
  async getItems(){
      const res = await GetItemById(this.$route.params.item_id)
      console.log("let's edit",res)
      this.itemEdit = res
  },
    // handleItemChange(e){
    // this[e.target.name] = e.target.value
    // },
    
    async updateItem(e) {
    e.preventDefault()
    const newUpdatedItem = {
      image: this.itemEdit.image,
      name: this.itemEdit.name,
      description: this.itemEdit.description,
      // user_id: this.user_id
      
    }
    console.log(newUpdatedItem)
    const res = await UpdateItem(this.$route.params.item_id,newUpdatedItem)
    console.log("updated",res)
    this.newUpdatedItem =  res
    this.$router.push("/listings")
    }


  // async updateItem(e){
  //   e.preventDefault()
  //   const res = await UpdateItem(this.$route.params.item_id, this.itemEdit)
  //   console.log("updated", res)
  //   this.newUpdatedItem = res
  //   this.$router.push("/listings")
  // }
  }
}
</script>

<style scoped>

</style>