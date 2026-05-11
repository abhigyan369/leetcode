# LC 1. Two Sum

## Problem
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

## Link
https://leetcode.com/problems/two-sum/

---

# Pattern
HashMap / Hashing

---

# Key Observation

For every number x,
we need another number:

target - x

Instead of searching again,
store previously seen numbers in a hashmap.

---

# Brute Force

Check every pair.

Time Complexity: O(n²)

---

# Optimal Approach

Use hashmap:

- Traverse array
- Compute complement = target - nums[i]
- If complement already exists:
    answer found
- Otherwise store current number

Time Complexity: O(n)
Space Complexity: O(n)

---

# Pattern Trigger

Use hashmap when:
- Need fast lookup
- Need complement/value existence
- "Find pair with target"

Keywords:
- pair sum
- complement
- target sum

---

# Mistakes I Made

- Forgot hashmap stores value -> index
- Returned values instead of indices
- Didn't check complement before insertion

---

# Code (C++)

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> mp;

        for(int i = 0; i < nums.size(); i++) {

            int complement = target - nums[i];

            if(mp.find(complement) != mp.end()) {
                return {mp[complement], i};
            }

            mp[nums[i]] = i;
        }

        return {};
    }
};
```

---

# Revision Note

Main idea:
Convert O(n²) pair search into O(n) lookup using hashmap.

This is one of the most fundamental hashing problems.