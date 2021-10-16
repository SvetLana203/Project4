import Client from './api'

export const GetItems = async () => {
  const res = await Client.get('/items')
  return res.data
}
export const GetItemById = async id => {
  const res = await Client.get(`/items/${id}`)
  return res.data
}
export const PostNewItem = async data => {
  const res = await Client.post('/items', data)
  return res.data
}

export const UploadImage = async file => {
  const res = await Client.post('/items/image', file)
  return res
}

export const DeleteItem = async id => {
  const res = await Client.delete(`/items/${id}`)
  return res
}

export const UpdateItem = async (id, data) => {
  const res = await Client.put(`/items/${id}`, data)
  return res
}
