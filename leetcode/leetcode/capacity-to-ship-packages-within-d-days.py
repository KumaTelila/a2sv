class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = low + (high - low)//2
            calculated_day = 1
            counter = 0
            for i  in range(len(weights)):
                counter+=weights[i]
                if counter > mid:
                    calculated_day+=1
                    counter = weights[i]
            # print(low, mid, high, counter, calculated_day)
            if calculated_day > days:
                low = mid + 1
            else:
                high = mid - 1
        return low
        