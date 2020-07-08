from flask import current_app, g, request
from backend.extension import http_auth, db, api_ext
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
        print(token)
        return False
    user = User.query.get(data['id'])
    if user is None:
        return False
    return user


@http_auth.verify_password
def login_auth(username_or_token, password=''):

    user = validate_token(username_or_token)
    print(user)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.validate_password(password):
            return False
    g.current_user = user
    return True

# TODO token should be returned if login with username


def register(username, password, email=None, role=2):
    user = User(username=username)
    user.set_password(password)
    user.email = email
    user.group = role
    db.session.add(user)
    db.session.commit()





