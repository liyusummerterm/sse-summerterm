# from . import api_ext
from flask import g, request
from flask_restful import reqparse, Resource
from emd_lstm.test import get_predict
import datetime
from . import api_ext


class WeatherApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('city', type=str, required=True)
        self.reqparser.add_argument('date', type=int, required=True)

    def get(self):
        res = {}
        city = request.json.get('city')
        date = datetime.datetime.fromtimestamp(request.json.get('date'))
        predict_result = get_predict(city, date.strftime('%Y-%m-%d'))
        res['city'] = {
            'name': request.json.get('city')
        }

        day_list = []
        for i in range(0, 7):
            day_list.append({})
            day_list[i]['temp'] = {
                'min': int(predict_result['TMIN'][i]),
                'max': int(predict_result['TMAX'][i]),
                'avg': int(predict_result['TAVG'][i]),
                'prcp': round(predict_result['PRCP'][i], 1)
            }
            day_list[i]['dt'] = int(datetime.datetime.timestamp(date + datetime.timedelta(days=i+1)))

        res['list'] = day_list
        res['code'] = 20000
        res['message'] = 'Weather data fetched successfully!'
        return res


api_ext.add_resource(WeatherApi, '/weather')
