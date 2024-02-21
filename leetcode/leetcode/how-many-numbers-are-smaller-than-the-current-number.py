class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ls = []
        for i in nums:
            a=0
            for j in nums:
                if(i>j):
                    a+=1
            ls.append(a)
        return ls