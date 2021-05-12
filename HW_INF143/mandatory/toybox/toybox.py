from BitVector import *

sbox = [14, 4, 13, 1, 2, 15, 11, 8,
        3, 10, 6, 12, 5, 9, 0, 7]


# Takes a pair of plaintexts ciphertexts and tries some combination of xors from the DDS.
def find_possible_keys(pair, combo, start, end):
    pair_1 = BitVector(intVal=pair[0], size=8)
    pair_2 = BitVector(intVal=pair[2], size=8)
    combo_1 = BitVector(intVal=combo[0])
    combo_2 = BitVector(intVal=combo[1])

    # Plaintext xor with some DDS xor could contain the key.
    key_possibility_1 = pair_1[start:end].__xor__(combo_1)
    key_possibility_2 = pair_2[start:end].__xor__(combo_2)
    assert key_possibility_1 == key_possibility_2
    return key_possibility_1.intValue()


def find_combinations(combo):
    row_combinations = []
    for i in range(16):
        for j in range(16):
            if i ^ j == combo[0]:  # Pair of numbers that xors into the given dx xor from the DDS table.
                if sbox[i] ^ sbox[j] == combo[1]:  # Pair of numbers that xors into the given dy xor from the DDS table.
                    row_combinations.append(i)
                    row_combinations.append(j)
    return row_combinations  # Returns all the combinations pairwise.


pairs = {}
delta_pairs = {}
permutation = [7, 5, 3, 1, 0, 2, 4, 6]
permutation2 = [4, 3, 5, 2, 6, 1, 7, 0]  # Reverse of permutation


# Just permutes the ciphertext to what it originally was.
def permute(old_array):
    array = []
    for i in range(len(old_array)):
        tmp = BitVector(intVal=old_array[i], size=8)
        if i % 2 != 0:
            tmp = tmp.permute(permutation2)
        array.append(tmp.intValue())
    return array


# All pairs starts with a character defining the plaintext\ciphertext pair. I.e 'a' or 'b'
def read_key_part(start, end):
    with open("pairs2.txt", "r") as file:
        for line in file:
            entry = line[0]  # The character.
            pairs[entry] = list(map(int, line[2:].split(" ")))
            pairs[entry] = permute(pairs[entry])

            # Takes the pairs, xor and add them to the dictionary containing the xors.
            d1 = BitVector(intVal=pairs[entry][0], size=8)
            d2 = BitVector(intVal=pairs[entry][1], size=8)
            d3 = BitVector(intVal=pairs[entry][2], size=8)
            d4 = BitVector(intVal=pairs[entry][3], size=8)
            dx = d1[start:end].__xor__(d3[start:end])
            dy = d2[start:end].__xor__(d4[start:end])
            delta_pairs[entry] = [dx.intValue(), dy.intValue()]
        file.close()


def find_key(start, end):
    combinations = {}
    for key, value in delta_pairs.items():
        combination = find_combinations(value)
        combinations[key] = combination
    combinations_sorted = (''.join(sorted(combinations, key=lambda k: len(combinations[k]))))
    key = None
    keys = []
    for entry in combinations_sorted:
        for i in range(0, len(combinations[entry]), 2):
            if key is None:
                keys.append(find_possible_keys(pairs[entry], combinations[entry][i:i + 2], start, end))
                if i == len(combinations[entry]) - 2:
                    #print("Keys: {}".format(keys))
                    key = 0
            else:
                key = find_possible_keys(pairs[entry], combinations[entry][i:i + 4], start, end)
                if key in keys:
                    break
    return key


# Finds the 4 left most key bits first
read_key_part(0, 4)
key1 = BitVector(intVal=find_key(0, 4), size=4)
pairs.clear()
delta_pairs.clear()
# Then the 4 right most key bits.
read_key_part(4, 8)
key2 = BitVector(intVal=find_key(4, 8), size=4)
print("The first 4 bits of the key  is {}, and the second 4 bits is {}".format(key1, key2))
print(key1 + key2)
