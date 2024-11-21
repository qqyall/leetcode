class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()


num = 10000000000000000000000000001011
sol = Solution()
print(sol.hammingWeight(num))

