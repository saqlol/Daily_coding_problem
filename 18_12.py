""" The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221

As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""

i = 0
N = input() 
list_digit = [int(digit) for digit in str(N)]
list_next_term = []

while i < len(list_digit):
    digit = list_digit[i]
    n_digit = 1
    j = i
    while j < len(list_digit):
        if list_digit[j] == list_digit[j+1]:
            n_digit += 1
            print(j, len(list_digit))
            if j < len(list_digit) - 1:
                print(j, len(list_digit) - 1)
                j += 1
                print(j)
            else:
                break

        else:
            break

    list_next_term.append(n_digit)
    list_next_term.append(digit)
    i += n_digit

print(''.join([str(integer) for integer in list_next_term]))



