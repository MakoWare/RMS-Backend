from flask import Flask
from flask import jsonify
from bson.json_util import dumps
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)


#from app.DataBase.database import init_db
#posts = init_db()

from app.routes import *

# @app.route('/')
# def home_page():
#     post = posts.find_one()
#     return dumps(post)



# from serveryourapplication.database import db_session

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()



