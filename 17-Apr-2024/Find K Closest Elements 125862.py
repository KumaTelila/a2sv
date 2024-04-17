# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        i = 0
        while i < len(arr):
            if i >= k:
                first = abs(heap[0] - x)
                second = abs(arr[i] - x)
                if second < first:
                    heapreplace(heap, arr[i])
            else:
                heappush(heap, arr[i])
            i+=1
        ans = []
        while heap:
            ele = heappop(heap)
            ans.append(ele)
        return ans
        