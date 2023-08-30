#Triple DES is basically DES but three times (like the name suggests)
#It involves a series of encryption, decryption then encryption, each stage using an independent DES subkey

#Import required Triple DES libraries and key generator methods
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

#Key generation
while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))  #24 bytes = 3 keys (8 bytes each)
        break
    except ValueError:
        pass

#Encryption
def encrypt(msg):
    cipher = DES3.new(key, DES3.MODE_EAX)
    nonce = cipher.nonce                                    #nonce stores random bytes and is stored with ciphertext for decryption.
    ciphertext = cipher.encrypt(msg.encode('ascii'))
    return nonce, ciphertext

#Decryption
def decrypt(nonce, ciphertext):
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('ascii')

#Execution
def DES3_main():
    nonce, ciphertext = encrypt(input("Enter a message:" ))
    plaintext= decrypt(nonce, ciphertext)

    #Output
    print(f"\nCipher text: {ciphertext}")
    print(f"\nPlain text: {plaintext}\n")