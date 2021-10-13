<template>
  <div class="new-item">
    <h2>Post your product</h2>
    <img :src="image"/>
    <div class="input_product">
    <input v-model="name" name="name" placeholder="product" @input="handleFormChange">
    </div>
    <textarea v-model="description" name="description" placeholder="description" @input="handleFormChange"/>
    <button class="submit" @click="createItem">Submit</button>
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
    async createItem(e){
      e.preventDefault()
      const res = {
        name: this.name,
        image: this.image,
        description: this.description,
        user_id: this.user_id
      }
      await PostNewItem(res)
      // const res = await PostNewItem({
      //   name: this.name,
      //   image: this.image,
      //   description: this.description
      // })
      // res.
    },
    handleFormChange(e) {
      this[e.target.name] = e.target.value
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