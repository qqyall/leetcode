class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        cur_row = [1]
        triangle.append(cur_row)
        for row in range(1, numRows):
            next_row = [1]
            for i in range(len(cur_row)- 1):
                next_row.append(cur_row[i] + cur_row[i + 1])
            next_row.append(1)
            triangle.append(next_row)
            cur_row = next_row.copy()
        return triangle

sol = Solution()
print(sol.generate(100))
