from BitVector import *

a = BitVector(bitstring='01101')
b = BitVector(bitstring='11001110')
modulus = BitVector(bitstring = '100011011')
print(a.gf_multiply_modular(b, modulus, 8))

#0010110000110
#    100011011
