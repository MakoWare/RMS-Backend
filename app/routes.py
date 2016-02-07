from app.Resources.UserResource import *
from app import *

#api.add_resource(HubListResource, '/hubs', endpoint='hubs')
api.add_resource(UserResource, '/users/<id>', endpoint='user')
