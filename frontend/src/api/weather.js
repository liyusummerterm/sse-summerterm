import request from '@/utils/request'

export function fetchWeather(query) {
  return request({
    url: 'http://127.0.0.1:5000/api/weather?city=Beijing&date=1593835200',
    method: 'get',
    params: query
  })
}
