# 53. Maximum Subarray
## link -
 https://leetcode.com/problems/maximum-subarray/description/

i studied from love babbar video- https://www.youtube.com/watch?v=w4W6yya1PIc&pp=ygUSbG92ZSBiYWJiYXIga2FkYW5l

## Problem
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

## approach
we have to find that subarray with the maximum sum
# algorithm
we will take 2 variable
maxi = nums[0]
sum = 0
for loop in the arr
sum += nums[i]
maxi = max(maxi,sum)
agar sum negative ho gya toh sum =0 kardenge- sum < 0:
last me maxi return ho jayega

