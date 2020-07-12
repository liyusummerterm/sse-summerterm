from backend import create_app
from backend.extension import db
from backend.models import User, Role

app = create_app()
with app.app_context():
    db.create_all()

    user = User(username='admin')
    user.set_password('111111')
    user.role = 'admin'
    db.session.add(user)

    role = Role(role_name='admin')
    role.role_permission = '[{"name":"role","children":[{"name":"role.browse"},{"name":"role.delete"},{"name":"role.update"}]}]'
    db.session.add(role)

    db.session.commit()
