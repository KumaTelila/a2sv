# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

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
    return n.bit_count()
print(solve())