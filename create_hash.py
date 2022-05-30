import hashlib

#firefox
print(hashlib.md5("1048576 0 16 12582912 25165824 1048576 30000 16 8".encode('utf-8')).hexdigest())

#chrome
print(hashlib.md5("6291456 65536 103 6291456 15728640 6291456 30000 100".encode('utf-8')).hexdigest())

