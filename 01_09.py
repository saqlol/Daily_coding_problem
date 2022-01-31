"""
Given a list of words, find all pairs of unique indices such that the concatenation 
of the two words is a palindrome.
For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""

test = ['code', 'edoc', 'da', 'd']
palindrome_index = []
for i in range(len(test)):
    for j in range(len(test)):
        if i !=j:
            concat = test[i] + test[j]
            if len(concat) % 2 == 0:
                part1 = concat[0:(len(concat)//2)]
                part2 = concat[(len(concat)//2):]
                if part1 == part2[::-1]:
                    palindrome_index.append([i,j])
            else:
                part1 =  concat[0:(len(concat)//2)+1]
                part2 = concat[len(concat)//2:]
                if part1 == part2[::-1]:
                    palindrome_index.append([i,j])

print(palindrome_index)
