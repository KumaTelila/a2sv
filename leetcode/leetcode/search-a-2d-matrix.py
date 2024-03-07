class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n - 1
        print(m, n)
        while low <= high:
            mid = low + (high - low)//2
            row = mid//n
            coll = mid%n
            print(low, high, row, coll)
            if matrix[row][coll] == target:
                return True
            elif matrix[row][coll] < target:
                low = mid + 1
            else:
                high = mid - 1    
        return False
            
#         {
# (0, 0) 0
# (0, 1) 1
# (0, 2) 2
# (0, 3) 3
# (1, 0) 4
# (1, 1) 5
# (1, 2) 6
# (1, 3) 7
# (2, 0) 8
# (2, 1) 9
# (2, 2) 10
# (2, 3) 11
#         }