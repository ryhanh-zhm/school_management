import random
import string

def generate_password(lenght=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(lenght))