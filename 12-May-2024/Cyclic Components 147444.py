# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

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
    n, m = lint()
    un = UnionFind(n+1)
    graph = defaultdict(list)
    degrees = defaultdict(int)
    for _ in range(m):
        u , v = lint()
        graph[u].append(v)
        graph[v].append(u)
        degrees[u]+=1
        degrees[v]+=1
        un.union(u, v)
    parents = defaultdict(list)
    for i in range(1, n+1):
        if i in graph:
            p = un.find(i)
            parents[p].append(i)
    ans = 0
    for childs in parents:
        flag = True
        for i in parents[childs]:
            if degrees[i] != 2:
                flag = False
                break
        if flag:
            ans+=1
            
    print(ans)
        
    
solve()