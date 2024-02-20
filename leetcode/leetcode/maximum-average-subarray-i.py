class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j, = 0, k
        sm = sum(nums[:k])
        mx = sm/k
        # print(w1)
        while j < len(nums):
            sm-=nums[i]
            sm+=nums[j]
            mx = max(sm/k, mx)
            i+=1
            j+=1

        return mx


        