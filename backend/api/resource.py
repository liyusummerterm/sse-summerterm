from flask import current_app, g, jsonify, request
from backend.extension import api_ext
from flask_restful import Resource, reqparse
from backend.algorithm import get_weather
from .schema import *
from . import auth
from . import api_bp


class AuthApi(Resource):
    def get(self):
        pass

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')

        if not auth.login_auth(username, password):
            return {'message': 'Username or password is wrong!'}, 400

        token, expiration = auth.generate_token(g.current_user)
        response = jsonify({
            'token': token,
            'token_type': 'Bearer',
            'expire_in': expiration
        })
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response


class UserApi(Resource):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        auth.register(username, password)
        return {'message': 'Register successfully!'}


class WeatherApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('city', type=str, required=True, help='City name is required!')
        self.reqparser.add_argument('date', type=int, help='The start date is required and needs to be timestamp!')


    def get(self):
        city = request.values['city']
        date = request.values['date']
        weather = get_weather(city, date)
        return weather_schema(weather)


class DataApi(Resource):
    def get(self):
        pass


api_ext.add_resource(WeatherApi, '/weather')
api_ext.add_resource(AuthApi, '/auth/token')
api_ext.add_resource(UserApi, '/user')
api_ext.add_resource(DataApi, '/data')







