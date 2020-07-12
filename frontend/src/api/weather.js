import request from '@/utils/request'

export function fetchWeather(query) {
  return request({
    url: 'http://127.0.0.1:5000/api/weather',
    method: 'get',
    params: query
  })
}
