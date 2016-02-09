from app.DataBase.database import db
from pymongo import ReturnDocument
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import request
from flask.ext.restful import abort, Resource, fields, marshal_with
import datetime
import json

class UserResource(Resource):
    def get(self, id):
#        user = db.users.find_one({"_id": ObjectId(id)})
#        if not user:
#            abort(404, message="does not exist, or has been soft deleted".format(id))
#        return json.loads(dumps(user))
        return "hi der"

    def put(self, id):
        requestJSON = request.get_json()
        resourceId = {'_id': ObjectId(id)}
        updatedUser = db.users.find_one_and_update(resourceId, {"$set": requestJSON}, return_document=ReturnDocument.AFTER)
        return json.loads(dumps(updatedUser)), 201

    def delete(self, id):
        now = datetime.datetime.utcnow()
        softDelete = {"deletedAt": now}
        resourceId = {'_id': ObjectId(id)}
        updatedUser = db.users.find_one_and_update(resourceId, {"$set": softDelete}, return_document=ReturnDocument.AFTER)
        return json.loads(dumps(updatedUser)), 201

class UserListResource(Resource):
    def get(self):
        users = db.users.find_one()
        return json.loads(dumps(users)), 201

    def post(self):
        requestJSON = request.get_json()
        createdUserId = db.users.insert_one(requestJSON).inserted_id
        createdUser = db.users.find_one(createdUserId)
        print(requestJSON)
        print(createdUser)
        return json.loads(dumps(createdUser))

