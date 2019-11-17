import csv
from database import *
import json
from model.algorithms import *


def query_db(query, args=(), one=False):
    mycursor.execute(query, args)
    r = [dict((mycursor.description[i][0], value) \
              for i, value in enumerate(row)) for row in mycursor.fetchall()]
    return (r[0] if r else None) if one else r


def read_movies():
    sql = "INSERT INTO movies (id, title, year) VALUES (%s, %s, %s)"
    with open('././csv/movies.csv', 'r') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=';')
        for row in readcsv:
            if row[0].isnumeric():
                val = (row[0], row[1], row[2])
                mycursor.execute(sql, val)


def read_users():
    sql = "INSERT INTO users (userId, name) VALUES (%s, %s)"
    with open('././csv/users.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=';')
        for row in readcsv:
            if row[0].isnumeric():
                val = (row[0], row[1])
                mycursor.execute(sql, val)


def read_ratings():
    sql = "INSERT INTO ratings (userId, movieId, rating) VALUES (%s, %s, %s)"
    with open('././csv/ratings.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=';')
        for row in readcsv:
            if row[0].isnumeric():
                val = (row[0], row[1], row[2])
                mycursor.execute(sql, val)


def get_ratings_from_all_unrated_movies_from_user(userid):
    sql = "SELECT * FROM ratings WHERE NOT ratings.movieId = ANY (SELECT movieId FROM ratings " \
          "WHERE userId =%s); "
    stm = (userid,)
    my_query = query_db(sql, stm)
    return my_query


def get_rating():
    sql = "SELECT * FROM ratings"
    my_query = query_db(sql)
    return my_query


def get_movies():
    sql = "SELECT * FROM movies"
    my_query = query_db(sql)
    return my_query


def get_users():
    sql = "SELECT * FROM users"
    my_query = query_db(sql)
    return my_query


def get_user_by_id(userid):
    sql = "SELECT * FROM users WHERE userId = %s"
    stm = (userid,)
    my_query = query_db(sql, stm)
    return my_query


def get_user_id_by_name(user):
    sql = "SELECT userId FROM users WHERE name = %s"
    stm = (user,)
    my_query = query_db(sql, stm)
    return my_query


def get_ratings_from_user(userid):
    sql = "SELECT * FROM ratings WHERE userId = %s"
    stm = (userid,)
    my_query = query_db(sql, stm)
    return my_query


def calculate_euclidean(selected_user):
    res = {}
    for users in get_users():
        if not selected_user == users["userId"]:
            res[users["name"]] = {"distance": euclidean(get_ratings_from_user(selected_user),
                                                        get_ratings_from_user(users["userId"])),
                                  "userId": users["userId"]}
    return res


def calculate_pearson(selected_user):
    res = {}
    for users in get_users():
        if not selected_user == users["userId"]:
            res[users["name"]] = {"distance": pearson(get_ratings_from_user(selected_user),
                                                      get_ratings_from_user(users["userId"])),
                                  "userId": users["userId"]}
    return res


def get_result(user, sim, res):
    print(user)
    print(sim)
    amount = int(res)
    return get_weigted_score_from_user(user, sim, amount)


def get_weigted_score_from_user(user, method, amount):
    selected_user = get_user_id_by_name(user)[0]["userId"]
    if method == 'Pearson':
        euclidean_from_users = calculate_pearson(selected_user)
    else:
        euclidean_from_users = calculate_euclidean(selected_user)

    unrated_movies_from_users = get_ratings_from_all_unrated_movies_from_user(selected_user)
    res = {}
    arr = []
    for movie in get_movies():
        tmp = {}
        for user in unrated_movies_from_users:
            if str(movie["id"]) == str(user["movieId"]):
                arr.append(movie["id"])
                name = get_user_by_id(user["userId"])
                num1 = user["rating"]
                num2 = euclidean_from_users[name[0]["name"]]["distance"]
                weighted_s = (float(num1) * float(num2))
                tmp[user["userId"]] = {'weigted': weighted_s, 'sum': num2}
        if movie["id"] in arr:
            res[movie["title"]] = tmp

    return calculate_weighted_score_for_movies(res, amount)


def calculate_weighted_score_for_movies(result, amount):
    arr = []
    objs = {}
    tmp = {}
    keys = list(result.keys())
    for idx, obj in enumerate(result.values()):
        w = 0
        s = 0
        for val in obj.values():
            w += float(val["weigted"])
            s += float(val["sum"])

        arr.append({'movie': keys[idx], 'weighted_score': (w / s)})

    sorted_arr = sorted(arr, key=lambda i: i['weighted_score'], reverse=True)
    return sorted_arr[:amount]
