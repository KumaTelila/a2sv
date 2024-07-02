# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        def helper(arr1, arr2):
            ans = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] > arr2[j]:
                    j+=1
                elif arr1[i] == arr2[j]:
                    ans.append(arr1[i])
                    i += 1
                    j += 1
                else:
                    i += 1
            return ans
        if len(nums1) < len(nums2):
            return helper(nums1, nums2)
       
        return helper(nums2, nums1)
        