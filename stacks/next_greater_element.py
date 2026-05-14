arr = [4, 5, 2, 10]
ans = []
# we want to find the next greater element for every element in the array
# if there is no next greater element, then it should be -1
# desired -> ans = [5, 10, 10, -1]

def next_greater(arr):
    n = len(arr)
    stack = []
    ans = [-1] * n

    # Traverse from right to left
    for i in range(n - 1, -1, -1):

        # Remove smaller or equal elements
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack is not empty, top is next greater
        if stack:
            ans[i] = stack[-1]

        # Push current element
        stack.append(arr[i])

    return ans

print(next_greater(arr))