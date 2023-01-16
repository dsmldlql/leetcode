# v1

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n_threshold = len(nums) / 2
        lst = [num for num in set(nums) if nums.count(num) > n_threshold]
        return lst[0]


# v2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n_threshold = len(nums) / 2
        dct = {}
        for num in nums:
            if num in dct:
                dct[num] += 1
                if dct[num] > n_threshold:
                    return num
            else:
                dct[num] = 1
        return dct[num]
