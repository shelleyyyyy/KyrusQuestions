import hashlib


def create_hash(string):
    hash_ = hashlib.md5(string.encode()).hexdigest()
    return hash_



print(create_hash(""))
