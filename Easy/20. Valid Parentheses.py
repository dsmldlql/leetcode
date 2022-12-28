class Solution:
    def isValid(self, s: str) -> bool:
        dct = {'()': '', '{}': '', '[]': ''}
        if (len(s) % 2 != 0) or (len(s) == 1):
            return False
        elif len(s) == 0:
            return True
        while s:
            s_two = s[:]
            for key, value in dct.items():
                s = s.replace(key, value)
            if s_two == s:
                break
        return not s
