class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = 0
        even = 0
        count = Counter(s)
        for i in count:
            if count[i]%2!=0:
                odd+=1
        if odd > 1:
            return len(s) - odd+1
        return len(s)
        