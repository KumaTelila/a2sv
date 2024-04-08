# Problem: E - Blocking Paths for Safe Escape - https://codeforces.com/gym/515998/problem/E

import sys, threading
from collections import defaultdict, Counter, deque
import bisect
import math
 
 
input = lambda : sys.stdin.readline().strip()
 
def lint():
    return list(map(int, input().split()))
 
def intp():
    return int(input())
    
def strp():
    return input()
 
def lstr():
    return list(input().split())
# divmod(a, b)




def main():
    def solve():
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(grid, row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        n,m = lint()
        
        grid = []
        for i in range(n):
            s = list(strp())
            grid.append(s)
        #print(grid)
        visited = set()
        def dfs(row, col):
            #print(row, col)
            if not inbound(grid, row, col) or (row, col) in visited:
                return 
            visited.add((row, col))
            if grid[row][col] == '#':
                return 
            else:
                
                if grid[row][col] == '.':
                    grid[row][col] = '#'
                    return
                for x,y in directions:
                    dfs(row+x, col+y)
            
        count_of_good_guys = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'B':
                    dfs(i, j)
                if grid[i][j] == 'G':
                    count_of_good_guys += 1
        visited = set()
        def way_out(row, col):
            nonlocal count_of_good_guys
            if not inbound(grid, row, col):
                return
            if grid[row][col]=='#' or (row, col )in visited:
                return
            visited.add((row, col))
            if grid[row][col] == 'G':   
                count_of_good_guys -= 1
            for x,y in directions:
                way_out(row + x, col + y)
        
        way_out(n-1, m-1)
        if count_of_good_guys:
            print("No")
        else:
            print("Yes")
        pass
    for _ in range(intp()):
        solve()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
