#!/usr/bin/env python3

from functools import reduce
from operator import xor

from BitVector import BitVector


def run_sequence(register):
    for i in range(15):
        register.step()
        print("Step {}\n{}".format(i + 1, register))
    print(register.sequence)

def run_all_sequences(reg, tap):
    all_seq = [[0] * (2**reg)] * (2**reg)
    for i in range(2**reg):
        bv = BitVector(intVal=i, size=reg)
        print(bv)
        register = LFSR(fill=[k for k in bv], taps=tap)
        run_sequence(register)
        all_seq[i] = register.sequence
    for seq in all_seq:
        print(seq)



class LFSR():
    '''An implementation of standard linear-feedback shift register.
       fill is the initial state as a list of 0s and 1s
       and taps correspond to indices in the binary number represented by the register.
       Bits on taps influence the next state. Note that taps are indices in binary notation,
       i.e. read from right to left. Example: taps = [3] on a nine-bit register
       is located on (9-1)-3 = 5th position in the array. '''

    def __init__(self, fill, taps):
        self.sequence = fill.copy()
        self.register = fill
        self.taps = taps

    def step(self):
        '''Advance the register by one step. All bits are shifted left by 1 and new bit
        is appended to the right tail. The new bit is a result of xor of the leaving (leftmost) bit
        and bits located at taps before the shift.'''
        new_bit = reduce(xor, [self.register[(len(self.register) - 1) - t] for t in
                               self.taps])  # binary number, read from right to left
        del self.register[0]
        self.register.append(new_bit)
        self.sequence.append(new_bit)
        return self.register[-1]

    def rand(self, k):
        '''Generate a k-bit pseudorandom number using the register.'''
        num = 0
        for _ in range(k):
            num *= 2
            num += self.step()
        return num

    def __str__(self):
        return "<LFSR: {}, taps: {}>".format(''.join(map(str, self.register)), self.taps)


def main():
    """A demo of the LFSR's functionality."""

    # create a new register with initial state 01101000010 and tap at position 8
    register = LFSR(fill=[1, 0, 0], taps=[0, 1])
    #run_sequence(register)
    reg = 3
    tap = [2,1]
    run_all_sequences(reg, tap)


if __name__ == '__main__':
    main()
