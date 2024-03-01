class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        n = len(digits)
        ans = []

        def backtrack(index, path):
            if path and len(path) == n:
                ans.append("".join(path[:]))
            if index >= n:
                return
            for i in dic[int(digits[index])]:
                path.append(i)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return ans
