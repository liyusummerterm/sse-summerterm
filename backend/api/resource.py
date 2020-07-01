from flask import current_app, g, jsonify, request
from backend.extension import api_ext
from flask_restful import Resource, reqparse
from backend.algorithm import get_weather
from . import auth
from . import api_bp


class AuthApi(Resource):
    def get(self):
        pass

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')

        if not auth.login_auth(username, password):
            return False
            # TODO return error msg

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


class WeatherApi(Resource):
    def get(self):
        if request.json is None:
            return 400
        city = request.json['records']
        date = request.json['date']
        weather = get_weather(city, date)
        return jsonify({
            'city': weather.city,
            'date': weather.date,
            'maximum': weather.max,
            'minimum': weather.min
        })


api_ext.add_resource(WeatherApi, '/weather')
api_ext.add_resource(AuthApi, '/auth/token')
api_ext.add_resource(UserApi, '/user')






