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
