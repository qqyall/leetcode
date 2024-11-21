class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


sol = Solution()
arr = [1, 2, 3, 4]
print(sol.containsDuplicate(arr))
