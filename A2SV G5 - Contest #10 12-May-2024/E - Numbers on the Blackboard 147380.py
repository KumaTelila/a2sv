# Problem: E - Numbers on the Blackboard - https://codeforces.com/gym/514644/problem/E

from sys import stdin
from collections import defaultdict, Counter, deque
import bisect
from math import gcd, lcm
 
 
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
def sol(common, num, k, count = 0):
    if num == common:
        return count
    num-=common
    return sol(common, num + k, k, count+1)
def solve():
    n, k = lint()
    a = lint()
    if len(set(a)) == 1:
        return 0
    for x in a:
        if (x >= k and k >= a[0]) or (x <= k and k <= a[0]):
            return -1
    _gcd = abs(a[0] - k)
    for i in a:
        _gcd = gcd(_gcd, abs(i - k))
    
    ans = 0
    for i in a:
        ans += abs(k - i)//(_gcd) - 1
    return ans
    
for _ in range(intp()):
    print(solve())