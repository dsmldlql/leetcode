# v1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        target_idx = 0
        for idx, num in enumerate(nums[1:]):
            # nums[idx + 1] = '_'
            if num != nums[target_idx]:
                target_idx += 1
                nums[target_idx] = num
            if num == 100:
                break
        return target_idx + 1


# v2

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_ = {val for val in nums}
        nums[:] = sorted(list(set_))
