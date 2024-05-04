# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        store = 0
        def backtrack(index, path = []):
            nonlocal store
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if not store & (1 << i):
                    store ^= (1 << i) 
                    path.append(nums[i])
                    backtrack(i, path)
                    store ^= (1 << i)
                    path.pop()
        backtrack(0)
        return ans
        