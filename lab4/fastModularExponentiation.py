# https://ru.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation


def getPowerOfTwoModC(A, C, n):
    result = [A % C]
    for i in range(1, n):
        result.append(result[i - 1] ** 2 % C)
    return result


def fastModularExponentiation(A, B, C):
    binaryB = list(reversed(list(map(int, "{0:b}".format(B)))))
    modC = getPowerOfTwoModC(A, C, len(binaryB))

    result = 1
    for i in range(len(binaryB)):
        if binaryB[i]:
            result *= modC[i]
    result %= C
    return result