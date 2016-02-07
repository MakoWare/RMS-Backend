from app.DataBase.database import db
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask.ext.restful import reqparse, abort, Resource, fields, marshal_with
import json

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)

class UserResource(Resource):
    def get(self, id):
        user = db.users.find_one({"_id": ObjectId(id)})
        if not user:
            abort(404, message="User doesn't exist".format(id))

        return json.loads(dumps(user))

    def post(self, id):
        parsed_args = parser.parse_args()
        user = users.insert_one()
        print("Inserted User: ")
        print(user)
        return json.loads(dumps(user))

    def put(self, id):
        parsed_args = parser.parse_args()
        hub = db_session.query(Hub).filter(Hub.id == id).first()
        if not hub:
            abort(404, message="Hub doesn't exist".format(id))

        hub.name = parsed_args['name']
        db_session.add(hub)
        db_session.commit()
        return hub.as_dict(), 201


    def delete(self, id):
        hub = db_session.query(Hub).filter(Hub.id == id).first()
        if not hub:
            abort(404, message="Hub {} doesn't exist".format(id))
        db_session.delete(hub)
        db_session.commit()
        return {}, 204


# class HubListResource(Resource):
#     @marshal_with(hub_fields)
#     def get(self):
#         hubs = db_session.query(Hub).all()
#         return hubs, 201

#     def post(self):
#         parsed_args = parser.parse_args()
#         hub = Hub(name=parsed_args['name'])
#         db_session.add(hub)
#         db_session.commit()
#         return hub.as_dict(), 201
