class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ls = [[]]
        def recu(ind,n):
            for i in range(ind,len(nums)):
                n.append(nums[i])
                ls.append(n[:])
                recu(i+1,n)
                n.pop()
        recu(0,[])
        return ls

        