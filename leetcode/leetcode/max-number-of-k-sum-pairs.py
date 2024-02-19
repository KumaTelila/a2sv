class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        a = sorted(nums)
        i = 0
        j = len(a)-1
        counter = 0
        while(i<j):
            sum = a[i] + a[j]
            if sum == k:
                counter+=1
                i+=1
                j-=1
            if(sum<k):
                i+=1
            if(sum>k):
                j-=1
        return counter

        