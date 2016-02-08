from app.DataBase.database import db
from pymongo import ReturnDocument
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import request
from flask.ext.restful import abort, Resource, fields, marshal_with
import datetime
import json

class RouteResource(Resource):
    def get(self, id):
        resource = db.routes.find_one({"_id": ObjectId(id)})
        if not resource:
            abort(404, message="does not exist, or has been soft deleted".format(id))
        return json.loads(dumps(resource))

    def put(self, id):
        requestJSON = request.get_json()
        resourceId = {'_id': ObjectId(id)}
        updatedResource = db.routes.find_one_and_update(resourceId, {"$set": requestJSON}, return_document=ReturnDocument.AFTER)
        return json.loads(dumps(updatedResource)), 201

    def delete(self, id):
        now = datetime.datetime.utcnow()
        softDelete = {"deletedAt": now}
        resourceId = {'_id': ObjectId(id)}
        updatedResource = db.routes.find_one_and_update(resourceId, {"$set": softDelete}, return_document=ReturnDocument.AFTER)
        return json.loads(dumps(updatedResource)), 201

class RouteListResource(Resource):
    def get(self):
        resources = db.resources.find_one()
        return json.loads(dumps(resources)), 201

    def post(self):
        requestJSON = request.get_json()
        createdResourceId = db.routes.insert_one(requestJSON).inserted_id
        createdResource = db.routes.find_one(createdResourceId)
        return json.loads(dumps(createdResource))

