<template>
  <div class="edit-item">
  <form  class="edit-item">
      <!-- <input
      type="file"
      placeholder="product image"
      accept="image/*"
      @input="handleItemChange"
      /> -->
      <div>
    <img :src="itemEdit.image" alt=""/>
    <div class="input_product">
    <textarea v-model="itemEdit.name" name="name"  placeholder="product" @input="handleItemChange"/>
    </div>
    <textarea v-model="itemEdit.description" name="description"  placeholder="description" @input="handleItemChange"/>
    </div>
    <button @click="updateItem">Edit</button>
  </form> 
      <div>
    </div>
  </div>
</template>

<script>
import { UpdateItem, GetItemById } from '../services/ItemServices'
export default {
  name: "EditItem",
  // props:["item"],
  data: ()=> ({
    itemEdit: {},
    name:"",
    image:"",
    description:"",
    user_id:""
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
    handleItemChange(e){
    this[e.target.name] = e.target.value
    },
    
    async updateItem(e) {
    e.preventDefault()
    const newUpdatedItem = {
      name: this.name,
      image: this.image,
      description: this.description,
      // user_id: this.user_id
      
    }
    console.log(newUpdatedItem)
    const res = await UpdateItem(this.$route.params.item_id,newUpdatedItem)
    console.log("here",res)
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