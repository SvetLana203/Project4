<template>
  <v-card>
    <v-card width="400" class="mx-auto mt-5">
      <v-card-title>
    <h2>Post your product</h2>
      </v-card-title>
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
    <v-card-text>
    <v-form  >
      <v-text-field  v-model="image" label="image" prepend-icon="mdi-image"/>
      <v-text-field v-model="name" label="product" prepend-icon="mdi-title"/>
      <v-text-field v-model="description" label="description" prepend-icon="mdi-edit"/>
    <v-card-actions>
    <v-btn color="success" @click="createItem">Submit</v-btn>
    </v-card-actions>
    </v-form>
    </v-card-text>
    </v-card>
  </v-card>
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
    // handleFormChange(e) {
      // /this[e.target.name] = e.target.value
    // },
    
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
.input-product {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  
}
/* .btn-postitem{
  background-color: purple;
  color:blue;
} */

</style>