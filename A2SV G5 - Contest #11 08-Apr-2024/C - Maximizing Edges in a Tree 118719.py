# Problem: C - Maximizing Edges in a Tree - https://codeforces.com/gym/515998/problem/C

from sys import stdin
from collections import defaultdict
 
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

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def solve():
        m = int(input())
        graph = defaultdict(list)
        end = -1
        color = defaultdict(bool)
        end = -1
        for _ in range(m-1):
            v, e = map(int, input().split())
            end = e
            graph[v].append(e)
            graph[e].append(v)
        def dfs(node):
            if node not in color:
                color[node] = True
            for ele in graph[node]:
                if ele not in color:
                    color[ele] =  not color[node]
                    dfs(ele)
        dfs(end)
        # print(dict(color), dict(graph))
        left = set()
        right = set()
        for i in color:
            if color[i]:
                left.add(i)
            else:
                right.add(i)
        ans = 0
        for i in right:
            ans+=(len(left) - len(graph[i]))
        print(ans)
    solve()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
