# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def check(s):
            if s != s[::-1]:
                return False
            return True
        def backtrack(ind, arr):
            if ind == len(s):
                ans.append(arr[:])
            # print(arr, ind)
            for i in range(ind, len(s)):
                curr = s[ind:i+1]
                if check(curr):
                    arr.append(curr)
                    backtrack(i+1, arr)
                    arr.pop()
                    
        backtrack(0, [])
        return ans
                
