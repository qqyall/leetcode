class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(n):
            if n == 1:
                return True
            elif n % 3 == 0:
                return helper(n / 3)
            else:
                return False
        if n ==0:
            return False
        return helper(n)


    def f(self, n: int) -> bool:
        def getDigits(n):
            res = []
            while n > 0:
                res.append(n % 10)
                n //= 10 
            return res

        def helper(n):
            if n < 1:
                return False
            while n > 1:
                if sum(getDigits(n)) % 3 != 0:
                    return False
                n /= 3
            return True

        return helper(n)

sol = Solution()
print(sol.isPowerOfThree(27))
print(sol.f(27))
