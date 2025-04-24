import random
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def inverse_mod(a, n):
    t, new_t = 0, 1
    r, new_r = n, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None 
    if t < 0:
        t = t + n
    return t

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def add_points(P, Q, a, n):
    if P.x == Q.x and P.y == Q.y:
        num = (3 * P.x**2 + a) % n
        den = (2 * P.y) % n
    else:
        num = (Q.y - P.y) % n
        den = (Q.x - P.x) % n

    inv_den = inverse_mod(den, n)
    if inv_den is None:
        return gcd(den, n)  

    lam = (num * inv_den) % n
    x3 = (lam**2 - P.x - Q.x) % n
    y3 = (lam * (P.x - x3) - P.y) % n
    return Point(x3, y3)

def scalar_mult(k, P, a, n):
    R = P
    for i in range(1, k):
        result = add_points(R, P, a, n)
        if isinstance(result, int):  
            return result
        R = result
    return None

def lenstra_ecm(N, B=50):
    while True:
        x = random.randint(1, N-1)
        y = random.randint(1, N-1)
        a = random.randint(1, N-1)
        b = (y**2 - x**3 - a*x) % N

        P = Point(x, y)

        try:
            k = math.prod([p**int(math.log(B, p)) for p in range(2, B) if is_prime(p)])
        except OverflowError:
            k = 2**16 

        factor = scalar_mult(k, P, a, N)
        if factor and factor != N:
            return factor

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def factor_all_ecm(N, B=50):
    """Return all prime factors of N using Lenstra ECM."""
    factors = []

    def _factor(n):
        if is_prime(n):
            factors.append(n)
            return
        factor = lenstra_ecm(n, B)
        if factor is None or factor == n:
            factors.append(n)
            return
        _factor(factor)
        _factor(n // factor)

    _factor(N)
    return sorted(factors)

N = 21
all_factors = factor_all_ecm(N)
print(f"All factors of {N}: {all_factors}")
