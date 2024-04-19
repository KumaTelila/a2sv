# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0 for i in range(len(nums))]
        def divide(left, right):
            if left == right:
                return [[nums[left], left, 0]]
            mid = left + (right - left)//2
            left_divide = divide(left, mid)
            right_divide = divide(mid+1, right)
            return merge(left_divide, right_divide)
        def check(left, right):
            # print(left, right)
            for i in range(len(left)):
                for j in range(len(right)):
                    if left[i][0] > right[j][0]:
                        # print("->", left[i], right[j])
                        count[left[i][1]]+=1
                    else:
                        break
        def merge(left_divide, right_divide):
            l = 0
            r = 0
            ans = [] 
            # print(left_divide, right_divide, left_divide[0][2])
            right_ele = [i[0] for i in right_divide]
            for i in range(len(left_divide)):
                left_divide[i][2] += bisect_left(right_ele,left_divide[i][0])
            # check(left_divide, right_divide)
            while l < len(left_divide) and r < len(right_divide):
                if left_divide[l] <= right_divide[r]:
                    ans.append(left_divide[l])
                    l+=1
                else:
                    ans.append(right_divide[r])
                    # count[left_divide[l][1]]+=1
                    r+=1
            ans.extend(left_divide[l:])
            ans.extend(right_divide[r:])
            return ans
        # print(count)
        ans = divide(0, len(nums)-1)
        for i in ans:
            count[i[1]] = i[2]
        return count



        