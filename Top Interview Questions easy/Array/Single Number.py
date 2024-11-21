class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            if num in arr:
                arr.remove(num)
            else:
                arr.append(num)
        return arr[0]
