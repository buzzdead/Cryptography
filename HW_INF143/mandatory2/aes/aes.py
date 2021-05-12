from BitVector import *
from collections import deque
import sbox

modulus = BitVector(bitstring='100011011')  # Taken from P(x) in the book

column_matrix = [
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
]


class AES():
    def __init__(self):
        self.c = []
        self.cipher_length = 128

    def add_round_key(self, k, p):
        new_c = list(k[i:i + 8].__xor__((p[i:i + 8])).intValue() for i in range(0, self.cipher_length, 8))
        new_c2 = list(new_c[i:i + 4] for i in range(0, len(new_c), 4))
        self.c = new_c2

    def sub_bytes(self):
        new_c = self.c.copy()
        for row in range(len(self.c)):
            for col in range(row):
                val = self.c[row][col]
                new_c[row][col] = sbox.s_box[val]
        self.c = new_c

    def shift_rows(self):
        rows = self.c.copy()
        new_c = [[0] * 4] * 4
        for i in range(len(rows)):
            queue_row = deque(rows[i])
            queue_row.rotate(i)
            new_c[i] = list(queue_row)
        self.c = new_c

    def mix_columns(self):
        new_c = self.c.copy()
        for i in range(len(self.c)):
            for k in range(4):
                c = BitVector(intVal=0, size=8)
                for j in range(4):
                    a = BitVector(intVal=self.c[j][k])  # B0-B5-B10-B15 etc.
                    b = BitVector(intVal=column_matrix[k][j])  # The values from the given row in the static matrix.
                    d = a.gf_multiply_modular(b, modulus, 8)
                    c ^= d
                new_c[i][k] = c.intValue()

    def print(self):
        for row in self.c:
            print(row)
        print()


k = BitVector(hexstring='2b7e151628aed2a6abf7158809cf4f3c')
p = BitVector(hexstring='3243f6a8885a308d313198a2e0370734')

aes = AES()
aes.add_round_key(k, p)
aes.print()
aes.sub_bytes()
aes.print()
aes.shift_rows()
aes.print()
aes.mix_columns()
aes.print()

# Adding the final key, just creates a new hexstring from the original cipher matrix first.
k2 = ""
for j in aes.c:
    for i in j:
        bv = BitVector(intVal=i, size=8)
        k2 += bv.getHexStringFromBitVector()
k2 = BitVector(hexstring=k2)
aes.add_round_key(k, k2)

aes.print()
