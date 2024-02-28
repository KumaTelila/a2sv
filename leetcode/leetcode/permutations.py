class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(path):
            # base case
            chk = len(set(path))
            # print(path, chk)
            if chk == n:
                ans.append(path[:])
            if len(path) >= n:
                return
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(path)
                path.pop()
        backtrack([])
        return ans



                
        