from random import sample


class Solution:
    def __init__(self, nums: list[int]):
        self.data = nums.copy() 


    def reset(self) -> list[int]:
        return self.data

        
    def shuffle(self) -> list[int]:
        return sample(self.data, k=len(self.data))


# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()

print(param_1)
print(param_2)
