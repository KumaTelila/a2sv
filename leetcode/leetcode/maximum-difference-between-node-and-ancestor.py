# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, _min, _max):
            # print(_min, _max)
            nonlocal ans
            if not root:
                return 
            _min = min(root.val, _min)
            _max = max(root.val, _max)
            ans = max(abs(_max - _min), ans)
            dfs(root.left, _min, _max)
            dfs(root.right, _min, _max)
        dfs(root, float('inf'), -float('inf'))
        return ans
            
        