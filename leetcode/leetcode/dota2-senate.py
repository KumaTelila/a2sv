class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        killed_d = 0
        killed_r = 0
        queue = deque()

        for i in senate:
            queue.append(i)

        freq = Counter(senate)
        while  True:
            if freq["D"] == 0:
                return "Radiant"
            if freq["R"] == 0:
                return "Dire"
            
            if queue[0] == 'R' :
                if killed_r == 0:
                    a = queue.popleft()
                    queue.append(a)
                    killed_d += 1
                else:
                    queue.popleft()
                    killed_r-=1
                    freq['R']-=1

            if queue[0] == 'D' :
                if killed_d == 0:
                    a = queue.popleft()
                    queue.append(a)
                    killed_r += 1
                else:
                    queue.popleft()
                    killed_d -= 1
                    freq['D']-=1