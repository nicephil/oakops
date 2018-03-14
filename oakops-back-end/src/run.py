from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
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
    return resources.RevokedTokenModel.is_jti_blacklisted(jti)

api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogout, '/logout')
api.add_resource(resources.SecretResource, '/my')
api.add_resource(resources.TokenRefresh, '/refreshtoken')

from organizaiton import OrganizationList

ROOT_URL_v1 = "/ops/v1/"
api.add_resource(OrganizationList, ROOT_URL_v1 + "organizations")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)