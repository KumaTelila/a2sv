class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic =  defaultdict(int)
        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                a = stack.pop()
                dic[a] = i
            stack.append(i)
        ans = [-1]*len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in dic:
                ans[i] = dic[nums1[i]]
        return ans
            

        