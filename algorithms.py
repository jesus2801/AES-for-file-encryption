# cryptography libraries
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import bcrypt

# standard libraries
from base64 import b64encode, b64decode  # for encoding and decoding
import io
import os

# for reading env variables file's desired buffer size. see https://stackoverflow.com/questions/31869247/understanding-the-buffering-argument-of-the-io-open-method-in-python-2-7
from dotenv import load_dotenv
load_dotenv()

# this determinates the
BUFFER_SIZE = -1

"""
Bcrypt allow us to generate a Key Derivation Function (KDF). This allow us to generate a key that is more
secure than the original plain text.
You could also use a hash (But be careful the hash has (AES_size / 8) bytes)
"""
def generateKey(password: str, salt: str, AES_size: int):
  return bcrypt.kdf(
      password=password.encode(), # password as bytes
      salt=salt.encode(), # salt as bytes
      desired_key_bytes=int(AES_size / 8), # AES_size (128, 192, 256) has a relation between the key: the key must be AES_size / 8 (16, 24, 32)
      rounds=100) # number of rounds used to generate the key

"""
This function reads each line of a line-based or utf-8 file and encrypts 
that line into an output file.
""" 
def cipher(args, key):
  # opens the output file in normal write mode
  with io.open(args['output'] + '.enc', mode='w', buffering=BUFFER_SIZE) as write_stream:
    # opens the input file in normal read mode
    with io.open(args['input'], mode='r', buffering=BUFFER_SIZE) as read_stream:
      for line in read_stream: # loops through each line of the input
        # creates a new cipher object in CBC mode. Receives the Initialization
        # Vector (IV) that is stored in the .env file. IV must be in bytes
        cipher = AES.new(key, AES.MODE_CBC, iv=os.getenv('IV').encode())
        # encrypts the line
        cipher_text_bytes = cipher.encrypt(pad(line.encode(), AES.block_size))
        # encodes data in base64, then decodes to a utf-8 format
        encrypted_data = b64encode(cipher_text_bytes).decode('utf-8')
        # writes the encrypted line
        # the "\n" is a separator that is useful when decrypting, because
        # without it, the reading stream of the decryption cannot identify
        # the chunks/lines and only reads the file as a single line
        write_stream.write(encrypted_data + '\n')

"""
This function reads each encrypted line of a generated output and then 
decrypt those lines into a new decrypted output file.
"""
def decipher(args, key):
  # opens the output file in normal write mode
  with io.open(args['output'] + '.dec', mode='w', buffering=BUFFER_SIZE) as write_stream:
    # opens the input file in normal read mode
    with io.open(args['input'], mode='r', buffering=BUFFER_SIZE) as read_stream:
      for line in read_stream: # loops through each line of the output
        # extracts the "\n" from the line
        line = line[:len(line) - 1]
        # creates a new cipher object in CBC mode. Receives the Initialization
        # Vector (IV) that is stored in the .env file. IV must be in bytes
        cipher = AES.new(key, AES.MODE_CBC, iv=os.getenv('IV').encode())
        # decodes the line
        cipher_text = b64decode(line)
        # decrypt the cipher and unpads it from its original form
        plain_text = unpad(cipher.decrypt(cipher_text), AES.block_size)
        # writes the decrypted line
        write_stream.write(plain_text.decode())
