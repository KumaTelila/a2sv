class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = []
        for i in s:
            if i.isalnum():
                ans.append(i.lower())
        if len(ans) <=1:
            return True
        l, r = 0, len(ans) -1
        while l< r:
            if ans[l] != ans[r]:
                return False
            l+=1
            r-=1
        return True

        