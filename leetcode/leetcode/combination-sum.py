class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(ind, arr):
            if sum(arr) > target:
                return
            if sum(arr) == target:
                ans.append(arr[:])
                return
            sm = 0
            for i in range(ind, len(candidates)):
                # print(arr, ind, sum(arr))
                arr.append(candidates[i])
                if sum(arr) < target:
                    backtrack(i, arr)
                    arr.pop()
                else:
                    backtrack(i + 1, arr)
                    arr.pop()
        backtrack(0, [])
        return ans
