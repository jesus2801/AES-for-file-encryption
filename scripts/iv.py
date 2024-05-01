from Crypto import Random

iv = Random.new().read(16)
print(iv)