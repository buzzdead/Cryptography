from BitVector import *
#Decipher not yet been implemented

class BlockCipher:
    def __init__(self, code_book):
        self.size = 4
        self.code_book = code_book
        self.block = []

    # Splits the bits of the plaintext into blocks of the BlockCipher size
    def split_bits(self, ptxt_bv):
        i = 0
        while i + self.size <= len(ptxt_bv):
            self.block.append(ptxt_bv[i:i + 4].intValue())
            i = i + self.size

    # Goes through the block with the list of integers and finds the respective 4 bits from the codebook.
    def encipher(self):
        bitstring = BitVector(size=0)
        for b in self.block:
            ctxt_bv = BitVector(intVal=self.code_book[b], size=4)
            bitstring += ctxt_bv

        # Printing the bytes in hexadecimal format of the ciphertext
        return bitstring

def main():
    code_book = [6, 0, 13, 4, 3, 1, 14, 8, 7, 12, 9, 15, 5, 2, 11, 10]
    ptxt = "hello"
    bv = BitVector(textstring=ptxt)

    # Printing the bytes in hexadecimal format
    print(bv.getHexStringFromBitVector())
    bc = BlockCipher(code_book)
    bc.split_bits(bv)
    cipher_bits = bc.encipher()
    cipher_text = cipher_bits.getTextFromBitVector()
    cipher_hex = cipher_bits.getHexStringFromBitVector()
    print(cipher_hex)






if __name__ == '__main__':
    main()
