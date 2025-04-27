import random
import string

def generate_email():
    return f"max_kalabin_19_{random.randint(100, 999)}@yandex.ru"

def generate_password(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))