# v1

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        if digits[-1] != 10:
            return digits
        digits = digits[::-1]
        for idx, value in enumerate(digits):
            print(idx, value)
            if value == 10:
                digits[idx] = 0
                if len(digits) == idx + 1:
                    digits.append(1)
                else:
                    digits[idx + 1] = digits[idx + 1] + 1
            else:
                return digits[::-1]


# v3

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        if digits[-1] != 10:
            return digits
        for idx in range(len(digits) - 1, -1, -1):
            print(idx, digits[idx])
            if digits[idx] == 10:
                digits[idx] = 0
                print(digits)
                if idx == 0:
                    digits.insert(0, 1)
                    print(digits)
                else:
                    digits[idx - 1] = digits[idx - 1] + 1
                    if digits[idx - 1] != 10:
                        return digits
        return digits
