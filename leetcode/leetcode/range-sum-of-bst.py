# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sm = 0
        def dfs(root, low, high):
            nonlocal sm
            if root:
                dfs(root.left, low, high)
                if root.val >= low and root.val <= high:
                    sm+=root.val
                dfs(root.right, low, high)
        dfs(root, low, high)
        return sm


        