# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size
    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
def solve():
    n,m,k = lint()
    un = UnionFind(n+1)
    tasks = []
    ans = []
    for _ in range(m):
        u, v = lint()
    for _ in range(k):
        s, u, v = input().split()
        u = int(u)
        v = int(v)
        tasks.append((s, u, v))
    tasks.reverse()
    for s, u, v in tasks:
        if s == 'ask':
            p1 = un.find(u)
            p2 = un.find(v)
            if p1 == p2:
                ans.append("YES")
            else:
                ans.append("NO")
        else:
            un.union(u, v)
    ans.reverse()
    for i in ans:
        print(i)
    # print(tasks)
        
            
    
    # pass
solve()