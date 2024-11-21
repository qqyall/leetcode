class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = [symbol for symbol in 'IVXLCDM']
        values = [1, 5, 10, 50, 100, 500, 1000]
        translater = {symbols[i]: values[i] for i in range(len(symbols))}

        index, res = len(s) - 1, 0
        while index >= 0:
            if translater[s[index]] <= translater[s[index - 1]] or index == 0:
                res +=  translater[s[index]]
            else:
                res += (translater[s[index]] - translater[s[index - 1]])
                index -= 1
            index -=1
        return res


a = Solution()
print(Solution.romanToInt(a, 'III'))
