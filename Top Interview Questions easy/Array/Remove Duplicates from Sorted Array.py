class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        insertIndex = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        return insertIndex



sol = Solution()
nums = [0,0,1,1,1,2,3,3,4]
print(sol.removeDuplicates(nums), nums)
