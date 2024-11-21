class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    nums2.remove(num2)
                    res.append(num2)
                    break
        return res


sol = Solution()

n1 = [4,9,5]
n2 = [9,4,9,8,4]
print(sol.intersect(n1, n2))
                    
