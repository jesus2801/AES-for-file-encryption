# with this file you can generate a random IV to use in your application
from random import SystemRandom

cryptogen = SystemRandom()
iv = ""
# generates random characters in a 16-length string
for _ in range(16):
  c = chr(97 + cryptogen.randrange(25))

  if cryptogen.randrange(2):
    c = c.upper()
  else:
    c = c.lower()

  iv += c

print(iv)
