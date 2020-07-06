from flask import jsonify


def weather_schema(weather_object):
    weather_list = []
    # for i, j in zip(weather_object.list, range(len(weather_object.list))):
    #     weather_list.append({})
    #     weather_list[j]['dt'] = i['dt']
    #     weather_list[j]['temp'] = {}
    #     weather_list[j]['temp']['min'] = i['temp']['min']
    #     weather_list[j]['temp']['max'] = i['temp']['max']
    #     weather_list[j].append({})
    #     weather_list[j]['weather'] = []
    #     weather_list[j]['weather'][0] = {
    #         'main': i['weather'][0]['main']
    #     }
    #     weather_list[j]['speed'] = i['speed']
    #     weather_list[j]['deg'] = i['deg']
    #     weather_list[j]['clouds'] = i['clouds']
    #     weather_list[j]['rain'] = i['rain']
    #     weather_list[j]['pressure'] = i['pressure']
    #     weather_list[j]['humidity'] = i['humidity']

    # return jsonify({
    #     'city': {
    #         'name': weather_object.city
    #     },
    #     'list': weather_list
    # })
    return {
        "city": {
            "id": 1816670,
            "name": "Beijing",
            "coord": {
                "lon": 116.3972,
                "lat": 39.9075
            },
            "country": "CN",
            "population": 1000000,
            "timezone": 28800
        },
        "cod": "200",
        "message": 4.076458,
        "cnt": 7,
        "list": [
            {
                "dt": 1593835200,
                "sunrise": 1593809460,
                "sunset": 1593863178,
                "temp": {
                    "day": 28.37,
                    "min": 27.31,
                    "max": 28.37,
                    "night": 27.31,
                    "eve": 28.37,
                    "morn": 28.37
                },
                "feels_like": {
                    "day": 30.93,
                    "night": 28.72,
                    "eve": 30.93,
                    "morn": 30.93
                },
                "pressure": 995,
                "humidity": 68,
                "weather": [
                    {
                        "id": 500,
                        "main": "Rain",
                        "description": "light rain",
                        "icon": "10d"
                    }
                ],
                "speed": 2.97,
                "deg": 248,
                "clouds": 98,
                "rain": 0.99
            },
            {
                "dt": 1593921600,
                "sunrise": 1593895894,
                "sunset": 1593949564,
                "temp": {
                    "day": 29.66,
                    "min": 24.46,
                    "max": 32.76,
                    "night": 25.03,
                    "eve": 32.25,
                    "morn": 25.42
                },
                "feels_like": {
                    "day": 30.74,
                    "night": 26.81,
                    "eve": 30.61,
                    "morn": 26.05
                },
                "pressure": 999,
                "humidity": 43,
                "weather": [
                    {
                        "id": 500,
                        "main": "Rain",
                        "description": "light rain",
                        "icon": "10d"
                    }
                ],
                "speed": 1.15,
                "deg": 79,
                "clouds": 95,
                "rain": 1.38
            },
            {
                "dt": 1594008000,
                "sunrise": 1593982328,
                "sunset": 1594035949,
                "temp": {
                    "day": 33.59,
                    "min": 23.39,
                    "max": 37.46,
                    "night": 30.63,
                    "eve": 37.46,
                    "morn": 23.39
                },
                "feels_like": {
                    "day": 34.78,
                    "night": 30.77,
                    "eve": 36.44,
                    "morn": 25.65
                },
                "pressure": 999,
                "humidity": 33,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "sky is clear",
                        "icon": "01d"
                    }
                ],
                "speed": 0.64,
                "deg": 98,
                "clouds": 0
            },
            {
                "dt": 1594094400,
                "sunrise": 1594068765,
                "sunset": 1594122331,
                "temp": {
                    "day": 33.33,
                    "min": 25.1,
                    "max": 37.62,
                    "night": 25.9,
                    "eve": 37.62,
                    "morn": 25.1
                },
                "feels_like": {
                    "day": 34.51,
                    "night": 27.52,
                    "eve": 37.25,
                    "morn": 27.15
                },
                "pressure": 1004,
                "humidity": 40,
                "weather": [
                    {
                        "id": 501,
                        "main": "Rain",
                        "description": "moderate rain",
                        "icon": "10d"
                    }
                ],
                "speed": 2.23,
                "deg": 96,
                "clouds": 0,
                "rain": 7.82
            },
            {
                "dt": 1594180800,
                "sunrise": 1594155202,
                "sunset": 1594208712,
                "temp": {
                    "day": 32.07,
                    "min": 24.89,
                    "max": 34.45,
                    "night": 26.77,
                    "eve": 34.45,
                    "morn": 24.89
                },
                "feels_like": {
                    "day": 33.18,
                    "night": 26.42,
                    "eve": 33.9,
                    "morn": 26.88
                },
                "pressure": 1006,
                "humidity": 41,
                "weather": [
                    {
                        "id": 500,
                        "main": "Rain",
                        "description": "light rain",
                        "icon": "10d"
                    }
                ],
                "speed": 1.89,
                "deg": 141,
                "clouds": 4,
                "rain": 2.79
            },
            {
                "dt": 1594267200,
                "sunrise": 1594241641,
                "sunset": 1594295091,
                "temp": {
                    "day": 33.06,
                    "min": 24.64,
                    "max": 35.89,
                    "night": 30.6,
                    "eve": 35.6,
                    "morn": 24.64
                },
                "feels_like": {
                    "day": 33.34,
                    "night": 32.35,
                    "eve": 34.49,
                    "morn": 24.09
                },
                "pressure": 1001,
                "humidity": 34,
                "weather": [
                    {
                        "id": 500,
                        "main": "Rain",
                        "description": "light rain",
                        "icon": "10d"
                    }
                ],
                "speed": 1.94,
                "deg": 154,
                "clouds": 0,
                "rain": 0.87
            },
            {
                "dt": 1594353600,
                "sunrise": 1594328080,
                "sunset": 1594381468,
                "temp": {
                    "day": 26.45,
                    "min": 24.2,
                    "max": 30.12,
                    "night": 24.53,
                    "eve": 30.12,
                    "morn": 24.2
                },
                "feels_like": {
                    "day": 27.8,
                    "night": 25.49,
                    "eve": 32.78,
                    "morn": 25.1
                },
                "pressure": 1003,
                "humidity": 63,
                "weather": [
                    {
                        "id": 502,
                        "main": "Rain",
                        "description": "heavy intensity rain",
                        "icon": "10d"
                    }
                ],
                "speed": 2.58,
                "deg": 74,
                "clouds": 100,
                "rain": 15.32
            }
        ]
    }
