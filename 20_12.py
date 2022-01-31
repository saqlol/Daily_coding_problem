''' 
UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for 
mapping characters are as follows:

For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.

Visually, this can be represented as follows.

 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Write a program that takes in an array of integers representing byte values, and returns whether it is a valid 
UTF-8 encoding.
'''

bit_integer = input()
result = "invalid"
list_bit = [int(digit) for digit in list(str(bit_integer))]
test = 0

if len(list_bit) % 8 == 0:
    if len(list_bit) == 8 and list_bit[0] == 0:
        result = "valid"
    else:
        number_bit = len(list_bit) // 8
        test = 1
        i = 0
        while i < number_bit:
            if list_bit[i] == 0:
                test = 0
                break
            i += 1
        if test == 1 and list_bit[number_bit] == 0:
            j = 1
            while j < number_bit:
                if list_bit[j*8] != 1 and list_bit[j*8+1] != 0:
                    test = 0
                j += 1

if test == 1:
    result = "valid"

print(result)

