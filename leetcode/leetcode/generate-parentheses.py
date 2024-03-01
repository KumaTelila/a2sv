class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        ls = ['(',  ')']
        def backtrack(index, path = [], op = 0):
            # print(path, index)
            if op > n or len(path) - op > op:
                return 
            if len(path) == 2*n:
                if op == len(path) - op:
                    ans.append(''.join(path[:]))
                return
            for i in range(2):
                if ls[i] == '(':
                    op+=1
                path.append(ls[i])
                backtrack(i+1, path, op)
                path.pop()
                if ls[i] == '(':
                    op-=1
        backtrack(0)
        
        return ans

                





        