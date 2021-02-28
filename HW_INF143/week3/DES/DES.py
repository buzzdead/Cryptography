from BitVector import *
import generate_round_keys as keys
import SBOX as sbox

initial_permutation = [
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6]

initial_permutation_inverse = [39, 7, 47, 15, 55, 23, 63, 31,
                               38, 6, 46, 14, 54, 22, 62, 30,
                               37, 5, 45, 13, 53, 21, 61, 29,
                               36, 4, 44, 12, 52, 20, 60, 28,
                               35, 3, 43, 11, 51, 19, 59, 27,
                               34, 2, 42, 10, 50, 18, 58, 26,
                               33, 1, 41, 9, 49, 17, 57, 25,
                               32, 0, 40, 8, 48, 16, 56, 24]

expansion_permutation = [31, 0, 1, 2, 3, 4,
                         3, 4, 5, 6, 7, 8,
                         7, 8, 9, 10, 11, 12,
                         11, 12, 13, 14, 15, 16,
                         15, 16, 17, 18, 19, 20,
                         19, 20, 21, 22, 23, 24,
                         23, 24, 25, 26, 27, 28,
                         27, 28, 29, 30, 31, 0]

f_permutation = [
    15, 6, 19, 20, 28, 11, 27, 16,
    0, 14, 22, 25, 4, 17, 30, 9,
    1, 7, 23, 13, 31, 26, 2, 8,
    18, 12, 29, 5, 21, 10, 3, 24
]


def get_padding(ptxt_bv):
    padding = ''
    length = 8 - (len(ptxt_bv) // 8) % 8
    if length > 0:
        for j in range(length):
            padding += "0{}".format(str(length))
    return padding


def reorder_plaintext(output_text):
    new_output_text = ""
    for k in range(len(output_text), 0, -16):
        new_output_text += output_text[k - 16:k]

    for j in range(1, 8):
        possible = "0{}".format(j)
        if new_output_text[-j * 2: len(new_output_text)] == possible * j:
            new_output_text = new_output_text[0:-j * 2]
    return new_output_text


def start_des():
    L = []  # List for storing the left side bits.
    R = []  # List for storing the right side bits.
    mode = input("Type 0 for decryption, 1 for encryption: ")
    decrypt = False
    encrypt = False
    if mode == "0":
        decrypt = True
    else:
        encrypt = True
    key_text = input("Enter key in hexadecimal: ")
    plaintext = input("Enter text to be encrypted or decrypted in hexadecimal: ")

    # Initializes the vectors and generates the keys.
    ptxt_bv = BitVector(hexstring=plaintext)  # The hexadecimal text to be encrypted\decrypted.
    key_bv = BitVector(hexstring=key_text)  # The key used for encryption\decryption.
    encryption_key = keys.get_encryption_key(key_bv)
    round_keys = keys.generate_round_keys(encryption_key)
    initial_vector = "7A65B3757269A47E"
    iv_bv = BitVector(hexstring=initial_vector)
    output_text = ""

    if decrypt:
        round_keys.reverse()

    # CBC
    # If the text is a multiplication of 64 bits then padding is skipped.
    if len(ptxt_bv) % 64 != 0:
        padding = BitVector(hexstring=get_padding(ptxt_bv))
        ptxt_bv += padding
    total_bits = len(ptxt_bv)
    one_block = (total_bits == 64)

    # Goes through each block of 64 bits.
    for bit_pos in range(0, total_bits, 64):
        iv = BitVector(hexstring=iv)  # Reset iv value to the new ciphertext \ iv.

        # Takes each block starting from the last one when decrypting.
        if decrypt:
            bit_start = total_bits - bit_pos - 64
            bit_end = total_bits - bit_pos
            input_text = ptxt_bv[bit_start:bit_end]
        else:
            input_text = ptxt_bv[bit_pos:bit_pos + 64]

        # Plaintext xor IV.
        if encrypt and not one_block:
            input_text = input_text.__xor__(iv)

        ip = input_text.permute(initial_permutation)
        old_iv = iv.deep_copy()  # This will be the xor combination of an iv with a plaintext.
        iv = run_des(round_keys, R, L, ip)

        if decrypt and not one_block:
            last_block = (bit_pos == total_bits - 64)

            if bit_pos > 0:
                # Takes the new cipher text and xor it with the old block.
                plaintext_block = input_text.__xor__(old_iv)
                output_text += plaintext_block.getHexStringFromBitVector()

            # If it is the last block then it is xor'ed with the initial vector.
            if last_block:
                cipher_block = BitVector(hexstring=iv)
                original_iv = BitVector(hexstring="7A65B3757269A47E")
                plaintext_block = cipher_block.__xor__(original_iv)
                output_text += plaintext_block.getHexStringFromBitVector()
        else:
            output_text += iv
        L.clear()
        R.clear()

    if decrypt:
        output_text = reorder_plaintext(output_text)
    print(output_text)


# Goes through the DES operations once a the keys and the message has been initialized.
def run_des(round_keys, R, L, ip):
    [LIP, RIP] = ip.divide_into_two()
    R0 = BitVector(bitstring=RIP)
    L0 = BitVector(bitstring=LIP)
    L.append(L0)
    R.append(R0)

    for i in range(16):
        key = round_keys[i]
        L.append(R[i])
        right = R[i].permute(expansion_permutation)
        right = right.__xor__(key)
        right = sbox.s_permute(right)
        right = right.permute(f_permutation)
        right = right.__xor__(L[i])
        R.append(right)
    final = R[16] + L[16]
    final = final.permute(initial_permutation_inverse)
    return final


if __name__ == "__main__":
    start_des()
