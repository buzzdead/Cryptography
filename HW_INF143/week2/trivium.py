#!/usr/local/bin/python

from BitVector import *

def trivium(key_bv, iv_bv, N):
    """
    trivivum keystream generation: len=N (N should be smaller than 2**64)
    arguments key_bv, iv_bv shoule be BitVector objects
    """
    if (len(key_bv) != 80) or (len(iv_bv) != 80) or (N >= 1<<64):
        sys.exit("Arguments Requirement: len(key_bv)=80, len(iv_bv)=80, N<(2**64)")

    keystream_bv = BitVector(size=N)
    state = BitVector(size=288)
    #Key,IV setup
    state[0:80]   = key_bv
    state[93:173] = iv_bv
    state[-3:] = BitVector(bitstring="111")
    # print(state)
    for i in range(4 * 288 + N):
        if i >= 4 * 288:
            j = i - 4 * 288
            keystream_bv[j] = (state[65] ^ state[92]) ^ (state[161] ^ state[176]) ^ (state[242] ^ state[287])
        t1 = state[65] ^ state[92] ^ (state[90] & state[91]) ^ state[170]
        t2 = state[161] ^ state[176] ^ (state[174] & state[175]) ^ state[263]
        t3 = state[242] ^ state[287] ^ (state[285] & state[286]) ^ state[68]
        state.shift_right_by_one()
        state[0] = t3
        state[93] = t1
        state[177] = t2
    return keystream_bv



# test
def main():

    # input from textstring
    # key_bv = BitVector(textstring="cryptograp")
    # iv_bv  = BitVector(textstring="security20")

    # input from hexstring
    key_bv = BitVector(hexstring = "80000000000000000000")
    iv_bv  = BitVector(hexstring = "00000000000000000000")
    # print("key_bv: ", key_bv)
    # print("iv_bv: ", iv_bv)

    plaintext = "ABCD"
    plaintext_bv = BitVector(textstring=plaintext)
    N = len(plaintext_bv)

    keystream_bv = trivium(key_bv, iv_bv, N)
    keystream_bv2 = trivium(key_bv, iv_bv, N)
    print(format(keystream_bv.__xor__(keystream_bv2)))
    print(keystream_bv)
    ciphertext_bv = plaintext_bv ^ keystream_bv
    # print(ciphertext_bv)
    print(ciphertext_bv.get_bitvector_in_hex())
    # print(keystream_bv.get_bitvector_in_hex())

if __name__ == "__main__":
    main()