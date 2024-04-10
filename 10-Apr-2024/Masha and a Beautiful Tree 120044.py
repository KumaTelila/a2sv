# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    # write your solution here
    def solve():
        n = int(input())
        a = list(map(int, input().split()))
        def merge(left, right):
            mid = left + (right - left)//2
            if left == right:
                return [a[left]]
            left_arr = merge(left, mid)
            right_arr = merge(mid + 1, right)
            return sort(left_arr, right_arr)
        count = 0
        def sort(left_arr, right_arr):
            nonlocal count
            ans = []
            # print(left_arr, right_arr)
            flag = False
            if left_arr and right_arr:
                if left_arr[-1] > right_arr[0]:
                    left_arr, right_arr = right_arr, left_arr
                    flag = not flag
                if flag and left_arr[-1] < right_arr[0]:
                    count+=1
                elif flag and left_arr[-1] > right_arr[0]:
                    return False
                ans.extend(left_arr[:])
                ans.extend(right_arr[:])
            return ans
        ans = merge(0, n-1)
        print(count if ans else -1)
    for _ in range(int(input())):
        solve()    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()