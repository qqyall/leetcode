class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        def getLowestWord(lst):
            minIndex = 0
            minWord = lst[0]
            for i in range(1, len(lst)):
                if len(lst[i]) < len(minWord):
                    minWord = lst[i]
                    minIndex = i
            return minWord


        res = ''
        flag = False
        for char in getLowestWord(strs):
            prefix = res + char
            for word in strs:
                if prefix != word[:len(prefix)]:
                    return res
            else:
                res += char
        return res
    
        
strs = ["flower","flow","flight"]
sol = Solution()
print(sol.longestCommonPrefix(strs))
