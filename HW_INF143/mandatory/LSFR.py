#!/usr/bin/env python3

from functools import reduce
from operator import xor, and_

from BitVector import BitVector


def run_sequence(register):
    for i in range(2 ** len(register.sequence) - 1):
        register.step()
        #print("Step {}\n{}".format(i + 1, register))


# Kind of did this in the last minute as i forgot about it, hope it counts for some points.
def make_groups(all_seq):
    groups = {}
    for i in range(len(all_seq)):
        group = []
        for j in range(1, len(all_seq)):
            if all_seq[i][1:16] == all_seq[j][0:15] or all_seq[i][2:16] == all_seq[j][0:14]:
                group.append(all_seq[i])
                group.append(all_seq[j])
        groups[i] = group
    print("\nGroups:")
    for k in groups:
        print(k)
        print(groups[k])

def run_all_sequences(reg, tap, multitaps):
    all_seq = [[0] * (2 ** reg)] * (2 ** reg)
    for i in range(2 ** reg):
        bv = BitVector(intVal=i, size=reg)
        register = LFSR(fill=[k for k in bv], taps=tap, multitaps=multitaps)
        run_sequence(register)
        all_seq[i] = register.sequence
    print("The sequences are: ")
    for j in range(len(all_seq)):
        seq_bv = BitVector(intVal=j, size=4)
        print("Initial sequence: {}, sequence: {}".format(seq_bv, all_seq[j]))
    make_groups(all_seq)


class LFSR:

    def __init__(self, fill, taps, multitaps):
        self.sequence = fill.copy()
        self.register = fill
        self.taps = taps
        self.multitaps = multitaps

    def step(self):
        new_bit = reduce(xor, [self.register[t] for t in
                               self.taps])
        if self.multitaps:
            new_bit2 = reduce(and_, [self.register[t] for t in
                                     self.multitaps])
            new_bit = new_bit ^ new_bit2

        del self.register[0]
        self.register.append(new_bit)
        self.sequence.append(new_bit)
        return self.register[-1]

    def __str__(self):
        return "<LFSR: {}, taps: {}>".format(''.join(map(str, self.register)), self.taps)


def main():
    # Initializes the register length, i.e the size of the LFSR, and at what position the taps should be.
    # In this exercise it was in the right-most position, s_t. So tap is set to position 4.
    reg = 4
    tap = [0]
    multitaps = [1, 2]
    # As there was just two positions being multiplied I made it simple with just a 1 dimensional array,
    # called multitaps which is set for position 2 and 3.
    run_all_sequences(reg, tap, multitaps)


if __name__ == '__main__':
    main()
