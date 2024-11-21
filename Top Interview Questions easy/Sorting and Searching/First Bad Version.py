# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        res = [n]
        def helper(ver, left, right):
            if left > right:
                return None
            tmp = int(ver / 2)
            if isBadVersion(tmp):
                if tmp  < res[0]:
                     res[0] = tmp
                return helper(tmp, left, tmp)
            else:
                return helper(tmp, tmp, right)

        helper(n, 0, n)
        print(res[0])

sol = Solution():
    
