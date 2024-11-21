class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        if strx[0] == '-':
            x = (-1) * int(strx[::-1][:-1])
        else:
            x = int(strx[::-1])
        if x < (-1) * (2 ** 31) or x > (2 ** 31) + 1: return 0 
        return x


sol = Solution()
print(sol.reverse(1534236469))
