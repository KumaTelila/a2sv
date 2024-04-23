# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        graph = {
            '0': ['9', '1'],
            '1': ['0', '2'], 
            '2': ['1', '3'],
            '3': ['2', '4'],
            '4': ['3', '5'],
            '5': ['4', '6'],
            '6': ['5', '7'],
            '7': ['6', '8'],
            '8': ['7', '9'],
            '9': ['8', '0']
        }
        def generate(s):
            possible = []
            for i in range(4):
                for j in graph[s[i]]:
                    temp = s[:i] + j + s[i+1:]
                    possible.append(temp)
            return possible

        queue = deque(['0000'])
        visited = set()
        for i in deadends:
            visited.add(i)
        count = 0
        if '0000' in visited:
            return -1
        while queue:
            l = len(queue)
            for _ in range(l):
                ele = queue.popleft()
                if ele == target:
                    return count
                pos = generate(ele)
                for negh in pos:
                    if negh not in visited:
                        queue.append(negh)
                        visited.add(negh)
            count+=1
        return -1


        