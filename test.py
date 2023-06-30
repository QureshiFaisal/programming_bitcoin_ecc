

from signature import Signature
from privatekey import PrivateKey
import hashlib
from fieldelement import FieldElement
from s256point import S256Point, G, N
from point import Point

prime = 223
# a = FieldElement(num=0, prime=prime)
# b = FieldElement(num=7, prime=prime)
# x1 = FieldElement(num=192, prime=prime)
# y1 = FieldElement(num=105, prime=prime)
# x2 = FieldElement(num=17, prime=prime)
# y2 = FieldElement(num=56, prime=prime)
# p1 = Point(x1, y1, a, b)
# p2 = Point(x2, y2, a, b)
# print(p1+p2)

# a = FieldElement(0, prime)
# b = FieldElement(7, prime)
# x1 = FieldElement(num=36, prime=prime)
# y1 = FieldElement(num=111, prime=prime)
# p = Point(x1, y1, a, b)
# print(p+p+p+p)


# a = FieldElement(0, prime)
# b = FieldElement(7, prime)
# x = FieldElement(15, prime)
# y = FieldElement(86, prime)
# p = Point(x, y, a, b)
# print(7*p)

# gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
# gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
# p = 2**256 - 2**32 - 977
# print(gy**2 % p == (gx**3 + 7) % p)

# gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
# gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
# p = 2**256 - 2**32 - 977
# n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
# x = FieldElement(gx, p)
# y = FieldElement(gy, p)
# seven = FieldElement(7, p)
# zero = FieldElement(0, p)
# G = Point(x, y, zero, seven)
# print(n*G)

# print(N*G)

# z = 0xbc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423
# r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
# s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
# px = 0x04519fac3d910ca7e7138f7013706f619fa8f033e6ec6e09370ea38cee6a7574
# py = 0x82b51eab8c27c66e26c858a079bcdf4f1ada34cec420cafc7eac1a42216fb6c4
# point = S256Point(px, py)
# s_inv = pow(s, N-2, N)  # <1>
# u = z * s_inv % N  # <2>
# v = r * s_inv % N  # <3>
# print((u*G + v*point).x.num == r)  # <4>

# e = int.from_bytes(hash256(b'my secret'), 'big')  # <1>
# z = int.from_bytes(hash256(b'my message'), 'big')  # <2>
# k = 1234567890  # <3>
# r = (k*G).x.num  # <4>
# k_inv = pow(k, N-2, N)
# s = (z+r*e) * k_inv % N  # <5>
# point = e*G  # <6>
# print(point)


# message = b'my message'

# # First SHA256 hash
# first_sha256_hash = hashlib.sha256(message)
# first_digest = first_sha256_hash.digest()

# # Second SHA256 hash on the first hash digest
# second_sha256_hash = hashlib.sha256(first_digest)
# second_digest = second_sha256_hash.digest()

# # Convert the second hash digest to an integer
# z = int.from_bytes(second_digest, 'big')

# print(hex(z))


# my_secret = b'my secret'

# # First SHA256 hash
# first_sha256 = hashlib.sha256(my_secret)
# first_hash = first_sha256.digest()

# # Second SHA256 hash on the first hash digest
# second_sha256 = hashlib.sha256(first_hash)
# second_hash = second_sha256.digest()

# # Convert the second hash digest to an integer
# e = int.from_bytes(second_hash, 'big')
# k = 1234567890
# r = (k*G).x.num
# k_inv = pow(k, N-2, N)
# s = (z+r*e) * k_inv % N
# point = e*G
# print(point)
# print(hex(z))
# print(hex(r))
# print(hex(s))

# priv = PrivateKey(5001)
# print(priv.point.sec(compressed=True).hex())

# r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
# s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
# sig = Signature(r, s)
# print(sig.der().hex())


# priv = PrivateKey(5002)
# print(priv.point.address(compressed=False, testnet=True))

priv = PrivateKey(5003)
print(priv.wif(compressed=True, testnet=True))
