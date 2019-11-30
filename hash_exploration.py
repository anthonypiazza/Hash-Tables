import bcrypt
import hashlib

first = "hello"

second = "world"

# Salt = random value used to encrypt; pseudo random seed value
salt = bcrypt.gensalt()

print(bcrypt.hashpw(b"first", salt))
print(bcrypt.hashpw(b"world", salt))

hash = bcrypt.hashpw(b"first", salt)

# Hashtable
# Array that uses indeices based off of hash method
# Provides storage thats easier to access than orther methods by using a hash function to separate values

# Creating hashes and table takes time, but once completed searching etc is constant
