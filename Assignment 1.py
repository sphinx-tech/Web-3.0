# Hash a single string with hashlib.sha256
from ast import For
import hashlib
from inspect import trace
from random import seed
import time

seed(100)

def padded_hex(i, l):
    given_int = i
    given_len = l

    hex_result = hex(given_int)[2:] # remove '0x' from beginning of str
    num_hex_chars = len(hex_result)
    extra_zeros = '0' * (given_len - num_hex_chars) # may not get used..

    return ('0x' + hex_result if num_hex_chars == given_len else
            '?' * given_len if num_hex_chars > given_len else
            '0x' + extra_zeros + hex_result if num_hex_chars < given_len else
            None)

#a_string = 'this string holds important and private information'

target_string = "0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"

hex_target = padded_hex(int(target_string, 16), 64)

inp_string = input("Enter Block string \n")

nounce = 0

hash_block = inp_string + str(nounce)

# print("Block Header", inp_string)
# print("Hash Block", hash_block)

# target_string = "0x0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
# hex_targ = hex(int(target_string, 16))
# # hex_target = "{:07x}".format(int(target_string, 16))
# hex_target = padded_hex(42, 4)

# print("Hexadecimal Target", hex_target)

hashed_string = hashlib.sha256(hash_block.encode('utf-8')).hexdigest()
hashed_num = padded_hex(int(hex(int(hashed_string, 16)), 16),64)
# print("Hexadecimal Number", hashed_num)

# for i in range(1, 10):
#     nounce = nounce + 1
#     hash_block = inp_string + str(nounce)
#     #print(hash_block)
#     hashed_string = hashlib.sha256(hash_block.encode('utf-8')).hexdigest()
#     hashed_num = hex(int(hashed_string, 16))
#     print(hashed_num)

start = time.time()

while(hashed_num > hex_target) :
    nounce = nounce + 1
    hash_block = inp_string + str(nounce)
    # print(hash_block)
    hashed_string = hashlib.sha256(hash_block.encode('utf-8')).hexdigest()
    hashed_num = padded_hex(int(hex(int(hashed_string, 16)), 16),64)


# print("************************")
# print("Hexadecimal Number", hashed_num)
# print("########################")
# print(hex_target)
# print(hashed_num < hex_target)
print("Nounce",nounce)
# while()
# hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
# print(hashed_string)

end = time.time()
print("Total Time Elapsed in seconds", end-start)