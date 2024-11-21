class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s = sum(range(len(nums)+ 1)) - sum(nums)
        if s == 0:
            if 0 in nums:
                return len(nums)
            return 0        
        return s


sol = Solution()
nums = [1]
print(sol.missingNumber(nums))
