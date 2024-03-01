import random

# https://stackoverflow.com/a/1210632/489239

def unique_id():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1


unique_sequence = unique_id()

def UID(prefix:str=''):
    return f"{prefix}-{hex(next(unique_sequence))[2:]}"
