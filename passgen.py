import hashlib
password = (input("Encripted message with md5: "))
print(hashlib.md5(str(password).encode('utf-8')).hexdigest())
