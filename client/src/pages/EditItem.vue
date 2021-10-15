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
    <button>Edit</button>
  </form> 
      <div>
    </div>
  </div>
</template>

<script>
//import { UpdateItem } from '../services/ItemServices'
export default {
  name: "EditItem",
  props:["item"],
  data: ()=> ({
    itemEdit: {}
    // name:"",
    // image:"",
    // description:"",
    // updatedItem:{}
  }),
  mounted(){
    this.$emit("getItems")
    },
  methods:{
    handleItemChange(e){
      this[e.target.name] = e.target.value
    },
      
        //this.$emit("getItems")
    // async updateItem(e) {
    //   e.preventDefault()
    //   const newUpdatedItem = {
    //     name: this.name,
    //     image: this.image,
    //     description: this.description
  }
  //   console.log(newUpdatedItem)
  //   const res = await UpdateItem(newUpdatedItem)
  //     if (res.status === 200) {
  //     this.$router.push(`/listings/${id}`)
  //     this.$emit("handleItemChange",itemDetails)
  // }
    //}}

  }

</script>

<style scoped>

</style>