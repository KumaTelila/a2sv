# Problem: A - Flag Checker - https://codeforces.com/gym/515998/problem/A

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
    n, m = lint()
    adj = ''
    for _ in range(n):
        s = set(strp())
        s = list(s)
        if len(s) > 1 or s[0] == adj:
            return False
        adj = s[0]
    return True 
a = solve()
print("YES" if a else "NO")