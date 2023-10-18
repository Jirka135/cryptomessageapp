from Crypto.Random import get_random_bytes
from icecream import ic
import bcrypt

def generate_salt():
    salt = bcrypt.gensalt(16)
    return salt

