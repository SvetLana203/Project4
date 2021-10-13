import Client from './api'

export const GetItems = async () => {
  const res = await Client.get('/items')
  return res.data
}

export const PostNewItem = async data => {
  const res = await Client.post('/items', data)
  return res
}

export const UploadImage = async file => {
  const res = await Client.post('/items/image', file)
  return res
}

export const DeleteItem = async item_id => {
  const res = await Client.delete(`/items/${item_id}`)
  return res
}
