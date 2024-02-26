class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        def backtrack(ind, arr):
            for i in range(ind, len(nums)):
                arr.append(nums[i])
                if arr not in ans:
                    ans.append(arr[:])
                backtrack(i+1, arr)
                arr.pop()
        backtrack(0, [])
        return ans
        