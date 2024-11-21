class Solution:
    def firstUniqChar(self, s: str) -> int:
        bad = set()
        for index1 in range(len(s)):
            for index2 in range(index1, len(s)):
                if s[index1] == s[index2]:
                    bad.add(s[index1])
                    break
            else:
                if s[index2] not in bad:
                    return index1
        else:
            return -1


s = "loveleetcode"
sol = Solution()
print(sol.firstUniqChar(s))
