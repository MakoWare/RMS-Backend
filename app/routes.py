from app.Resources.UserResource import *
from app.Resources.GymResource import *
from app import *


#Users 
api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(UserResource, '/users/<id>', endpoint='user')

#Gyms
api.add_resource(GymListResource, '/gyms', endpoint='gyms')
api.add_resource(GymResource, '/gyms/<id>', endpoint='gym')
