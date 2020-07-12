import ast
import json
import requests

from backend.models import User, Role, router_info


def weather_schema(city, date):
    url = 'http://127.0.0.1:5001/weather'
    header = {'Content-Type': 'application/json'}
    datas = {"city": city, "date": int(date)}
    r = requests.get(url, headers=header, data=json.dumps(datas))
    return r.json()


def user_list_schema():
    users = User.query.all()
    response = {
        'code': 20000,
        'data': {
            'users': []
        }
    }
    for i in users:
        id = i.id
        username = i.username
        email = i.email
        role = i.role
        response['data']['users'].append({
            'id': id,
            'username': username,
            'email': email,
            'role': role
        })

    return response


def user_info_schema(user):
    # TODO need to modify
    role = Role.query.filter_by(role_name=user.role).one()
    print(role.role_permission)
    return {
        'code': 20000,
        'data': {
            'roles': user.role,
            'introduction': '',
            'avatar': user.avatar,
            'name': user.username,
            'auth': ast.literal_eval(role.role_permission)
        }

    }


def role_list_schema():
    data = []
    roles = Role.query.all()
    for i in roles:
        data.append({
            'key': i.id,
            'name': i.role_name,
            'description': i.role_description,
            'auth': ast.literal_eval(i.role_permission)
        })

    return {
        'code': 20000,
        'data': data
    }
    # return {
    #     'code': 20000,
    #     'data': [{
    #         'key': 'admin',
    #         'name': 'admin',
    #         'description': 'admin',
    #         'auth': [{
    #             "name": "role",
    #             "children": [
    #                 {
    #                     "name": "role.browse",
    #                 },
    #                 {
    #                     "name": "role.delete",
    #                 },
    #                 {
    #                     "name": "role.update"
    #                 }
    #             ]
    #         }]
    #     }]
    # }


def route_info_schema():
    return {
        'code': 20000,
        'data': router_info
    }
