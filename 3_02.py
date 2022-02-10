'''
Given a positive integer N, find the smallest number of steps it will take to reach 1.
There are two kinds of permitted steps:
You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the following route: 
100 -> 10 -> 9 -> 3 -> 2 -> 1.
'''

import numpy as np
def largest_factor(num):
    a = 1
    b = num
    factor1 = 1
    factor2 = 1
    while a <= round(np.sqrt(num),0):
        if num % a == 0:
            factor1 = a
            factor2 = num // a 
        a += 1

    return max(factor1, factor2)


num = int(input())
path = [num]

if num == 1:
    result = 0
if num < 1:
    result = "imposssible"
else:
    '''
    On compare à chaque étape si le nombre est premier (son plus grand diviseur est lui-même) dans ce cas on 
    soustrait 1 sinon on stock son plus grand diviseur.
    '''
    while num != 1:
        lf = largest_factor(num)
        if num == lf:
            num -= 1
        else:
            num = lf

        path.append(num)

print("le chemin est {}, le nombre d'étape est {}".format(path, len(path)))
