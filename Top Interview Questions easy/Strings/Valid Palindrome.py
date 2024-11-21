class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ''.join(filter(lambda ch: ch.isdigit() or ch.isalpha(),s.lower()))
        return r == r[::-1]
        

st = "anagram"
sol = Solution()
print(sol.isPalindrome(s = "A man, a plan, a canal: Panama"))



