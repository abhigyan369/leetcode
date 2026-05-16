# find max num in array

arr = [54,2,3,4,56,6]
maxi = arr[0]
for num in arr:
    if num > maxi:
        maxi = num

#print(maxi)

'''
Now we will solve it using recursion
base case - sabse chhota input
yt link - https://www.youtube.com/watch?v=Qh_U6NYf99o&list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2&index=71
'''

def maximumNum(arr,n):
    if n == 1:
        return arr[0]
    temp = arr[n-1]
    return max(maximumNum(arr,n-1),temp)
print("ans" , maximumNum(arr,len(arr)))