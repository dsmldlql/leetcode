# v1

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


# v2

class Solution:
    def isValid(self, s: str) -> bool:
        dct = {'(': ')', '{': '}', '[': ']'}
        lst = []
        for bracket in s:
            if bracket in dct:
                lst.append(bracket)
            else:
                if len(lst) == 0:
                    return False
                else:
                    last_bracket_in_list = lst.pop()
                    if dct[last_bracket_in_list] != bracket:
                        return False
        if len(lst) != 0:
            return False
        else:
            return True