from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

from resources import authentication, organization

app = Flask(__name__)
api = Api(app)
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
CORS(app)

import resources

jwt = JWTManager(app)
# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'jwt-secret-oakridge'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return authentication.RevokedTokenModel.is_jti_blacklisted(jti)



baseurl = '/ops/v1/'
# Authentication
api.add_resource(authentication.UserLogin, baseurl + 'login')
api.add_resource(authentication.UserLogout, baseurl + 'logout')
api.add_resource(authentication.SecretResource, baseurl + 'my')
api.add_resource(authentication.TokenRefresh, baseurl + 'refreshtoken')
# Organization
api.add_resource(organization.OrganizationList, baseurl + 'organizations')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
