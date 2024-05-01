# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

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
    n, m, k = lint()
    ls = []
    for _ in range(m+1):
        a = intp()
        ls.append(a)
    b = ls[-1]
    ans = 0
    for i in range(m):
        one = b^ls[i]
        ones = one.bit_count()
        if ones <= k:
            ans+=1
    return ans
    
    # pass
print(solve())