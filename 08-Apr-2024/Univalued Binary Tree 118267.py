# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        ans = root.val
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                ele = queue.popleft()
                if ele.val != ans:
                    return False
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
        return True