from RsaUtil import *

p, a = 59, 3
rsa = RsaUtil(p, a, None)
x1, x2, new_x2 = 13, 18, 19
rsa.public_key = 29

r1, s1 = 25, 20
r2, s2 = 25, 7

# Explained in readme
k = (x1 - x2) * rsa.xgcd(s1 - s2, p - 1)[1] % (p - 1)
rsa.ephermal_key = k


tps = rsa.generate_third_party_signature(x1, s1, new_x2)
rsa.verify_signature(r1, tps, new_x2)


