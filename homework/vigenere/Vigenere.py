import string

alphabet_string = string.ascii_uppercase
alphabet = list(alphabet_string)
alphabet_pos = {}


def map_alphabet():
    for i in range(len(alphabet)):
        alphabet_pos[alphabet[i]] = i


def vigenere_encrypt(plaintext, keyword):
    plaintext = str(plaintext)
    ciphertext = ""
    for i in range(len(plaintext)):
        plaintext_chr = plaintext[i].upper()
        keyword_chr = keyword[i % len(keyword)]

        plaintext_chr_pos = alphabet_pos.get(plaintext_chr)
        keyword_chr_pos = alphabet_pos.get(keyword_chr)
        char_pos = (plaintext_chr_pos + keyword_chr_pos) % 26

        if plaintext[i].islower():
            ciphertext += str(alphabet[char_pos]).lower()
        else:
            ciphertext += alphabet[char_pos]

    return ciphertext


def read_files():
    input_file = open("input.txt")
    key_file = open("key.txt")

    input_plain = input_file.readline()
    key = key_file.readline()

    input_file.close()
    key_file.close()

    return input_plain, key


if __name__ == "__main__":
    map_alphabet()
    [text_to_encrypt, key_to_use] = read_files()
    output = vigenere_encrypt(text_to_encrypt, key_to_use)

    output_file = open("output.txt", "w")
    output_file.write(output)
    output_file.close()
