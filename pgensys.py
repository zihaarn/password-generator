import secrets
import string

def generate_password(length=10):
    alphabet = string .ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in
        
range(length))
    return password

for _ in range(10):
    password = generate_password()
    print (password)


