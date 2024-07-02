from flask import Blueprint
from flask_restful import Api, Resource

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

class MatchResource(Resource):
    def get(self):
        return {'message': 'Hello World'}

api.add_resource(MatchResource, '/matches')
