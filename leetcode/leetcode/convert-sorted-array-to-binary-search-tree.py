# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # st = 0
        # en = len(nums)-1
        # mid = (st + en)//2
        # root = TreeNode(nums[mid])
        # temp = root
        # for i in range(mid-1, -1, -1):
        #     new = TreeNode(nums[i])
        #     # print(new)
        #     temp.left = new
        #     temp = new
        # temp = root
        # for i in range(mid+1, en+1):
        #     new = TreeNode(nums[i])
        #     # print(new)
        #     temp.right = new
        #     temp = new

        # cons(0, len(nums))
        def divideAndConq(st, en):
            if st == en:
                return TreeNode(nums[st])
            if st > en:
                return
            mid = (st + en)//2
            new = TreeNode(nums[mid])
            new.left = divideAndConq(st, mid-1)
            new.right = divideAndConq(mid+1, en)
            return new

        return divideAndConq(0, len(nums)-1)
        