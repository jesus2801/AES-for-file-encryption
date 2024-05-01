# Here are the constants that appears on the help option of the executable
name = "AES for files encryption"
description = "This program encrypts files with AES"
epilog = "For more information, look at README.md"

help = {
  'type': '"cipher" if you want to encrypt and "decipher" if you want to decrypt',
  'password': 'This is the password for encryption and decryption of the file, it must be the same password',
  'salt': 'this adds more entropy to the password hash',
  'size': 'The size used for the AES algorithm. either 128, 192 or 256',
  'input': 'The file input to encrypt',
  'output': 'The file to output the encrypted file to'
}
