# v1

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        for idx, value in enumerate(s[::-1]):
            print(idx, value, counter)
            if value != ' ':
                counter += 1
                continue
            elif (counter != 0) and (value == ' '):
                return counter
        return counter


# v2

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        for idx, value in enumerate(s):
            if value != ' ':
                i = idx
                break
        for idx, value in enumerate(s[idx:]):
            if value == ' ':
                return idx
        return idx + 1
