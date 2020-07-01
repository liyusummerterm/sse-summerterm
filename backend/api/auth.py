from flask import current_app, g, request
from backend.extension import http_auth, db, api
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from backend.models import User


def generate_token(user):
    expiration = 3600
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    token = s.dumps({'id': user.id}).decode('ascii')
    return token, expiration


def validate_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except (BadSignature, SignatureExpired):
        # TODO should return notice
        return False
    user = User.query.get(data['id'])
    if user is None:
        return False
    return user


@http_auth.verify_password
def login_auth(username_or_token, password):
    user = validate_token(username_or_token)
    if not user:
        user = User.query.filter_by(username_or_token).first()
        if not user or not user.validate_password(password):
            return False
    g.current_user = user
    return True

# TODO token should be returned if login with username

def register(username, password):
    pass


