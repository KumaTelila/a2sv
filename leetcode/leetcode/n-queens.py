class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        seen_row = set()
        seen_column = set()
        seen_down = set()
        seen_up = set()
        def checker(curr):
            r, c = curr
            if r in seen_row or c in seen_column or (r - c) in seen_down or (r + c) in seen_up:
                return False
            return True
        def backtrack(row, coll, path = []):
            # if not checker((row, coll)):
            #     return
            if len(path) == n:
                val = sorted(path[:])
                if val not in ans:
                    ans.append(val)
                return
            if coll >= n:
                return
            for i in range(n):
                if  checker((i, coll)):
                    seen_row.add(i)
                    seen_column.add(coll)
                    seen_down.add(i - coll)
                    seen_up.add(i+coll)
                    path.append((i, coll))
                    backtrack(i, coll + 1, path)
                    r, c = path.pop()
                    seen_row.remove(i)
                    seen_column.remove(coll)
                    seen_down.remove(i - coll)
                    seen_up.remove(i + coll)
        for i in range(n):
            backtrack(0, i)
        res = []
        for i in ans:
            x = []
            for j in i:
                s = '.'*n
                new = s[:j[1]]
                s = new+ 'Q' + s[j[1]+1:]
                x.append(s)               
            res.append(x)
        return res


        