class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {j: i for i, j in enumerate(s)}
        glob = 0
        l = 0
        ans = []
        for i in range(len(s)):
            glob = max(glob, last[s[i]])
            if glob == i:
                ans.append(glob+1 - l)
                l = glob+1

        return ans

        