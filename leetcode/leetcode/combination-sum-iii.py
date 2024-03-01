class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(index, path=[], sm=0):
            # base case
            if len(path) == k and sm == n:
                ans.append(path[:])
                return
            if sm > n:
                return
            if len(path) >= k:
                return
            for i in range(index, min(n + 1, 10)):
                if sm <= n:
                    path.append(i)
                    sm += i
                    backtrack(i + 1, path, sm)
                    path.pop()
                    sm -= i

        backtrack(1)
        # print(ans)
        return ans
