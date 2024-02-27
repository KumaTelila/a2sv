class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(first_num, arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            for num in range(first_num, n+1):
                arr.append(num)
                backtrack(num+1,  arr)
                arr.pop()
            
        backtrack(1, [])
        return ans

                    
                
                

        