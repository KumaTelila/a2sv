class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        ans = []
        for i in arr2:
            ans.extend([i]*count[i])
            del count[i]
        left = []
        for i in count:
            left.extend([i]*count[i])
        left.sort()
        ans.extend(left)
        return ans
