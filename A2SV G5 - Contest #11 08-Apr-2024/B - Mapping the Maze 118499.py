# Problem: B - Mapping the Maze - https://codeforces.com/gym/515998/problem/B

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
def check(graph, node, m):
    ans = "unknown topology"
    l = set()
    for i in graph:
        l.add(len(graph[i]))
    l = list(l)
    l.sort()
    if len(l) == 1 and l[0] == 2:
        return "ring topology"
    if len(l) == 2 and l[0] == 1 and l[1] == 2:
        return "bus topology"
    if len(l) ==  2 and l[0] == 1 and l[1] == m:
        return  "star topology"
    return ans   
def solve():
    n, m = lint()
    graph = defaultdict(list)
    end = -1
    for _ in range(m):
        v, e = lint()
        end = e
        graph[v].append(e)
        graph[e].append(v)
    ans = check(graph, end, m)
    print(ans)
solve()