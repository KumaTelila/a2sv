# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque([root])
        count = 0
        while queue:
            l = len(queue)
            count += 1
            for _ in range(l):
                ele = queue.popleft()
                for i in ele.children:
                    if i:
                        queue.append(i)
        return count
        