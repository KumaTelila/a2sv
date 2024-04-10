# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for i in redEdges:
            red[i[0]].append(i[1])
        for i in blueEdges:
            blue[i[0]].append(i[1])
        visitedRed,  visitedBlue = set(), set()
        ans = [-1]*n
        queue = deque([(0, 0, '')])
        visitedRed.add(0)
        visitedBlue.add(0)
        ans[0] = 0
        while queue:
            u, d, c = queue.popleft()
            if c == '' or c == 'b':
                for v in red[u]:
                    if v not in visitedRed:
                        ans[v] = d + 1 if ans[v] == -1 else min(ans[v], d + 1)
                        queue.append((v, d+1, 'r'))
                        visitedRed.add(v)
            if c == '' or c == 'r':
                for v in blue[u]:
                    if v not in visitedBlue:
                        ans[v] = d + 1 if ans[v] == -1 else min(ans[v], d + 1)
                        queue.append((v, d+1, 'b'))
                        visitedBlue.add(v)

        return ans


        
        