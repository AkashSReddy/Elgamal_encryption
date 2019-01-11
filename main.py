import prime_generator
import random
import inverse

def find_primitive_root(p):
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1
    while (1):
        g = random.randint(2, p - 1)
        if not (pow(g, (p - 1) // p1, p) == 1):
            if not pow(g, (p - 1) // p2, p) == 1:
                return g

def key_generator():
    p = prime_generator.generate_prime_number()
    g = find_primitive_root(p)
    private = random.randint(2, p - 2)
    public = pow(g, private, p)
    return {"p": p, "private": private, "public": public, "gen": g}

def ascii(message):
    l = []
    for i in message:
        l.append(ord(i))
    return l

def tochar(message):
    l = [chr(i) for i in message]
    return "".join(l)

def Encrypt(message, paras):
    cipher = []
    for i in message:
        k = random.randint(2, paras['p'] - 2)
        K = pow(paras['public'], k, paras['p'])
        c1 = pow(paras['gen'], k, paras['p'])
        c2 = (K * i) % paras['p']
        cipher.append([c1, c2])
    return cipher

def Decrypt(ciphertext, paras):
    dec = []
    op = pow(ciphertext['c1'], paras['private'], paras['p'])
        inv = inverse.modinv(op, paras['p'])
        dec.append((ciphertext['c2'] * inverse.modinv(op, paras['p'])) % paras['p'])
    return dec
if __name__ == "__main__":
    paras = key_generator()
    message = input('Enter the message: ')
    message = ascii(message)
    # dec = []
    # for i in message:
    #     k = random.randint(2, paras['p'] - 2)
    #     K = pow(paras['public'], k, paras['p'])
    #     c1 = pow(paras['gen'], k, paras['p'])
    #     c2 = (K * i) % paras['p']
        
    #     # print('C1 = ', c1, '\n\n\nC2 = ', c2)

    #     op = pow(c1, paras['private'], paras['p'])
    #     inv = inverse.modinv(op, paras['p'])
    #     # print("\n\n\n inv - ", inv)
    #     dec.append((c2 * inverse.modinv(op, paras['p'])) % paras['p'])
    #     # print("\n\n\n\n Plain - ", plain)
    # print(tochar(dec))

    