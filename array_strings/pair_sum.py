"""
1. Two Sum
Difficulty: Easy
https://leetcode.com/problems/two-sum/
---

Algorithm:
    1. Create an empty hashmap.
    2. Loop over enumerated array of numbers,
        a. In each loop we calculate the difference between target and curr num
    3. If the difference value is already in the hash map
        a. Return the index of the already added number and the new one.
        b. If not, add to hash map, where the number is the key and the
        value is the index.
"""

def pair_sum(numbers, target):
    prev_map = {}

    for i, num in enumerate(numbers):
        diff = target - num
        if target in prev_map:
            return (prev_map[diff], i)
        
    return


def pair_sum(numbers, target_sum):
    prev_map = {}

    for i, num in enumerate(numbers):

        diff = target_sum - num
        if diff in prev_map:
            return (i, prev_map[diff])

        prev_map[num] = i

    return