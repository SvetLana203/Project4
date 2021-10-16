import Client from './api'

export const GetUser = async id => {
  const res = await Client.get(`/users/${id}`)
  return res.data
}

export const CreateUser = async data => {
  const res = await Client.post('/users', data)
  return res
}
export const GetAllUsers = async () => {
  const res = await Client.get('/users')
  return res.data
}

export const VerifyUser = async data => {
  const res = await Client.post('/users/verify', data)
  return res
}
// export const FindUsername = async username => {
//   const res = await Client.get(`/users/search?username=${username}`)
//   return res.data
// }

// export const RemoveUser = async userId => {
//   const res = await Client.delete(`/users/${userId}`)
//   return res.data
// }
