class Solution:
    def intersection(self, ls1, ls2):
        visited = [0]*len(ls2)
        ls = []
        for i in ls1:
            if i in ls2:
                ind = ls2.index(i)
                ls.append(i)
                ls2.pop(ind)
        return ls
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <= len(nums2):
            return self.intersection(nums1, nums2)
        else:
            return self.intersection(nums2, nums1)
        