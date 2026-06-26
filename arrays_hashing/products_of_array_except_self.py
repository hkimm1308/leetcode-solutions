class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        for i, n in enumerate(nums):
            x = 1
            if len(nums) == 0:
                return []
            for pre in range(0, i):
                x *= nums[pre]
            for suf in range(i + 1, len(nums)):
                x *= nums[suf]
            res.append(x)
        return res