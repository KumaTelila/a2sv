# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        # print(tasks)
        heap = []
        time = tasks[0][0]
        ans = []
        for start, hold, ind in tasks:
            # print(heap, time)
            if not heap and time < start:
                time = start
            if time >= start:
                heappush(heap, (hold, ind))
            else:
                while  heap and time < start:
                    end, indx  = heappop(heap)
                    time+=end
                    ans.append(indx)
                if not heap and time < start:
                    time = start
                if time >= start:
                    heappush(heap, (hold, ind))
            
        while heap:
            i, j  = heappop(heap)
            ans.append(j)
        return ans

        