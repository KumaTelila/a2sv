# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        visited = set()
        queue = deque([[1, 0]])
        n = len(board)
        def row_and_col(num):
            row = (num - 1)//n
            col = (num - 1)%n
            if row%2:
                col = (n-1) - col
            return (row, col)
        board.reverse()
        visited = set()
        visited.add(1)
        count = 1
        while queue:
            if n*n in visited:
                break
            ele = queue.popleft()
            (r, c) = row_and_col(ele[0])
            new = ele[0]
            curr = ele[1]
            for i in range(new+1, min(new + 6, n*n)+1):
                temp = i
                (r, c) = row_and_col(i)
                if board[r][c] != -1:
                    temp  = board[r][c]
                if temp not in visited:
                    visited.add(temp)
                    queue.append([temp, curr+1])
        for i, j in queue:
            if i == n*n:
                return j
        return -1
            



        