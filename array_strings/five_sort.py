"""
Two pointers implentation. 
If right hand pointer is 5, move left.
if left hand pointer is 5, swap pointers values
If left hand pointer is not 5, move right
"""


def five_sort(nums: list[int]) -> list:

    i = 0
    j = len(nums) - 1

    while j > i:
        if nums[j] == 5:
            j -= 1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums

    
print(five_sort([12, 5, 1, 5, 12, 7]))