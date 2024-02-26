class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = Counter(blocks[:k])
        i = 0
        j = k
        ans = float('inf')
        while j < len(blocks):
            ans = min(ans, window['W'])
            window[blocks[i]]-=1
            if window[blocks[i]] == 0:
                del window[blocks[i]]
            i+=1
            window[blocks[j]]+=1
            j+=1
        ans = min(ans, window['W'])
        return ans
        