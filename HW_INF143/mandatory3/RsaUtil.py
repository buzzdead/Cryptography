import sys


class RsaUtil:
    def __init__(self, prime, primitive_element, private_key):
        self.prime = prime
        self.primitive_element = primitive_element
        self.private_key = private_key
        self.ephermal_key = None
        self.public_key = None

    def xgcd(self, a, b):
        if a < 0 or b < 0:
            sys.exit("\n Integers a, b cannot be negative!\n")
        if a == b:
            return a
        if a == 0:
            return b
        if b == 0:
            return a
        if a < b:
            return self.xgcd(b, a)
        r = [a, b]
        u = [1, 0]
        v = [0, 1]
        while r[-2] % r[-1] != 0:
            q = r[-2] // r[-1]
            r.append(r[-2] - q * r[-1])
            u.append(u[-2] - q * u[-1])
            v.append(v[-2] - q * v[-1])
        return r[-1], v[-1], u[-1]

    def get_inverse_ephermal(self):
        return self.xgcd(self.ephermal_key, self.prime - 1)[1]

    def get_signature(self, message):
        r = pow(self.primitive_element, self.ephermal_key, self.prime)
        s = ((message - self.private_key * r) * self.get_inverse_ephermal()) % (self.prime - 1)
        return r, s

    def verify_signature(self, r, s, message):
        t = (pow(self.public_key, r, self.prime) * pow(r, s, self.prime)) % self.prime
        print("Signature verification code from signature is {}, and it is supposed to be {} "
              .format(t, pow(self.primitive_element, message, self.prime)))

    # Explained in readme
    def generate_third_party_signature(self, x1, s1, new_x2):
        third_party_signature = s1 - ((x1 - new_x2) * self.get_inverse_ephermal() % (self.prime - 1))
        return third_party_signature
