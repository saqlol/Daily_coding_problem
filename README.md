# Daily_coding_problem
Solutions (si possible) aux problèmes quotidiens de Daily Coding Problem  en Python ( https://www.dailycodingproblem.com/ )

### Problem 01/09

Given a list of words, find all pairs of unique indices such that the concatenation 
of the two words is a palindrome.
For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
[Solution](01_09.py)

### Problem 02/09

Given an N by M matrix, rotate it by 90 degrees clockwise.
[Solution](02_09.py)

### Problem 18/12

The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:
1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.
Given an integer N, print the Nth term of this sequence.
[Solution](18_12.py)

### Problem 20_12

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
[Solution](20_12.py)
