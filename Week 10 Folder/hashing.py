import hashlib

print(hashlib.sha256(b"pasword123").hexdigest())
print(hashlib.sha256(b"password123").hexdigest())

pt = "asdf1234"
bt = b"asdf1234"
ct = hashlib.sha256(bt).hexdigest() #TypeError: Strings must be encoded before hashing (using pt)
#algorithm needs a parameter which is binary. Plain text to binary. There is also an encode function to do this
print(ct)
print(len(ct)) #64 digits

x = b"password123"
P = "password123".encode()

print(P)
print(list(P))

y = b"something67823"

print(list(x))
print(list(y))










import bcrypt
password = b"password123"

#gen random value
salt = bcrypt.gensalt()

#create hash value
hsh = bcrypt.hashpw(password, salt)

print(hsh)

#generating two different salts
salt1 = bcrypt.gensalt()
salt2 = bcrypt.gensalt()

#hash the same password twice
hash1 = bcrypt.hashpw(password, salt1)
hash2 = bcrypt.hashpw(password, salt2)

print("Anna:", hash1)
print("Ben:", hash2)

print("Are the hashes equal? ->", hash1 == hash2)