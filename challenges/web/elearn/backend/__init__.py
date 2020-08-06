import os
from hashlib import sha256

from flask import Flask
from werkzeug.security import safe_str_cmp

from flask_cors import CORS
from flask_jwt import JWT, current_identity, jwt_required


def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('FLASK_SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite3')
    app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'WHITEHACKS')

    from .model import db, ma
    db.init_app(app)
    ma.init_app(app)

    from .api import api
    api.init_app(app)

    from .model import User
    def authenticate(username, password):
        user = User.query.filter(User.username.ilike(username)).first()
        if user and safe_str_cmp(user.password.encode('utf-8'), sha256(password.encode('utf-8')).hexdigest().encode('utf-8')):
            return user

    def identity(payload):
        user_id = payload['identity']
        return User.query.filter(User.id == user_id).first()

    def jwt_decode_handler(token):
        from flask import current_app
        secret = current_app.config['JWT_SECRET_KEY']
        algorithm = current_app.config['JWT_ALGORITHM']
        leeway = current_app.config['JWT_LEEWAY']

        verify_claims = []  # current_app.config['JWT_VERIFY_CLAIMS']
        required_claims = []  # current_app.config['JWT_REQUIRED_CLAIMS']
        options = {'verify_' + claim: True for claim in verify_claims}
        options.update({'require_' + claim: True for claim in required_claims})

        import base64, json, jwt
        header = token.split('.')[0]
        header = header + '=' * (4 - len(header) % 4)
        verify = json.loads(base64.b64decode(header).decode()).get('alg', 'None').lower() != 'none'
        return jwt.decode(token, secret, options=options, algorithms=[algorithm], leeway=leeway, verify=verify)

    @app.route('/identity')
    @jwt_required()
    def user():
        return {'id': current_identity.id,
                'name': current_identity.name,
                'username': current_identity.username}

    jwt = JWT(app, authenticate, identity)
    jwt.jwt_decode_handler(jwt_decode_handler)

    cors = CORS(app, resources={r"/api/*": {'origins': '*'},
                                r"/auth": {'origins': '*'},
                                r"/identity": {'origins': '*'}})

    return app
