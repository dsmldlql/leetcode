# v1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = {}
        for num in nums:
            if num in dct:
                del dct[num]
            else:
                dct[num] = 1
        return list(dct.keys())[0]
