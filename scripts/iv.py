# with this file you can generate a random IV to use in your application
from Crypto import Random

iv = Random.new().read(16)
print(iv)
