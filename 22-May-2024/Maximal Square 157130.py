# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        directions = [(-1, -1), (-1, 0), (0, -1)]
        for i in range(1, n):
            for j in range(1, m):
                ls = []
                for x, y in directions:
                    ls.append(int(matrix[i+x][j+y]))
                if matrix[i][j] != '0':
                    matrix[i][j] = str(int(matrix[i][j]) + min(ls))
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, int(matrix[i][j]))
        return ans**2
        
        