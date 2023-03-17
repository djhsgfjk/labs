import random
from extendedEuclideanAlgorithm import *
import time


def trialComposite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True

def isPrime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trialComposite(a, d, n, s):
            return False
    return True


def getPrimePQ(a, b):
    p = -1
    q = -1
    while True:
        num = random.randint(a, b)
        if isPrime(num):
            if p == -1:
                p = num
            elif q == -1:
                q = num
                break
    return p, q


# https://habr.com/ru/post/534014/
# https://e-maxx.ru/algo/reverse_element
def generateKeys(bits):
    startTime = time.time()
    bit_start = '1' + '0' * (bits - 1)
    bit_end = '1' + '1' * (bits - 1)
    first_num = int(bit_start,2) + 1
    last_num = int(bit_end,2)
    p, q = getPrimePQ(first_num, last_num)
    n = p * q
    phi = (p - 1) * (q - 1)
    e, d = 0, 0
    while True:
        e = random.randint(3, phi-1)
        gcd, x, y = extendedEuclideanAlgorithm(e, phi)
        if gcd == 1:
            d = (x % phi + phi) % phi
            break
    print("--- Keys generated in %s seconds ---" % (time.time() - startTime))
    return p, q, n, phi, e, d
