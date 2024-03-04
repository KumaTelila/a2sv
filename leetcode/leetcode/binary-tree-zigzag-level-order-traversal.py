# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count = 0
        ans = []
        dic = defaultdict(list)
        def dfs(root, path = [], count = 0):
            if root:
                dic[count].append(root.val)
                dfs(root.left, path, count+1)
                dfs(root.right, path, count+1)
        dfs(root)
        flag = False
        for i in dic:
            if flag:
                ans.append(dic[i][::-1])
            else:
                ans.append(dic[i])
            flag = not flag
        return ans


        