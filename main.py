import prime_generator
import random

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
    a = random.randint(2, p - 2)
    return {"p": p, "g": g, "a": a}

if __name__ == "__main__":
    paras = key_generator()