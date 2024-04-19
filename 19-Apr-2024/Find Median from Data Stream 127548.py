# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.count = 0
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        self.count+=1
        if self.count%2:
            heappush(self.max_heap, -num)a
        else:
            heappush(self.min_heap, num)
        if self.min_heap and self.max_heap and self.min_heap[0] < -self.max_heap[0]:
            ele1 = heappop(self.min_heap)
            ele2 = heappop(self.max_heap)
            heappush(self.min_heap, -ele2)
            heappush(self.max_heap, -ele1)


    def findMedian(self) -> float:
        # print(self.min_heap, self.max_heap)
        if self.count%2:
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()