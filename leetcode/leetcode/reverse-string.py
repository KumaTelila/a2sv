class Solution:
    count = 0
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = self.count, len(s) - self.count -1
        if i>= j:
            return None
        s[i], s[j] = s[j] , s[i]
        self.count+=1
        self.reverseString(s)
        