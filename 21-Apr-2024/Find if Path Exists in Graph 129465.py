# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        graph = defaultdict(list)
        for u,v in edges:
            graph[v].append(u)
            graph[u].append(v)
        queue = deque([source])
        visited = set([source])
        while queue:
            ele = queue.popleft()
            for negh in graph[ele]:
                if negh == destination:
                    return True
                if negh not in visited:
                    queue.append(negh)
                    visited.add(negh)
        return False