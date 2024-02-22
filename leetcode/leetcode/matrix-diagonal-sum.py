class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        first = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    first+=mat[i][j]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(mat)%2!= 0 and i == len(mat)//2:
                    continue
                if i + j == len(mat[0])-1:
                    first+=mat[i][j]
        return first
        