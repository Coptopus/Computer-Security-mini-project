#This technique requires for both peers to use two keys (Public & Private) alternatively to encrypt and decrypt messages
#Sender encrypts message with receipient's public key so that only the receipient can decrypt is with their private key

#Required library for RSA ciphering
import rsa

#Key generation method
def generate_keys():
    (pubkey, privkey) = rsa.newkeys(1024)       #1024 bit or 1 KB key
    with open('keys/pubkey.pem', 'wb') as f:
        f.write(pubkey.save_pkcs1('PEM'))       #Write public key to the keys folder
    with open('keys/privkey.pem', 'wb') as f:
        f.write(privkey.save_pkcs1('PEM'))      #Write private key to the keys folder

#Key loading method
def load_keys():
    with open('keys/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())     #Retreive public key from the keys folder
    with open('keys/privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())   #Retreive private key from the keys folder
    return pubKey, privKey

#Encryption method
def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)

#Decryption method
def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')     #Exception indicates decryption failure
    except:
        return False
    
#Method to provide message with a signature
def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')


#Method to verify the message signature
def verify_sha1(msg, signature, key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

#Execution
def RSA_main():
    #Key generation and input
    generate_keys()
    pubKey, privKey = load_keys()
    message = input("Enter a message: ")

    #RSA encryption & decryption
    ciphertext = encrypt(message, pubKey)
    signature = sign_sha1(message, privKey)
    plaintext = decrypt(ciphertext, privKey)

    #Output and signature verification
    print(f"\nCiphertext:\n{ciphertext}")
    print(f"\nSignature:\n{signature}")

    if plaintext:
        print(f"\nPlaintext:\n{plaintext}")
    else:
        print("\nDecryption failed\n")      #either the message is encrypted in another public key or message was manipulated

    if verify_sha1(plaintext, signature, pubKey):
        print("\nSignature verified, message is authentic\n")
    else:
        print("\nMessage signature couldn't be verified\n")