# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(mat)
        m = len(mat[0])
        def inbound(row, col):
            return (0 <= row < len(mat) and 0 <= col < len(mat[0]))
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = n*m
        while queue:
            row, col = queue.popleft()
            for i, j in directions:
                x = row  + i
                y = col + j
                if inbound(x, y) and mat[x][y] > mat[row][col]:
                    queue.append((x, y))
                    mat[x][y] = mat[row][col] + 1
        return mat





        