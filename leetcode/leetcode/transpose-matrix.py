class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ls = []
        for i in zip(*matrix):
            ls.append(list(i))
        print(ls)
        return ls