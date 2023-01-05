# v1

class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0) or (x == 1):
            return x
        start = 0
        for value, square in self.getNumGenerator(start, x, 200):
            if square > x:
                break
            start = value
        for val, sq in self.getNumGenerator(start, x, 1):
            if sq == x:
                return val
            elif sq > x:
                return val - 1

    def getNumGenerator(
            self, start: int, stop: int, step: int, power=2
        ) -> int:
        for value in range(start, stop + 1, step):
            yield value, value**power

# v2

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lst_x = self.splitX(x)
        root, diff = self.getFisrtNum(int(lst_x[0]))
        if x < 100:
            return root
        else:
            for num in lst_x[1:]:
                diff = int(str(diff) + num)
                doubled_root = str(root * 2)
                root_add, diff_sub = self.getNextRoot(0, diff, 1, doubled_root)
                diff -= diff_sub
                root = int(str(root) + str(root_add))
        return root

    def splitX(self, x: int) -> list:
        str_x = str(x)
        if len(str_x) % 2 == 0:
            lst_x = [str_x[i:i + 2] for i in range(0, len(str_x), 2)]
        else:
            lst_x = [str_x[i:i + 2] for i in range(1, len(str_x), 2)]
            lst_x.insert(0, str_x[0])
        return lst_x

    def getFisrtNum(self, num: int) -> int:
        for value, square in self.getNumGeneratorFirst(0, num, 1):
            if square == num:
                diff = num - square
                return value, diff
            elif square > num:
                val_minus_1 = value - 1
                diff = num - (val_minus_1) ** 2
                return val_minus_1, diff

    def getNumGeneratorFirst(
            self, start: int, stop: int, step: int, power=2
    ) -> int:
        for value in range(start, stop + 1, step):
            yield value, value ** power

    def getNextRoot(
            self, start: int, stop: int, step: int, doubled_root: str
    ) -> str:
        if stop == 0:
            return 0, 0
        for value in range(start, stop + 1, step):
            val = int(doubled_root + str(value)) * value
            if stop < val:
                return prev_value, prev_val
            prev_value = value
            prev_val = int(doubled_root + str(value)) * value
