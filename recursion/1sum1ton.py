'''we need to find the sum from 1 to n, we already we can use loop to find the sum
now we will use recursion to find the sum where we check base case i.e if n ==1 return 
recursive call should sum + fn(n-1)
'''

def sum1ton(n):
    ## base case
    if n == 1:
        return 1
    ## recurive call
    return n + sum1ton(n-1)


print(sum1ton(5))