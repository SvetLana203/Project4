<template>
  <div class="new-item">
    <h2>Post your product</h2>
    <form @submit="createItem" >
    <input
      type="file"
      placeholder="product image"
      accept="image/*"
      @input="handleFormChange"
      />
    <img :src="image" alt=""/>
    <div class="input_product">
    <textarea v-model="name" name="name" placeholder="product" @input="handleFormChange"/>
    </div>
    <textarea v-model="description" name="description" placeholder="description" @input="handleFormChange"/>
    <button>Submit</button>
    </form>
  </div>
</template>

<script>
import {PostNewItem} from "../services/ItemServices";
export default {
  name: "PostItem",
  data: () => ({
    name: "",
    image: "",
    description: "",
  }),

  
  methods: {
    handleFormChange(e) {
      this[e.target.name] = e.target.value
      // this[e.target.description] = e.target.value
    },

    async createItem(e){
      e.preventDefault()
      this.name = ""
      this.image = ""
      this.description = ""
      const res = {
        name: this.name,
        image: this.image,
        description: this.description,
        user_id: 2
      }
      await PostNewItem(res)
      // const res = await PostNewItem({
      //   name: this.name,
      //   image: this.image,
      //   description: this.description
      // })
      // res.
    }
    
    
  }
}
</script>

<style scoped>
.new-post {
  display: flex;
  flex-direction: column;
  justify-content: space-between
}

</style>