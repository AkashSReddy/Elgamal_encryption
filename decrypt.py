def inverse(a, m):
    return pow(a, m-2, m)


def decrypt(cipherL, privateA, prime):
    plainL = []
    for i in cipherL:
        yy = pow(i[0], privateA, prime)
        mm = (i[1]*inverse(yy, prime)) % prime
        plainL.append(mm)
    return plainL
