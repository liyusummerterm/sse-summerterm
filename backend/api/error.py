from flask import current_app, g, request


def user_schema(user):
    return {
        'id': user.id,
        'username': user.username,
        'group': user.group
    }