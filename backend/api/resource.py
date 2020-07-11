from flask import current_app, g, jsonify, request
from backend.extension import api_ext, db
from flask_restful import Resource, reqparse
from backend.algorithm import get_weather
from .schema import *
from . import auth
from . import api_bp
from backend.models import User, role_map
import werkzeug, requests
from io import BufferedReader, BytesIO
import os


class TokenApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('username', type=str, required=True)
        self.reqparser.add_argument('password', type=str, required=True)

    def get(self):
        pass

    def post(self):
        username = request.json['username']
        password = request.json['password']

        if not auth.login_auth(username, password):
            return {'code': 50008, 'message': 'Username or password is wrong!'}

        token, expiration = auth.generate_token(g.current_user)
        response = jsonify({
            'code': 20000,
            'data': {
                'token': token,
                'token_type': 'Bearer',
                'expire_in': expiration
            }
        })
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response


class AuthApi(Resource):
    def post(self):
        pass


class UserApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('username', type=str)
        self.reqparser.add_argument('password', type=str)
        self.reqparser.add_argument('role', type=str)
        self.reqparser.add_argument('email', type=str)

    def post(self):
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')
        auth.register(username, password, email)
        return {'code': 20000, 'message': 'Register successfully!'}

    def put(self, user_id):
        user = User.query.filter_by(id=user_id).one()
        user.email = request.json['email']
        if request.json.get('password') is not None:
            user.set_password(request.json['password'])
        try:
            user.role = request.json['role']
        except ValueError:
            return {'code': 50000}
        db.session.commit()
        return {'code': 20000}

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).one()
        db.session.delete(user)
        db.session.commit()
        return {'code': 20000}


class UserListApi(Resource):
    def get(self):
        return user_list_schema()


class UserInfoApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('token', type=str, required=True)

    def get(self):
        token = request.values['token']
        if not auth.login_auth(token):
            return {'code': 50008}, 400
        return user_info_schema(g.current_user)


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
        auth.register('admin', '111111')


class LogoutApi(Resource):
    def post(self):
        g.current_user = None
        return {
            'code': 20000,
            'data': 'success'
        }


class AvatarUploadApi(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('img', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        image_file = args['img']
        image_file = BytesIO(image_file.read())
        header = {'Authorization': '5Elz35ckLkjBKMurwW3FwiJ8wookBrds'}
        r = requests.post('https://sm.ms/api/v2/upload', files={'smfile': image_file})
        res = r.json()
        if not res or res.get('success') is not True:
            return {'code': 50000}, 400
        return res


class AvatarChangeApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('avatar', type=str, required=True)

    def put(self):
        token = request.headers.get('X-Token')
        user = auth.validate_token(token)
        if not auth.validate_token(token):
            return {'code': 50000, 'message': 'Token is invalid!'}, 400
        else:
            user.avatar = request.json.get('avatar')
            db.session.commit()


class RoleApi(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('key', type=str)
        self.reqparser.add_argument('name', type=str)
        self.reqparser.add_argument('description', type=str)
        self.reqparser.add_argument('auth', type=str)

    def get(self):
        return role_list_schema()

    def put(self, role_id):
        role = Role.query.filter_by(id=role_id).one()
        role.name = request.json['name']
        role.role_description = request.json['description']
        role.role_permission = json.dumps(request.json['auth'])
        db.session.commit()
        return {
            'code': 20000,
            'msg': 'Role updated successfully!'
        }

    def post(self):
        role = Role(role_name=request.json['name'],
                    role_description=request.json['description'])
        role.role_permission = json.dumps(request.json['auth'])
        db.session.add(role)
        db.session.commit()
        return {
            'code': 20000,
            'data': {
                'key': role.id,
                'name': role.role_name,
                'description': role.role_description
            }
        }

    def delete(self, role_id):
        role = Role.query.filter_by(id=role_id).one()
        db.session.delete(role)
        db.session.commit()
        return {
            'code': 20000,
            'msg': 'Delete successfully!'
        }


class RouteApi(Resource):
    def get(self):
        return route_info_schema()


api_ext.add_resource(WeatherApi, '/weather')
api_ext.add_resource(TokenApi, '/user/login')
api_ext.add_resource(UserApi, '/user', '/user/<int:user_id>', '/user/<string:username>')
api_ext.add_resource(DataApi, '/data')
api_ext.add_resource(UserInfoApi, '/user/info')
api_ext.add_resource(LogoutApi, '/user/logout')
api_ext.add_resource(UserListApi, '/user/list')
api_ext.add_resource(AvatarUploadApi, '/upload')
api_ext.add_resource(AvatarChangeApi, '/avatar')
api_ext.add_resource(RoleApi, '/roles', '/role/<int:role_id>', '/role')
api_ext.add_resource(RouteApi, '/routes')
