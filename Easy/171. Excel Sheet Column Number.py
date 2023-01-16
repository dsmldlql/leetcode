# v1

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        output = 0
        for letter in columnTitle:
            output = output * 26 + alphabet.index(letter)
        return output
