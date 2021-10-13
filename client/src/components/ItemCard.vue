<template>
  <div class="item-content">
    <div>
      <img :src="itemDetails.image"/>
      <h3>{{itemDetails.name}}</h3>
      <h3>{{itemDetails.description}}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: "ItemCard",
  // props: {
  //   name: String,
  //   image: String,
  //   description: String
  // },
  data: () => ({
    itemDetails: {}
  }),
  mounted(){
    this.postDetails = { ...this.post };
  }
}
</script>

<style scoped>

</style>