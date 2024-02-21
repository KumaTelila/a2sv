class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ls = [0]*(n+1)
        for i, j, k in bookings:
            ls[i-1]+=k
            ls[j]-=k
        for i in range(1, n+1):
            ls[i]+=ls[i-1]
        return ls[:-1]

