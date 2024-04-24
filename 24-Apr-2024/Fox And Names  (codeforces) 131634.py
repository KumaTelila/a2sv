# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from sys import stdin
from collections import defaultdict, Counter, deque
import bisect
import math

 
 
input = lambda : stdin.readline().strip()
 
def lint():
    return list(map(int, input().split()))
 
def intp():
    return int(input())
    
def strp():
    return input()
 
def lstr():
    return list(input().split())
# divmod(a, b)
def solve():
    n = intp()
    indegree = defaultdict(int)
    graph = defaultdict(list)
    prev = ''
    for _ in range(n):
        s = strp()
        if prev == '':
            prev = s
        else:
            p1 = 0
            while p1 < len(prev) and p1 < len(s):
                if s[p1] != prev[p1]:
                    graph[prev[p1]].append(s[p1])
                    indegree[s[p1]]+=1
                    break
                p1+=1
                if p1 == len(s) and p1 < len(prev):
                    return "Impossible"
            prev = s
    queue = deque([chr(i) for i in range(ord('a'), ord('z')+1) if indegree[chr(i)] == 0])
    ans = ''
    while queue:
        ele = queue.popleft()
        ans+=ele
        for negh in graph[ele]:
            indegree[negh]-=1
            if indegree[negh] == 0:
                queue.append(negh)
    
    return ans if len(ans) == 26 else "Impossible"
    
print(solve())