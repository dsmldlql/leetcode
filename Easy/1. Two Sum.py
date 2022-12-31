# v1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            if target - num in nums[idx + 1:]:
                return [idx, nums.index(target - num, idx + 1)]


# v2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for idx, val in enumerate(nums):
            difference = target - val
            if difference in dct:
                return [dct[difference], idx]
            dct[val] = idx
