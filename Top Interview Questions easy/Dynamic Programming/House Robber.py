class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 0: 
            return 0
        
        robNextPlusOne = 0
        robNext = nums[n - 1]

        for i in range(n - 2, -1, -1):
            current = max(robNext, robNextPlusOne + nums[i])
            robNextPlusOne = robNext
            robNext = current
        
        return robNext 


class Solution1:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) < 3:
            return max(nums)

        nums[1] = max(nums[:2])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i] + nums[i-2])
        return nums[-1]


sol = Solution1()
arr = [2,7,9,3,1]
print(sol.rob(arr))
