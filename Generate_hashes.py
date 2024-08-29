import hashlib

password = "Aztrek900@"
hash = hashlib.sha256(password.encode('utf-8'))
print(hash.hexdigest())