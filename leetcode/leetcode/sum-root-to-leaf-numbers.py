# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, path = ''):
            nonlocal ans
            if not root:
                return

            if not root.left and not root.right:
                ans += int(path + str(root.val))

            dfs(root.left, path + str(root.val))
            dfs(root.right, path + str(root.val))
        ans = 0
        dfs(root)
        return ans

        