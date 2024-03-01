class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        freq = Counter(candidates)
        unique = []
        for i in candidates:
            if i not in unique:
                unique.append(i)
        unique.sort()
        def backtrack(index, path = [], sm = 0):
            # base case
            if sm > target:
                return
            if sm == target:
                ans.append(path[:])
                return

            # recurance relation
            for i in range(index, len(unique)):
                if freq[unique[i]] != 0:
                    path.append(unique[i])
                    freq[unique[i]]-=1
                    sm+=unique[i]
                    backtrack(i, path, sm)
                    path.pop()
                    freq[unique[i]]+=1
                    sm-=unique[i]
        ans = []
        backtrack(0)
        return ans

        