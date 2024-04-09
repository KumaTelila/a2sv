# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def dfs(root):
            if root:
                if root.right:
                    graph[root.val].append(root.right.val)
                    graph[root.right.val].append(root.val)
                if root.left:
                    graph[root.val].append(root.left.val)
                    graph[root.left.val].append(root.val)
                dfs(root.right)
                dfs(root.left)
        dfs(root)
        queue = deque()
        visited = set()
        visited.add(target.val)
        queue.append(target.val)
        while queue and k > 0:
            k-=1
            for _ in range(len(queue)):
                ele = queue.popleft()
                for negh in graph[ele]:
                    if negh not in visited:
                        queue.append(negh)
                        visited.add(negh)
        return list(queue)