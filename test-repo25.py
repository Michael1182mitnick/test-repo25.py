# find the bug in the code
# make the numbers vertical
"""
def printTo(n):
    # Takes in a number n and prints
    # from 0 all the way up until n
    for i in range(1, n):
        print(n)

# Example 
# printTo(5)
# => 0
# => 1
# => 2
# => 3
# => 4
# => 5
"""
def printTo(n):
    # Takes in a number n and prints
    # from 0 all the way up until n 
    for i in range(0, n + 1):
        print(i, end=" ")

printTo(5)