# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        comb = []
        # def backtrack(ind, path):
        #     if len(path) == len(s):
        #         comb.append(path[:])
        #         return
        #     print(path)
        #     for i in range(len(s)):
        #         path.append(s[i])
        #         backtrack(i+1, path)
        #         ele  = path.pop()
        #         if ele.isalpha():
        #             if ele.islower():
        #                 s[i] = ele.upper()
        #             else:
        #                 s[i] = ele.lower()
        # backtrack(0, [])
        # ans = []
        # print(comb)
        # for i in comb:
        #     flag = True
        #     for j in range(len(i)):
        #         if ord(i[j]) & 31 != ord(s[j]) & 31:
        #             flag = False
        #             break
        #     if flag:
        #         ans.append(i)
        def backtrack(sub, i):
            if len(sub) == len(s):
                ans.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)
                
        ans = []
        backtrack("", 0)
        return ans
        