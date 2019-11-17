from flask_restful import Resource
from database import mycursor
from model.utils import *


class Users(Resource):
    def get(self):
        return get_users()


class Ratings(Resource):
    def get(self):
        return get_rating()


class Movies(Resource):
    def get(self, user):
        return get_weigted_score_from_user(user)


class FindTopMatchUser(Resource):
    def get(self, user, sim, res):
        return get_result(user, sim, res)

