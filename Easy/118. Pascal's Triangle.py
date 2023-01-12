# v1

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return None
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        rows = [[1], [1, 1]]
        for r in range(1, numRows - 1):
            lst = [1] + [rows[-1][i] + rows[-1][i + 1] for i in range(r)] + [1]
            rows.append(lst)
        return rows
