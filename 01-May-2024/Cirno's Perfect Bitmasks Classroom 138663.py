# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

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
    y = n & -n
    while y & n == 0 or y ^ n == 0:
        y += 1
    return y
    # pass
for _ in range(intp()):
    print(solve())