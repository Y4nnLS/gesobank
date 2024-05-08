import rsa

# Generate RSA key pair
def new_key(nbits:int = 1024):
    public_key, private_key = rsa.newkeys(nbits)
    return public_key, private_key

# Encrypt message using RSA public key
def rsa_encrypt_message(public_key, message):
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return encrypted_message

# Decrypt message using RSA private key
def rsa_decrypt_message(private_key, encrypted_message):
    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    return decrypted_message.decode()