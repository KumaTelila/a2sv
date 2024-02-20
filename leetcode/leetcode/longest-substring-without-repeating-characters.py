class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        window = Counter(s[:j])
        mx = -float('inf')
        while j < len(s):
            mx = max(mx, len(window))
            if s[j] in window:
                window[s[i]]-=1
                if window[s[i]] == 0:
                    del window[s[i]]
                i+=1
            else:
                window[s[j]]+=1
                j+=1
        mx = max(len(window), mx)
        return mx
            
            

        