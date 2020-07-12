from flask import request, current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import json
from collections import namedtuple
from backend.extension import db

role_map = ['admin', 'moderator', 'user']


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(128))
    role = db.Column(db.String(128), nullable=False, default='user')
    avatar = db.Column(db.String(128), default='https://jandan.net/ofk.gif')
    description = db.Column(db.String(128), default='This guy is lazy, no details have been filled yet.')

    # 0 for admin, 1 for moderator, 2 for ordinary member

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, hashed_password):
        return check_password_hash(self.password_hash, hashed_password)


class Weather:
    def __init__(self, city, date, maximum, minimum):
        self.city = city
        self.date = date
        self.max = maximum
        self.min = minimum
        self.seven_day_list = []


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(128), index=True)
    role_description = db.Column(db.String(128))
    role_permission = db.Column(db.String(1024))


router_scheme = '''
[{
                "name": "role",
                "meta":
                    {
                        "title": "角色管理"
                    },
                "children": [
                    {
                        "name": "role.browse",
                        "meta":
                            {
                                "title": "查看角色"
                            }
                    },
                    {
                        "name": "role.add",
                        "meta":
                            {
                                "title": "添加角色"
                            }
                    },
                    {
                        "name": "role.delete",
                        "meta":
                            {
                                "title": "删除角色"
                            }
                    },
                    {
                        "name": "role.update",
                        "meta":
                            {
                                "title": "编辑角色"
                            }
                    }
                ]
            },
            {
                "name": "user",
                "meta":
                    {
                        "title": "用户管理"
                    },
                "children": [
                    {
                        "name": "user.browse",
                        "meta":
                            {
                                "title": "查看用户列表"
                            }
                    },
                    {
                        "name": "user.add",
                        "meta":
                            {
                                "title": "添加用户"
                            }
                    },
                    {
                        "name": "user.delete",
                        "meta":
                            {
                                "title": "删除用户"
                            }
                    },
                    {
                        "name": "user.update",
                        "meta":
                            {
                                "title": "更改用户"
                            }
                    }
                ]
            },
            {
                "name": "query",
                "meta":
                    {
                        "title": "天气查询"
                    },
                "children": [
                    {
                        "name": "query.browse",
                        "meta":
                            {
                                "title": "天气查询"
                            }
                    },
                    {
                        "name": "query.download",
                        "meta":
                            {
                                "title": "天气数据下载"
                            }
                    }
                ]
            }]
'''

router_info = json.loads(router_scheme)

city_list = ['Beijing', 'Changchun', 'Changsha', 'Chengdu', 'Chongqing', 'Fuzhou', 'Guangzhou', 'Guiyang', 'Haikou', 'Hangzhou', 'Harbin', 'Hefei', 'Hohhot', 'Kunming', 'Lahsa', 'Macau', 'Nanchang', 'Nanjing', 'Nanning', 'Shanghai', 'Shijiazhuang', 'Taiyuan', 'Tianjin', 'Wuhan', 'Wulumuqi', 'Wushaoling', 'Xian', 'Xining', 'Yinchuan', 'Zhengzhou']
