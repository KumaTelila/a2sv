class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        _max = -1
        j =len(processorTime)-1
        for i in range(len(tasks)):
            if i!=0 and i%4 ==0:
                j-=1
            _max = max(_max, processorTime[j] + tasks[i])
            
        return _max

        