from Crypto.Random import get_random_bytes


def generate_salt():
    salt = get_random_bytes(32)
    return salt