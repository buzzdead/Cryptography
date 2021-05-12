from BitVector import *

p = 467
alpha = 2
a = 228
b = 57

k_pub_a = pow(alpha, a, p)
k_pub_b = pow(alpha, b, p)

common_key = pow(k_pub_a, b, p)
common_key_2 = pow(k_pub_b, a, p)

print(common_key == common_key_2)