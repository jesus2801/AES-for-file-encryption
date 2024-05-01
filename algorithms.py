from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
import bcrypt
import io

import os
from dotenv import load_dotenv
load_dotenv()

BUFFER_SIZE = -1


def generateKey(password: str, salt: str, AES_size: int):
  return bcrypt.kdf(
      password=password.encode(),
      salt=salt.encode(),
      desired_key_bytes=int(AES_size / 8), rounds=100)


def cipher(args, key):
  with io.open(args['output'] + '.enc', mode='w', buffering=BUFFER_SIZE) as write_stream:
    with io.open(args['input'], mode='r', buffering=BUFFER_SIZE) as read_stream:
      for line in read_stream:
        cipher = AES.new(key, AES.MODE_CBC, iv=os.getenv('IV').encode())
        ct_bytes = cipher.encrypt(pad(line.encode(), AES.block_size))
        encrypted_data = b64encode(ct_bytes).decode('utf-8')
        write_stream.write(encrypted_data + '\n')


def decipher(args, key):
  with io.open(args['output'] + '.dec', mode='w', buffering=BUFFER_SIZE) as write_stream:
    with io.open(args['input'], mode='r', buffering=BUFFER_SIZE) as read_stream:
      for line in read_stream:
        line = line[:len(line) - 1]
        cipher = AES.new(key, AES.MODE_CBC, iv=os.getenv('IV').encode())
        ct = b64decode(line)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        write_stream.write(pt.decode())
