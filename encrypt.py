import hashlib
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

password = "nevimcosemmamnapsatuz"

salt = b'&\xf9\x19\xa32`\x81\xc6\xf0\xcb\xab^\xc2\x87\x8c\xc7\xe9\x84\x82z\xd5\x7f\xe2\x88KYH\x9b\xfe\xb1\xca\x8b'

key = PBKDF2(password, salt, dkLen=32, count=100000, prf=lambda p, s: hashlib.sha256(p + s).digest())

message = "mira je gej"

cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))

print(cipher.iv)
print(ciphertext)

with open('encrypted.bin','wb') as f:
    f.write(cipher.iv)
    f.write(ciphertext)
    f.close()