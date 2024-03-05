# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        dic = defaultdict(list)

        def dfs(root, hor = 0, vert = 0):
            if root:
                dic[vert].append((hor, root.val))
                dfs(root.left, hor + 1, vert - 1)
                dfs(root.right, hor + 1, vert  + 1)
        dfs(root)
        srt = sorted([[i,sorted(dic[i],key = lambda x: (x[0],x[1]))] for i in dic])
        ans  = []
        for key in srt:
            out = []
            for value in key[1]:
                out.append(value[1])
            ans.append(out)
        return ans

        