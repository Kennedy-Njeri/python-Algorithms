"""Given an array of integers, return indices of the two numbers such that they add up to a specific target"""

"""Example 
nums = [1, 3, 11, 2, 7]
target = 9
return : [3,4]
9 - 1 = 8 -> {8: 0}
9 - 3 = 6 -> {8: 0, 6: 1}
9 - 11 = -2 -> {8: 0, 6: 1, -2: 2}
9 - 2 = 7 -> {8: 0, 6: 1, -2: 2, 7: 3}

nums[i], i
index=3
in this case its [3, 4]
"""

nums = [1, 2, 11, 3, 7]
target = 9

for i in range(len(nums)):
    print (nums[i], i)


def two_sum(nums, target):
    if len(nums) <= 1:
        return False

    aux_dict = {}
    for i in range(len(nums)):
        if nums[i] in aux_dict:
            return [aux_dict[nums[i]], i]
        else:
            aux_dict[target - nums[i]] = i


print (two_sum(nums, target))


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index_map = {}
    for i in range(len(nums)):
        num = nums[i]
        pair = target - num
        if pair in index_map:
            print ([index_map[pair], i])
            #return [index_map[pair], i]
        index_map[num] = i
    return None


nums = [1, 4, 8, 3, 2, 9, 15]
target = 13
print("Nums: ", nums)
print("Target: ", target)
print("Solution: ", twoSum(nums, target))
