from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

from resources import authentication

app = Flask(__name__)
api = Api(app)
CORS(app)

import views, resources

jwt = JWTManager(app)
# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'jwt-secret-oakridge'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return authentication.RevokedTokenModel.is_jti_blacklisted(jti)

api.add_resource(authentication.UserLogin, '/login')
api.add_resource(authentication.UserLogout, '/logout')
api.add_resource(authentication.SecretResource, '/my')
api.add_resource(authentication.TokenRefresh, '/refreshtoken')