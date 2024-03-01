class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)

        min_unfairness = float('inf')
        combination = [0]*k
        # define backtracking fumction
        def backtrack(index):
            nonlocal min_unfairness
            # base cases
            if index >= len(cookies):
                min_unfairness = min(min_unfairness, max(combination))
                return
            # recurence relation 
            for i in range(k):
                # take
                combination[i]+=cookies[index]
                # backtrack
                backtrack(index+1)
                # not take
                combination[i]-=cookies[index]
        backtrack(0)

        return min_unfairness
        