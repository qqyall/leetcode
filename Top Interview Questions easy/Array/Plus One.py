class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        flag  = True
        i = len(digits)-1
        while flag and i >= 0:
            digits[i] = (digits[i] + 1) % 10
            if digits[i] != 0:
                flag = False
            i -= 1

        if digits[0] == 0:
            digits.reverse()
            digits.append(1)
            digits.reverse()
        return digits


sol = Solution()
arr = [9, 9, 9, 9]
print(sol.plusOne(arr))

