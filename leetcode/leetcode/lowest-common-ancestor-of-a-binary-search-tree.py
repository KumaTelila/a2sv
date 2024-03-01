# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if not root:
                return 
            # both are from left and right
            if (root.val > p.val  and  root.val < q.val) or (root.val < p.val and root.val > q.val):
                return root
            # if p less than or greater root and q equal to root
            if root.val == q.val and (p.val > root.val or p.val  < root.val):
                return root
            # if p greater than or less root and q equal to root
            if root.val == p.val and (q.val > root.val or q.val < root.val):
                return root
            return dfs(root.left, p, q) or dfs(root.right, p, q)
        return dfs(root, p, q)
        