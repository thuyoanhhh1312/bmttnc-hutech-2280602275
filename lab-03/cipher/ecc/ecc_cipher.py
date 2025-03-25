import ecdsa, os

if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')
    
class ECCCipher:
    def __init__(self):
        pass
    
    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()
        vk = sk.get_verifying_key()
        
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())
        
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())
            
    def load_keys(self):
        # Sửa lại chế độ mở tệp thành 'rb' (read binary)
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
            
        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())  # Sử dụng VerifyingKey thay vì SigningKey cho public key
        
        return sk, vk
    
    def sign(self, message, key):
        return key.sign(message.encode('ascii'))
    
    def verify(self, message, signature, key):
        _, vk = self.load_keys()
        try:
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadDigestError:
            return False
