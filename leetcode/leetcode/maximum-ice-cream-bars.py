class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        pref = [costs[0]]
        for i in range(1, len(costs)):
            pref.append(pref[-1]+costs[i])
        print(pref)
        for i in range(len(pref)):
            if pref[i] > coins:
                return i
        return len(costs)