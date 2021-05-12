from BitVector import *


def xgcd(a, b):
    if a < 0 or b < 0:
        sys.exit("\n Integers a, b cannot be negative!\n")
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        return xgcd(b, a)
    r = [a, b]
    u = [1, 0]
    v = [0, 1]
    while r[-2] % r[-1] != 0:
        q = r[-2] // r[-1]
        r.append(r[-2] - q * r[-1])
        u.append(u[-2] - q * u[-1])
        v.append(v[-2] - q * v[-1])
    return r[-1], v[-1], u[-1]


e = 17
p = 16870358856335444017
q = 14379358502208144409

n = p * q
phi = (p - 1) * (q - 1)
bv = BitVector(textstring="RSAPKC")
m = bv.intValue()

c = pow(m, e, n)

abc = xgcd(e, phi)
d = abc[1]

print(pow(c, d, n))

dP = d % (p - 1)
dQ = d % (q - 1)
abcd = xgcd(q, p)
qInv = abcd[1]

c1 = pow(c % p, dP, p)
c2 = pow(c % q, dQ, q)

m2 = (c2 + (c1 - c2) * q * qInv) % n


print("So, c = {} \n d = {}, \n".format(c, d))
print("For verification, c^d mod n = {} \n which is equal to m = {}".format(pow(c, d, n), m))
print("\nFurthermore we have dP = {}, dQ = {}, qInv = {}".format(dP, dQ, qInv))
print("If we calculate m2 we should get the same as m, m2 = {}".format(m2))
print("When using the CRT factors to decrypt we still get the correct message, i.e m == m2: {}".format(m2 == m))

