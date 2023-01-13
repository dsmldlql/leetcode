# v1

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1, 1]
        for idx in range(1, rowIndex):
            row = [1] + [row[i] + row[i + 1] for i in range(idx)] + [1]
        return row
