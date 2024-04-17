# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        _max = max(freq.values())
        buckets = [ set() for _ in range(_max)]
        for i in freq.keys():
            buckets[freq[i] - 1].add(i)
        buckets = buckets[::-1]
        ans = []
        for i in buckets:
            if k > 0:
                ans.extend(list(i))
                k-=len(i)
            else:
                break
        return ans
        