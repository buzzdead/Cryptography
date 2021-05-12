import rsa

p = 467
a = 2
d = 105
beta = pow(a, d, p)

i = 213
x = 33

ephermal_key_alice = pow(a, i, p)

masking_key = pow(beta, i, p)

y = (x * masking_key) % p

inv_masking_key = rsa.xgcd(masking_key, p)[1]
decrypted = (y * inv_masking_key) % p
print("Message encrypted is: {} \n ciphertext decrypted is: {}".format(y, decrypted))
