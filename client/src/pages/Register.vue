<template>
  <div>
    <h1>Register</h1>
    <form class="register-form" @submit="registerUser">
      <input v-model="name" type="text" placeholder="name">
      <input v-model="email" type="email" placeholder="email"/>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import {CreateUser} from "../services/UserServices"
export default {
  name: "Register",
  props:[""],
  data: () => ({
    name: "",
    email: ""
  }),
  methods: {
    async registerUser(e){
      if (this.name && this.email)
      {e.preventDefault()
        const payload = {
          name: this.name,
          email: this.email
        }
        const res = await CreateUser(payload)
        if(res.status === 201) {
          this.storeUserData(res.data)
        }
      }
    },
    storeUserData(data) {
      localStorage.setItem("name", data.name);
      localStorage.setItem("email", data.email);
      this.$router.push("/");
  }
  }
}
</script>

<style scoped>

</style>