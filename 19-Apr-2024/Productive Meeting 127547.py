# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

from sys import stdin
from collections import defaultdict, Counter, deque
import bisect
import math
from heapq import *
 
 
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
    n =  intp()
    a = lint()
    heap = []
    for i in range(n):
        if a[i] != 0:
            heappush(heap, (-a[i], i+1))
    count = 0
    ans = []
    while heap:
        if len(heap) == 1:
            break
        first, ind1 = heappop(heap)
        second, ind2  = heappop(heap)
        diff = second - first
        if -first > 0 and -second > 0:
            ans.append([ind2, ind1])
            heappush(heap, (first+1, ind1))
            heappush(heap, (second+1, ind2))
            
    print(len(ans))
    for i in ans:
        print(*i)
for _ in range(intp()):
    solve()