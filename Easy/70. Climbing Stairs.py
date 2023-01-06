# v1

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        twos = n // 2
        ones = n - twos * 2
        if not ones:
            distinct = 2
            ones = 2
        else:
            distinct = 1 + self.countComb(ones, twos)
            ones = 3
        for one in range(ones, n, 2):
            twos -= 1
            distinct += self.countComb(one, twos)
        return int(distinct)

    def countComb(self, one: int, two: int) -> int:
        numerator = self.calcFactorial(one + two)
        denominator = self.calcFactorial(one) * self.calcFactorial(two)
        return numerator / denominator

    def calcFactorial(self, num: int) -> int:
        factorial = 1
        while num > 1:
            factorial *= num
            num -= 1
        return factorial
