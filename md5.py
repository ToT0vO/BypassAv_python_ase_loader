import hashlib


string='helloworld'
hash_md5 = hashlib.md5(string.encode('utf-8')).hexdigest()

hash_16 = hash_md5[8:24]

print(hash_16)
