# https://e-maxx.ru/algo/export_extended_euclid_algorithm

def extendedEuclideanAlgorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = extendedEuclideanAlgorithm(b % a, a)
    return gcd, y - (b // a) * x, x