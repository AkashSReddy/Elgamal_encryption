import prime_generator
import random
import decrypt


def ascii(string):
    data = []
    for i in string:
        data.append(ord(i))
    return data


def encrypt(prime, primitive, privateA, dataL):
    publicA = pow(primitive, privateA, prime)
    cipher = []
    for i in dataL:
        L = []
        k = random.randint(1, 99)
        K = pow(publicA, k, prime)
        c = pow(primitive, k, prime)
        cc = (K*i) % prime
        L.append(c)
        L.append(cc)
        cipher.append(L)
    return cipher


print("message : Akash")
x = "Akash"

yy = ascii(x)
# print(encrypt(19, 10, 5, yy))
cp = encrypt(19, 10, 5, yy)
print(cp)
new = decrypt.decrypt(cp, 5, 19)
print(new)
print(yy)

# p = prime_generator.generate_prime_number()
