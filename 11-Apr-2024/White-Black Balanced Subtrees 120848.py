# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G

import sys, threading
from collections import defaultdict

def main():
    # write your solution here
    input = lambda: sys.stdin.readline().strip()
 
    def lint():
        return list(map(int, input().split()))
    
    def intp():
        return int(input())
        
    def strp():
        return input()
    
    def lstr():
        return list(input().split())
    # divmod(a, 
    from functools import lru_cache

    def solve():
        n = intp()
        a = lint()
        s = input()
        graph = defaultdict(list)
        for i in range(1, n):
            graph[a[i-1]].append(i+1)
        count= 0
        def dfs(node):
            nonlocal count
            if node not in graph:
                w = 0
                b = 0
                if s[node-1] == 'W':
                    w+=1
                else:
                    b+=1
                return (w, b)
            tw = 0
            tb = 0
            for negh in graph[node]:
                # print(negh, dfs(negh))
                cw, cb = dfs(negh)
                if cw == cb and cw != 0:
                    count+=1
                tw += cw
                tb += cb
            
            if s[node-1] == 'W':
                tw+=1
            else:
                tb+=1
            return (tw, tb)
        # print(graph)
        ans = dfs(1)
        if ans[0] == ans[1] and ans[0] != 0:
            count+=1
        print(count)
    for _ in range(intp()):
        solve()
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()