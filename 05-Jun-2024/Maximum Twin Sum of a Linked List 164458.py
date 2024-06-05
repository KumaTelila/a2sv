# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        l = 0
        temp = head
        while temp:
            temp = temp.next
            l += 1
        mid = l//2
        sm = defaultdict(int)
        temp = head
        count = 0
        while temp:
            if count >= mid:
                sm[l - count - 1] += temp.val
            else:
                sm[count] += temp.val
            temp = temp.next
            count += 1
        return max(sm.values())

        