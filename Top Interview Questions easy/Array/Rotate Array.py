class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        sub = []
        for i in range(len(nums) - k, len(nums)):
           sub.append(nums[i])
        for i in range(len(nums) - k - 1, - 1, -1):
            nums[i + k] = nums[i]
        for i in range(len(sub)):
            nums[i] = sub[i]
            
                
               

sol = Solution()
arr = [0, 1, 2, 3, 4, 5, 6]
sol.rotate(arr, 3)
print(arr)
