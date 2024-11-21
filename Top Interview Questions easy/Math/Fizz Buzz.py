class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        def fizz(n):
            return True if n % 3 == 0 else False
        def buzz(n):
            return True if n % 5 == 0 else False

        res = []
        i = 1
        while i < n + 1:
            match (fizz(i), buzz(i)):
                case (True, True):
                    res.append('FizzBuzz')
                case (True, False):
                    res.append('Fizz')
                case (False, True):
                    res.append('Buzz')
                case _:
                    res.append(str(i))
            i += 1
        return res


sol = Solution()
print(sol.fizzBuzz(20))
