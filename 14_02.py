"""
Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following 
conditions:
a + b = M
a XOR b = N
""""



def count_ab(m, n):
    count = 0
    for a in range(0,m):
        for b in range(0, m):
            if a+b == m and a^b == n:
                count += 1
    return count
    
    """
    This is a naive solution. it is possible to reduce the number of loop using binary
    """
