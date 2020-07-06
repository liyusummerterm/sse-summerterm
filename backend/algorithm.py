from .models import Weather


def get_weather(city, date):
    weather_obj = Weather(city, date, 10, 20)
    # weather_list = []
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
    weather_obj.seven_day_list.append({})
