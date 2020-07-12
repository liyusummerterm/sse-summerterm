import request from '@/utils/request'

export function fetchWeather(query) {
  return request({
    url: '/api/weather',
    method: 'get',
    params: query
  })
}

export function fetchCityList() {
  return request({
    url: '/api/citylist',
    method: 'get',
    params: ''
  })
}
