# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

rom sys import stdin
from heapq import *
 
 
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
    heap = []
    ans = []
    for _ in range(n):
        s = strp()
        new = s.split()
        if new[0] == 'insert':
            heappush(heap, int(new[1]))
            ans.append(s)
        elif new[0] == 'removeMin':
            if heap:
                heappop(heap)
                ans.append(s)
            else:
                # heappush(heap, 0)
                ans.append('insert 0')
                ans.append(s)
        else:
            num = int(new[1])
            while heap and heap[0] < num:
                heappop(heap)
                ans.append('removeMin')
            if heap and num == heap[0]:
                ans.append(s)
            else:
                heappush(heap, num)
                ans.append('insert '+str(num)) 
                ans.append(s) 
    print(len(ans))
    for i in ans:
        print(i)
 
solve()