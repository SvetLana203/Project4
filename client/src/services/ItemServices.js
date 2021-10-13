import Client from './api'

export const GetItems = async () => {
  const res = await Client.get('/items')
  return res.data
}

export const PostNewItem = async data => {
  const res = await Client.post('/items', data)
  return res.data
}
