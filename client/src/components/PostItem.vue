<template>
  <div class="new-item">
    <h2>Post your product</h2>
    
      <!-- <p>Preview here:</p>
    <template v-if="previewImage" >
    <img :src="previewImage" alt=""/>
    </template>
    <input
      type="file"
      placeholder="item image"
      accept="image/*"
      @change="previewIm"
      />
      <button @click="uploadIm">Upload</button> -->
    <form @submit="createItem" >
    <div class="input_product">
    <input v-model="image" name="image" placeholder="image"/>
    <textarea v-model="name" name="name"  placeholder="product" @input="handleFormChange"/>
    </div>
    <textarea v-model="description" name="description"  placeholder="description" @input="handleFormChange"/>
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
    itemImage: null,
    previewImage: null
  }),

  
  methods: {
    // previewIm(e){ 
    //   // this.previewImage = e.target.files[0]}
    //   // this.input = e.target
    //   // if (this.input.files && this.input.files[0]) {
    //   //   const reader = new FileReader()
    //   //   reader.onload = (e) => {
    //   //     this.previewImage = e.target.result
    //   //   }
    //   //   reader.readAsDataURL(this.input.files[0])
    //   // }   
    //   const file = e.target.files
    //   if (file && file[0]){
    //     console.log("file :>>", file)
    //     this.itemImage = file[0]
    //     const reader = new FileReader()
    //     reader.onload = (e) => {
    //       this.previewImage = e.target.result
    //     }
    //     reader.readAsDataURL(file[0])
    //   }
    // },
    // async uploadIm(){
    //   const formData = new FormData()
    //   formData.append("file", this.previewImage)
    //   const res = await UploadImage(formData)
    //   console.log(res)
    //   this.image = this.itemImage.name
    // },  
    handleFormChange(e) {
      this[e.target.name] = e.target.value
    },
    
    async createItem(e){
      e.preventDefault()
      const res = {
        name: this.name,
        image: this.image,
        description: this.description,
        user_id: localStorage.getItem("user_id")
      }
      await PostNewItem(res)
      this.name = ""
      this.image = ""
      this.description = ""
    }, 
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