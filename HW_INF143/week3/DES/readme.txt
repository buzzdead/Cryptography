There are three files: DES, gegnerate_round_keys and SBOX.

To keep it simple I created a file SBOX with all the sboxes,
as well as methods to go through a BitVector to permute all the
blocks of 6 bits of right part of the text to be permuted.

generate_round_keys simply takes the given key and created a key
for every round of the DES cipher:
Permutes, shifts etc.

DES is the main file, it starts and asks for input. First to choose
if you are decrypting or encrypting, which gives a value to mode
which chooses how the process should go. After determining if there
should be padding in line 89, the start_des() method starts iterating
through blocks of 64 bits, now there are two variables that are dependent
on whether it is decrypting or encrypting, start and end, which are placed
such that it is either encrypting from the start of the text or decrypting from
the end of the text. At the end it will remove padding with reorder_plaintext if
it is decrypting, simply checking for the padding at the end.
