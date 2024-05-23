import rsa


def encrypt(message: str):
    with open('pub_key.rsa', 'rb') as f:
        pub_key_data = f.read()

    pub_key = rsa.PublicKey.load_pkcs1(pub_key_data)

    encrypted_message = rsa.encrypt(message.encode(), pub_key)
    return encrypted_message
