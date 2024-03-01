# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = Counter()
        def dfs(root):
            if root:
                freq[root.val]+=1
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        ls = sorted(freq.values(), reverse = True)
        ans = []
        for i in freq:
            if freq[i] == ls[0]:
                ans.append(i)
        return ans
        