find_combinations():
this method just finds all possible combinations for the given dx and dy in the dds table.

find_possible_keys():
for a given position in the dds table there are some combinations, which combined with a pair of plaintexts
and ciphertexts are used to find possible keys.

permute():
the reversed array of what the original permutation does, so this puts the ciphertext back in order.

read_key_part():
takes a position in the ciphertext\plaintext, for example the first 4 bits.
xor's these plaintexts and ciphertexts and puts them in a dictionary for the pairs themselves
and for the dx \ dy pairs.

find_key():
for the dx \ dy pairs it first finds the relevant combinations in the dds table.
sorts this combinations dictionary so that it starts with the entry with the least
number of possible combinations. In such a way it will be faster (i think) to get to
the right key. For the first entry then, it will add all its keys to a list, and for the next
entries it will simply find a key that already exists in that list.