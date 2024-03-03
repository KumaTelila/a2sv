class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float('inf')
        window = Counter(cards[:1])
        i = 0
        j = 1
        while j < len(cards):
            # print(window)
            if len(window) < j - i:
                ans = min(j - i, ans)
                window[cards[i]]-=1
                if window[cards[i]] == 0:
                    del window[cards[i]]
                i+=1
            else:
                window[cards[j]]+=1
                j+=1
        while len(window) < j - i:
            ans = min(j - i, ans)
            window[cards[i]]-=1
            if window[cards[i]] == 0:
                del window[cards[i]]
            i+=1
        if i == 0 and j == len(cards):
            return -1
        return ans
        