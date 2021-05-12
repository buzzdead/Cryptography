from HW_INF143.mandatory3.RsaUtil import *

p, a, d = 59, 3, 23
x = 17
rsa = RsaUtil(p, a, d)
rsa.ephermal_key = 25
rsa.public_key = pow(a, d, p)

r, s = rsa.get_signature(x)
rsa.verify_signature(r, s, x)