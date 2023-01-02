# v1

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx_to_remove = 0
        for idx, value in enumerate(nums):
            if val != value:
                nums[idx_to_remove] = value
                idx_to_remove += 1
        return idx_to_remove
