from flask import Flask
from flask_restful import Api
from routes.router import *
from flask_cors import CORS
from database import mycursor

app = Flask(__name__)
api = Api(app)
CORS(app)
# read_movies()
# read_users()
# read_ratings()
# mydb.commit()


api.add_resource(Users, '/users/')
api.add_resource(Ratings, '/ratings')
api.add_resource(Movies, '/movies')
api.add_resource(FindTopMatchUser, '/<user>/<sim>/<res>')


if __name__ == '__main__':
    app.run(port='5002')
