from BitVector import *


def xorr(first, last):
    first = BitVector(intVal=first)
    last = BitVector(intVal=last)
    print(first)
    print(last)
    print(first.__xor__(last))

if __name__ == "__main__":
    xorr(32, 34)
