# Daily_coding_problem
Solutions (si possible) aux problèmes quotidiens de Daily Coding Problem  en Python ( https://www.dailycodingproblem.com/ )


### Problem 14/02
Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following 
conditions:
a + b = M
a XOR b = N
[Solution](14_02.py)

### Problem 12/02
You are given a string consisting of the letters x and y, such as xyxxxyxyy. In addition, you have an operation called flip, which changes a single x to y or vice versa.
Determine how many times you would need to apply this operation to ensure that all x's come before all y's. In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.
[Solution](12_02.py)


### Problem 10/02
In chess, the Elo rating system is used to calculate player strengths based on game results.
A simplified description of the Elo system is as follows. Every player begins at the same score. For each subsequent game, the loser transfers some points to the winner, where the amount of points transferred depends on how unlikely the win is. For example, a 1200-ranked player should gain much more points for beating a 2000-ranked player than for beating a 1300-ranked player.

[Solution](10_02.py)

### Problem 06/02
Consider the following scenario: there are N mice and N holes placed at integer points along a line. Given this, find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.
Each move consists of moving one mouse one unit to the left or right, and only one mouse can fit inside each hole.
For example, suppose the mice are positioned at [1, 4, 9, 15], and the holes are located at [10, -5, 0, 16]. In this case, the best pairing would require us to send the mouse at 1 to the hole at -5, so our function should return 6.

[Solution](6_02.py)


### Problem 03/02
Given a positive integer N, find the smallest number of steps it will take to reach 1.
There are two kinds of permitted steps:
You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

[Solution](03_02.py)


### Problem 20/12

UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.
For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for 
mapping characters are as follows:
For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.
Visually, this can be represented as follows.
<br/> 1 bit     0xxxxxxx 
<br/> 2 bit 110xxxxx 10xxxxxx
<br/> 3 bit 1110xxxx 10xxxxxx 10xxxxxx
<br/> 4 bit 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values, and returns whether it is a valid 
UTF-8 encoding.
[Solution](20_12.py)


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

### Problem 02/09

Given an N by M matrix, rotate it by 90 degrees clockwise.
[Solution](02_09.py)

### Problem 01/09

Given a list of words, find all pairs of unique indices such that the concatenation 
of the two words is a palindrome.
For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
[Solution](01_09.py)

