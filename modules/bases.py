import base64
import base58

alphabet = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
base_count = len(alphabet)
		
def debase32(encoded):
    return str(base64.b32decode(encoded).decode("utf-8"))

def debase58(encoded):
    return str(base58.b58decode(encoded).decode("utf-8"))

def debase64(encoded):
    return str(base64.b64decode(encoded).decode("utf-8"))