# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition

# Return the answer with the smaller index first

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}
        for i, n in enumerate(nums):
            match = target - n
            if match in nums_dict:
                return [nums_dict[match],i]
            nums_dict[n] = i