class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n =  len(board)
        m =  len(board[0])
        flag = False
        st=set()
        def backtrack(i, j, ind):
            nonlocal flag,st
            if ind >= len(word):
                flag = True
                return 
            if i >= n or j >= m or i < 0 or j < 0:
                return 
            if (i, j) in st:
                return
            if board[i][j] != word[ind]:
                return 
            valid = {(i+1, j), (i, j+1), (i-1, j), (i, j-1)}
            st.add((i,j))
            for k in valid:
                backtrack(k[0], k[1], ind+1)
            st.remove((i, j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    backtrack(i, j, 0)
        return flag