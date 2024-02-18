class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            for j in range(len(i)):
                if i[j] == 0:
                    i[j] = 1
                else:
                    i[j] = 0
        for i in image:
            j = 0
            k = len(i)-1
            while j<=k:
                i[j], i[k] = i[k], i[j]
                j+=1
                k-=1
        return image
        