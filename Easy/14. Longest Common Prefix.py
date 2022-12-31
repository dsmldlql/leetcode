# v1

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs)
        if len(shortest_word) == 0:
            return ""
        elif len(strs) == 1:
            return shortest_word
        for idx, letter in enumerate(shortest_word):
            if not all([letter in word[idx] for word in strs]):
                if idx == 0:
                    return ""
                return shortest_word[:idx]
        return shortest_word[:idx + 1]


# v2

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        for idx, letter in enumerate(list(strs[0][: min(map(len, strs))])):
            for i in range(1, len(strs)):
                if letter == strs[i][idx]:
                    continue
                else:
                    return string
            string += letter
        return string


# v3

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = min(strs)
        for word in strs:
            while shortest_word:
                if not (shortest_word in word[:len(shortest_word)]):
                    shortest_word = shortest_word[:-1]
                    continue
                break
        if len(shortest_word) == 0:
            return ""
        else:
            return shortest_word
