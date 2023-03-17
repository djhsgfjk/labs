from fastModularExponentiation import *


def grouper(iterable, n):
    res = []
    for i in range(0, len(iterable), n):
        res.append(iterable[i:i + n])
    return res


def cryptRSA(text, e, n):
    nBinary = "{0:b}".format(n)
    blockMaxLen = len(nBinary) - 1
    textBinary = ''.join(f"{ord(i):08b}" for i in text)
    print(textBinary)
    g = grouper(textBinary, blockMaxLen)
    print(g)
    M = [int(x, 2) for x in g]
    print("M:", M)
    C = []
    result = ""
    for i in range(len(M)):
        c = fastModularExponentiation(M[i], e, n)
        C.append(c)
        cBinary = "{0:b}".format(c)
        result += "0" * (blockMaxLen - len(cBinary)) + cBinary
    print("C:", C)
    return result


def decryptRSA(text, d, n):
    nBinary = "{0:b}".format(n)
    blockMaxLen = len(nBinary) - 1
    g = grouper(text, blockMaxLen)
    C = [int(x, 2) for x in g]
    M = []
    textBinary = ""
    print("C:", C)
    for i in range(len(C) - 1):
        m = fastModularExponentiation(C[i], d, n)
        M.append(m)
        mBinary = "{0:b}".format(m)
        textBinary += "0" * (blockMaxLen - len(mBinary)) + mBinary

    m = fastModularExponentiation(C[-1], d, n)
    M.append(m)
    mBinary = "{0:b}".format(m)
    if len(mBinary) % 8 > 0:
        textBinary += "0" * (8 - (len(mBinary) % 8)) + mBinary
    else:
        textBinary += \
            mBinary
    print("M:", M)
    print(textBinary)
    text = ""
    for letter in grouper(textBinary, 8):
        text += chr(int(letter, 2))
    return text
