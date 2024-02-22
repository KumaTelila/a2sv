class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        _max = max(arr)
        ind = arr.index(_max)
        if ind == len(arr) - 1 or ind == 0:
            return False
        for i in range(1, ind+1):
            if arr[i] <= arr[i-1]:
                return False
        for i in range(ind+1, len(arr)):
            if arr[i] >= arr[i-1]:
                return False
        return True


        