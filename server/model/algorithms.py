import math


def euclidean(a, b):
    sim = 0
    n = 0
    for rA in a:
        for rB in b:
            if rA["movieId"] == rB["movieId"]:
                sim += (float(rA["rating"]) - float(rB["rating"])) ** 2
                n += 1

    if n == 0:
        return 0
    inv = 1 / (1 + sim)
    return inv


def pearson(a, b):
    sum1 = 0
    sum2 = 0
    sum1sq = 0
    sum2sq = 0
    p_sum = 0
    n = 0

    for rA in a:
        for rB in b:
            if rA["movieId"] == rB["movieId"]:
                sum1 += (float(rA["rating"]) * 1)
                sum2 += (float(rB["rating"]) * 1)
                sum1sq += (float(rA["rating"]) ** 2)
                sum2sq += (float(rB["rating"]) ** 2)
                p_sum += float(rA["rating"]) * float(rB["rating"])
                n += 1

    num = p_sum - (sum1 * sum2 / n)
    den = math.sqrt((sum1sq - sum1 ** 2 / n) * (sum2sq - sum2 ** 2 / n))

    if n == 0:
        score = 0
    if num <= 0:
        score = 0
    if num > 0:
        score = num / den

    return score

