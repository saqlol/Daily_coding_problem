'''
You are given a string consisting of the letters x and y, such as xyxxxyxyy. In addition,
you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come before all y's. 
In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.
'''

def min_flip(str_xy):

    list_str = list(str_xy)
    flipped_list_str = list_str[::-1]
    count_x = 0
    count_y = 0

    for i in range(len(str_xy)):

        if list_str[i] == 'x':
            last_x = i 
        if flipped_list_str[i] == 'y':
            last_y = len(list_str) - 1  - i

    for i in range(0, last_x, 1):
        if list_str[i] == 'y':
            count_y += 1
    for i in range(last_y, len(list_str) , 1):
        if list_str[i] == 'x':
            count_x += 1

    return min(count_x, count_y) 

test_1 = 'xyxxxyxyy'
test_2 = 'xxxyyy'
test_3 = 'yxxxyyyx'
test_4 = 'xyxyxy'

print('{} flips are needed'.format(min_flip(test_1)))
print('{} flips are needed'.format(min_flip(test_2)))
print('{} flips are needed'.format(min_flip(test_3)))
print('{} flips are needed'.format(min_flip(test_4)))
