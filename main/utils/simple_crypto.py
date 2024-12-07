from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

PREDEFINED_KEY = "drW9i4ozZ0n4S0He9hTnW5mmt98GYxUgDd8nJPtuxag="  

# Decodificando a chave base64
key = base64.b64decode(PREDEFINED_KEY)

# Função para criptografar os dados
def encrypt(data: str) -> str:
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv + ct

# Função para descriptografar os dados
def decrypt(data: str) -> str:
    iv = base64.b64decode(data[:24])
    ct = base64.b64decode(data[24:])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size) 
    return pt.decode('utf-8')

def decrypt_cpf(encrypted_cpf):
    # Usando o algoritmo de cifra XOR ou outro método simples (conforme o que você implementou)
    decrypted_cpf = ''.join(chr(ord(c) ^ 42) for c in encrypted_cpf)  # Exemplo de cifra simples XOR
    return decrypted_cpf
