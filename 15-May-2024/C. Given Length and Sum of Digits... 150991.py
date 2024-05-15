# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

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
    m, s = lint()
    num = 9*m
    if s > num or s == 0 and m > 1:
        print(-1, -1)
        return
    mn = [1]
    mx = [0]
    for i in range(1, m):
        mn.append(0)
        mx.append(0)
    i = 1
    mns = s-1
    while mns > 9:
        mn[m - i]+=9
        mns -= 9
        i += 1   
    mn[m-i]+=mns
     
    mxs = s
    j = 0
    while mxs > 9:
        mx[j] += 9
        mxs -= 9
        j+=1
    mx[j]+=mxs
    for i in range(m):
        mn[i] = str(mn[i])
        mx[i] = str(mx[i])
     
    print(''.join(mn), ''.join(mx))    
solve()