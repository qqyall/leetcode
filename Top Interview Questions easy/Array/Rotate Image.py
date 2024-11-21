class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)      
        for i in range(n // 2 + n % 2):
            for j in range(i, n - i - 1):
                if i == j or  i == n - 1 - j:     
                    matrix[i][j], matrix[n - 1 - j][j], matrix[n - 1 - j][n - 1 - i], matrix[i][n - 1  - i] = matrix[n - 1 - j][j], matrix[n - 1 - j][n - 1 - i], matrix[i][n - 1 - i], matrix[i][j]
                else:
                    matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] =
                    matrix[n - j - 1][i], matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1]
        

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

sol = Solution()
sol.rotate(matrix)
[print(row) for row in matrix]
