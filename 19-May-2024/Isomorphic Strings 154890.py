# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for i, j in enumerate(s):
            if j in dic1:
                dic1[j].append(i)
            else:
                dic1[j]= [i]
        for i, j in enumerate(t):
            if j in dic2:
                dic2[j].append(i)
            else:
                dic2[j]= [i]
        print(dic1, dic2)
        for i in dic1.values():
            if i not in dic2.values():
                return False
        return True