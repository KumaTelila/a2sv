# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        i = 0
        freq = defaultdict(int)
        for i in words:
            freq[i] += 1
        for word in freq:
            fr = freq[word]
            heappush(heap, (-fr, word))
        ans = []
        while k > 0:
            ele = heappop(heap)
            ans.append(ele[1])
            k-=1
        return ans