from flask_restful import Resource


class OrganizationList(Resource):
    def get(self):
        return {"list":"list"}