import Client from './api'

// export const SignIn = async (username, password) => {
//   const res = await Client.post('/users/login', {
//     username,
//     password
//   })
//   return res.data
// }

export const CreateUser = async data => {
  const res = await Client.post('/users', data)
  return res
}
// export const RegisterUser = async (name, email) => {
//   const res = await Client.post('/users/register', { name, email })
//   return res.data
// }

// export const FindUsername = async username => {
//   const res = await Client.get(`/users/search?username=${username}`)
//   return res.data
// }

// export const RemoveUser = async userId => {
//   const res = await Client.delete(`/users/${userId}`)
//   return res.data
// }
