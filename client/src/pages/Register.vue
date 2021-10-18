<template>
  <v-app class="cyan lighten-5">
    <v-card  width="400" class="mx-auto mt-5">
      <v-card-title>
      <h1>Welcome</h1>
      </v-card-title>
    <v-card-text>
    <v-form >
      <v-text-field  label="name" v-model="name" prepend-icon="mdi-account-circle"/>
      <v-text-field type="email" label="email" v-model="email" prepend-icon="mdi-email"/>
      <v-card-actions>
    <v-btn color="success" @click="createUser">Submit</v-btn>
    </v-card-actions>
    </v-form>
    </v-card-text>
    </v-card>
  </v-app>
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
          email: this.email,
          user_id: this.user_id
        }
        const res = await CreateUser(payload)
        if(res.status === 201) 
        {
          this.storeUserData(res.data)
          console.log(res.data)
        }
      }
    },
    
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