import rsa
import base64


def generate_rsa_keys():
    # 生成公钥和私钥
    (pubkey, privkey) = rsa.newkeys(512)

    # 将公钥和私钥保存到文件
    with open('public.pem', 'w') as publickfile:
        publickfile.write(pubkey.save_pkcs1().decode())

    with open('private.pem', 'w') as privatefile:
        privatefile.write(privkey.save_pkcs1().decode())


def decrypt(str_message: str) -> str:
    # 读取私钥
    with open('Security/private.pem', 'r') as privatefile:
        privkey = rsa.PrivateKey.load_pkcs1(privatefile.read().encode())

    # base64解码
    encrypted_message = base64.b64decode(str_message)

    # 解密
    message = rsa.decrypt(encrypted_message, privkey).decode()
    return message


def encrypt(message: str) -> str:
    # 读取公钥
    with open('Security/public.pem', 'r') as publicfile:
        pubkey = rsa.PublicKey.load_pkcs1(publicfile.read().encode())

    # 加密
    encrypted_message = rsa.encrypt(message.encode(), pubkey)

    # base64编码
    str_message = base64.b64encode(encrypted_message).decode()
    return str_message


# 中国海洋大学统一身份认证平台加密
def encrypt_blackboard(message: str) -> str:
    # 读取公钥
    with open('Security/pub_key.rsa', 'r') as publicfile:
        pubkey = rsa.PublicKey.load_pkcs1(publicfile.read().encode())

    # 加密
    encrypted_message = rsa.encrypt(message.encode(), pubkey)
    str_message = base64.b64encode(encrypted_message).decode()
    return str_message


if __name__ == '__main__':
    print(encrypt('s_session_id=9FC896CA91868698D53CC3EF80C1A624;'))
    # print(decrypt(''))