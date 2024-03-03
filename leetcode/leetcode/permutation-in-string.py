class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        n = len(s2)
        k = len(s1)
        window = Counter(s2[:k])
        i = 0
        j = k
        while j < n:
            if window == s1_freq:
                return True
            window[s2[i]]-=1
            if window[s2[i]] == 0:
                del window[s2[i]]
            window[s2[j]]+=1
            i+=1
            j+=1
        if window == s1_freq:
            return True
        return False

        