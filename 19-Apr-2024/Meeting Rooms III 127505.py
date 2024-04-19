# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        unused_rooms = [i for i in range(n)]
        used_rooms = []
        heapify(unused_rooms)
        ans = defaultdict(int)
        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                time, room = heappop(used_rooms)
                heappush(unused_rooms, room)
            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, [end,room])
            else:
                time, room = heappop(used_rooms)
                heappush(used_rooms, [time + end - start, room])
            ans[room]+=1
        sol = -float('inf')
        res = -1
        for k, v in ans.items():
            if v > sol:
                sol = v
                res = k
        return res
        