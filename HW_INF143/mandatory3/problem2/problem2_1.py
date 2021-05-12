from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key = DSA.generate(1024)
key_pub = key.publickey().export_key()

file = open('../text.txt', 'r')
text = bytes(file.read(), 'utf-8')
h = SHA256.new(text)

signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(h)
key_pub2 = DSA.import_key(key_pub)
verifier = DSS.new(key_pub2, 'fips-186-3')

print("P: {}".format(key.p))
print("Q: {}".format(key.q))
print("G: {}".format(key.g))
print("Private key: {}".format(key.x))
print("Public key: {}".format(key.y))
print("Signature (r, s): {}".format((signature[0], signature[1])))


try:
    verifier.verify(h, signature)
    print("The message is authentic.")
except ValueError:
    print("The message is not authentic.")
