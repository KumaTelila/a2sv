# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

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
        self.min = [i for i in range(size)]
        self.max = [i for i in range(size)]
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
                self.min[rootX] = min(self.min[rootX], self.min[rootY])
                self.max[rootX] = max(self.max[rootX], self.max[rootY])
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]
                self.min[rootY] = min(self.min[rootY], self.min[rootX])
                self.max[rootY] = max(self.max[rootY], self.max[rootX])
def solve():
    n, m = lint()
    un = UnionFind(n+1)
    for _ in range(m):
        s = input().split()
        if s[0] == 'union':
            un.union(int(s[1]), int(s[2]))
        else:
            p = un.find(int(s[1]))
            print(un.min[p], un.max[p], un.size[p])           
    # pass
solve()