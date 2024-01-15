import hashlib

def encrypt_password(password):
    # Simple hash function for password hashing
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def encrypt_data(data, key):
    # Simple encryption function (replace with a more secure method for production)
    encrypted_data = "".join([chr(ord(char) ^ ord(key)) for char in data])
    return encrypted_data
