# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

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
    a = lint()
    stack = []
    ans = 1
    curr = 1
    for i in range(1, n):
        if a[i]- a[i-1] > 0:
            curr += 1
        else:
            curr = 1
        ans= max(curr, ans)
    
    print(ans)
            
    
solve()