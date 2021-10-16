<template>
  <div>
    <h1>Welcome</h1>
    <form class="register-form" @submit.prevent="createUser">
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
  data: () => ({
    name: "",
    email: ""
  }),
  methods: {
    async createUser(){
      if (this.name && this.email){
        const payload = {
          name: this.name,
          email: this.email
        }
        const res = await CreateUser(payload)
        if(res.status === 201) 
        {
          this.storeUserData(res.data)
          console.log(res.data)
        }
      }
    },
    // async getUser() {
    //   if (this.verifyEmail) {
    //     const payload = {
    //       user_email: this.verifyEmail,
    //     };
    //     const res = await VerifyUser(payload);
    //     if (res.data.msg === "user not found") {
    //       this.found = false;
    //     } else {
    //       this.storeUserData(res.data);
    //     }
    //   }
    // },
    storeUserData(data) {
      localStorage.setItem("name", data.name);
      localStorage.setItem("email", data.email);
      localStorage.setItem("user_id", data.id);
      localStorage.setItem("authenticated", true);
      this.$router.push("/");
  }
  }
}
</script>

<style scoped>

</style>