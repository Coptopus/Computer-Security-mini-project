#DES is a simple block cipher technique, the AES technique is an improved and more modern variation of DES

#Import DES and key generation libraries
from Crypto.Cipher import DES
from secrets import token_bytes

#Key generation
key = token_bytes(8)    #8 bit key

#Encryption
def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)         #EAX is a mode of operation for block ciphers (eg. ECB, CBC, OCB, OFB).
    nonce = cipher.nonce                        #nonce stores random bytes and is stored with ciphertext for decryption.
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

#Decryption
def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:                                        #Message could be manipulated or corrupted
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

#Execution
def DES_main():   
    nonce , ciphertext, tag = encrypt(input("Enter a message: "))
    plaintext = decrypt(nonce, ciphertext, tag)

    #Output
    print(f"\nCiphertext: {ciphertext}")

    if not plaintext:                               #Output depends on message integrity
        print("\nMessage is corrupted\n")
    else:
        print(f"\nPlaintext: {plaintext}\n")