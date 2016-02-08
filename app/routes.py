from app.Resources.UserResource import *
from app.Resources.GymResource import *
from app.Resources.WallResource import *
from app.Resources.RouteResource import *
from app import *


#Users
api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(UserResource, '/users/<id>', endpoint='user')

#Gyms
api.add_resource(GymListResource, '/gyms', endpoint='gyms')
api.add_resource(GymResource, '/gyms/<id>', endpoint='gym')

#Walls
api.add_resource(WallListResource, '/walls', endpoint='walls')
api.add_resource(WallResource, '/walls/<id>', endpoint='wall')

#Routes
api.add_resource(RouteListResource, '/routes', endpoint='routes')
api.add_resource(RouteResource, '/routes/<id>', endpoint='route')
