from BitVector import *

p = 16870358856335444017
alpha = 5
a = 87035885633544
b = 335444017

k_pub_a = pow(alpha, a, p)
k_pub_b = pow(alpha, b, p)

common_key = pow(k_pub_a, b, p)
common_key_2 = pow(k_pub_b, a, p)

print(common_key == common_key_2)