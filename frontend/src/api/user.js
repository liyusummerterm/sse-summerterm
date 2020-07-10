import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/user/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/api/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/api/user/logout',
    method: 'post'
  })
}

export function getUserList() {
  return request({
    url: '/api/user/list',
    method: 'get'
  })
}

export function updateAvatar(data) {
  return request({
    url: '/api/avatar',
    method: 'put',
    data
  })
}
