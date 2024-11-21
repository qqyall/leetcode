class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if 0 not in nums:
            return None
        index1 = nums.index(0)
        index2 = index1
        while index2 < len(nums):
            while index2 < len(nums) and nums[index2] == 0:
                index2 += 1
            if index2 == len(nums):
                break
            nums[index1], nums[index2] = nums[index2], nums[index1]
            index1 += 1
                    

sol = Solution()
arr = [1,0,2,3,4,5,0,6,7,8,0,9,10,11,12,13]
sol.moveZeroes(arr)
print(arr)
