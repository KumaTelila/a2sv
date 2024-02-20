class Solution:
    def isEqual(self, cs, cp):
        for i in cp:
            if i not in cs or cp[i] != cs[i]:
                return False
        
        return True
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        cp = dict(Counter(p))
        cs = defaultdict(int)
        for i in s[:len(p)]:
            cs[i] += 1
        ans = []
        i, j = 0, len(p) -1
        if self.isEqual(cs, cp):
            ans.append(i)
        while j < len(s)-1:
            i+=1
            j+=1
            cs[s[i-1]] -= 1
            cs[s[j]] += 1
            if cs[s[i-1]] == 0:
                cs.pop(s[i-1])
            if self.isEqual(cp, cs) :
                ans.append(i)       
        return ans