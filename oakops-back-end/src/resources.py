from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be null', required=True)
parser.add_argument('password', help='This field cannot be null', required=True)

blacklist = set()

class RevokedTokenModel():        

    @classmethod
    def is_jti_blacklisted(self, jti):
        return jti in blacklist

    @classmethod
    def addToBlacklist(self, jti):
        blacklist.add(jti)

    @classmethod
    def getBlackList(self):
        return blacklist


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        try:
            if data['username'] != 'hui.he@oakridge.io' or data['password'] != 'oakridge':
                return {
                    "error_code": 100100,
                    "message": "Bad username or password"
                }

            return {
                'error_code': 0,
                'message' : 'Login success',             
                'access_token': create_access_token(identity = data['username']),
                'refresh_token': create_refresh_token(identity = data['username'])
            }

            # return jsonify(ret), 200

        except:
            return {
                 'message' : 'Something went wrong'
            }, 500

class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        RevokedTokenModel.addToBlacklist(jti)
        return {"msg": "Successfully logged out"}

class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        ret = {
            'access_token': create_access_token(identity=current_user)
        }
        return jsonify(ret), 200            



# Example: The protected resuource need token
class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }           