class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ls = []
        mp = {}
    
        for i in range(len(points)):
            sum = 0
            for j in range(len(points[0])):
                sum  +=points[i][j]*points[i][j]
            ls.append(sum)
        j =0
        for i in points:
            mp[tuple(i)]=ls[j]
            j+=1
        ls2 = [False]*len(ls)
        ls1 = []
        s =0
        while(s<k):
            st=ls.index(min(ls))
            ls1.append(points[st])
            del ls[st]
            del points[st]
            print(st)
            s+=1
        # while(s<k):
        #     min = ls[0]
            
            
        #     index = 0
        #     for i in range(len(ls)):
        #         if(min>ls[i] and ls2[i] == False):
        #             min = ls[i]
        #             ls1.append(points[i])
        #             ls2[i] = True
        #     s+=1
        # print(ls1)
        # print(ls2)
        
        print(mp)
        print(ls)
        return ls1

        # # print(OrderedDict(sorted(mp.values()))
        # # sr = sorted(dict((k, v) for k, v in mp.items()))
        # ls1 = []
        # # for i in sorted(mp.values()):
        # #     ls1.append(list(i))
            
        # # ls1 = []
        
        
        # for i in sortedMp:
        #     ls1.append(list(i))
        # print(mp)
        # print(ls1)
        # print(ls)
        # return ls1[:k]
        # # j = 0
        # # print(ls)
        # # print(points)
        # # for i in range(len(ls)):
        # #     for j in range(len(ls)):
        # #         if(ls[i]<ls[j]):
        # #             ls[i], ls[j] = ls[j], ls[i]
        # #             points[i], points[j] = points[j], points[i]
        # # print(ls)
        # # print(points)
        # # ls1 = []
        # # for i in range(k):
        # #     ls1.append(points[i])
        # # return points


        # # for i in range(0, len(ls)):
            
        # #     mp[ls[i]] = points[j]
        # #     print(mp)
        # #     j+=1
        # # ls.sort()
        # # sorted_dict = {i: mp[i] for i in ls}
        # # ls1 = []
        # # b =0
        # # for i in ls:
        # #     if(b<k):
        # #         ls1.append(sorted_dict[i]);
        # #     b+=1

        # # # print(sorted_dict)
        # # # print(ls)
        # # print(mp)
        # # print(ls1)    
      