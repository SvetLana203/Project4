<template>
  <div class="edit-item">
    <div>
  <form class="edit-item" @submit="handleUpdateSubmit">
      <input
      type="file"
      placeholder="product image"
      accept="image/*"
      @input="handleItemChange"
      />
    <img :src="image" alt=""/>
    <div class="input_product">
    <textarea v-model="name" name="name"  placeholder="product" @input="handleItemChange"/>
    </div>
    <textarea v-model="description" name="description"  placeholder="description" @input="handleItemChange"/>
    </form> 

    </div>
  </div>
</template>

<script>
import { UpdateItem } from '../services/ItemServices'
export default {
  name: "EditItem",
  props:["item"],
  data: ()=> ({
    name:"",
    image:"",
    description:"",
    updatedItem:{}
  }),
  mounted(){
    this.updatedItem = { ...this.item }
    },
  methods:{
    handleItemChange(e){
      this[e.target.name] = e.target.value
    },
    async updateItem(e) {
      e.preventDefault()
      const newUpdatedItem = {
        name: this.name,
        image: this.image,
        description: this.description
  }
    console.log(newUpdatedItem)
    const res = await UpdateItem(newUpdatedItem)
      if (res.status === 200) {
      this.$router.push(`/listings/${id}`)
  }
    }

  }
}
</script>

<style scoped>

</style>