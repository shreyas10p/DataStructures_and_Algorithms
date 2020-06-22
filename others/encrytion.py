import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import json


class AESCipher:

    def __init__(self, key):
        self.bs = 16
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        message = self._pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(message)).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]




def main():

    f=open("encrypted.txt", "r")
    data = json.loads(f.read())
    f.close()
    crytpoObj = AESCipher("this is my key")
    newList = []
    for x in data:
        newDict = {}
        for key in x.keys():
            keyA = crytpoObj.decrypt(key).decode("utf-8").replace("\n","")
            valA = crytpoObj.decrypt(x[key]).decode("utf-8").replace("\n","")
            newDict[keyA] = valA
            newList.append(newDict)

    print(newList)

if __name__ == '__main__':
    main()
