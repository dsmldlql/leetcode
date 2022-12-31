# v1

class Solution:
    def romanToInt(self, s: str) -> int:
        summa = 0
        dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for num in s[::-1]:
            if num in ('V', 'X'):
                dct['I'] = -1
            elif num in ('L', 'C'):
                dct['X'] = -10
            elif num in ('M', 'D'):
                dct['C'] = -100
            summa += dct[num]
        return summa


# v2

class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res, prev = 0, 0
        for i in s[::-1]:
            if dct[i] >= prev:
                res += dct[i]
            else:
                res -= dct[i]
            prev = dct[i]
        return res


# v3

class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        summa = 0
        previous = 0
        for idx in range(len(s)):
            current = dct[s[idx]]
            if current > previous:
                summa += (current - 2 * previous)
            else:
                summa += current
            previous = current
        return summa
