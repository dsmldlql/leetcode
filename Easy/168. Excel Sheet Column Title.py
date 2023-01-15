# v1

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while columnNumber:
            idx = columnNumber % 26 - 1
            res += alpha[idx]
            columnNumber = (columnNumber - 1) // 26
        return res[::-1]


# v2

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber:
            columnNumber -= 1
            result = chr(columnNumber % 26 + ord('A')) + result
            print(result)
            columnNumber //= 26
        return result
