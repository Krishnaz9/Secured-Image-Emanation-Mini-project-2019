import base64
import binascii
import hashlib
import secrets
import sys

from Crypto.Cipher import AES
from tinyec import registry


def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)


def decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext


def ecc_point_to_256_bit_key(point):
    sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
    sha.update(int.to_bytes(point.y, 32, 'big'))
    return sha.digest()


def encrypt_ECC(curve, msg, pubKey):
    ciphertextPrivKey = secrets.randbelow(curve.field.n)
    sharedECCKey = ciphertextPrivKey * pubKey
    secretKey = ecc_point_to_256_bit_key(sharedECCKey)
    ciphertext, nonce, authTag = encrypt_AES_GCM(msg, secretKey)
    ciphertextPubKey = ciphertextPrivKey * curve.g
    return (ciphertext, nonce, authTag, ciphertextPubKey)


def decrypt_ECC(encryptedMsg, privKey):
    (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
    sharedECCKey = privKey * ciphertextPubKey
    secretKey = ecc_point_to_256_bit_key(sharedECCKey)
    plaintext = decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey)
    return plaintext


if __name__ == '__main__':
    file_path = sys.argv[1]

    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        print(encoded_string)

        curve = registry.get_curve('brainpoolP256r1')

        privKey = secrets.randbelow(curve.field.n)
        pubKey = privKey * curve.g

        encryptedMsg = encrypt_ECC(curve, encoded_string, pubKey)

        enc_file = open('encrypted.dat', 'wb')
        enc_file.write(encryptedMsg[0])
        enc_file.flush()
        enc_file.close()

        ciphertext = binascii.hexlify(encryptedMsg[0])
        print("encryptedMsg")
        print(encryptedMsg)
        print("ciphertext")
        print(ciphertext)

        decryptedMsg = decrypt_ECC(encryptedMsg, privKey)
        print("decrypted msg:", decryptedMsg)

        dec_file = open('dec.jpg', 'wb')
        dec_file.write(base64.b64decode(decryptedMsg))
        dec_file.flush()
        dec_file.close()
