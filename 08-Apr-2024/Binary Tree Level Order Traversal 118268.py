# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ans = []
        if root:
            ans.append([root.val])
            queue.append(root)
        while queue:
            curr = []
            for _ in range(len(queue)):
                ele = queue.popleft()
                if ele.left:
                    queue.append(ele.left)
                    curr.append(ele.left.val)
                if ele.right:
                    queue.append(ele.right)
                    curr.append(ele.right.val)
            ans.append(curr)        
        return ans[:-1]