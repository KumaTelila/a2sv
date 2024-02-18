# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:
        def reverse(head):
            if not head or not head.next:
                return head
            last = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = last
                last = curr
                curr = next_node
            return last

        if not head and not head.next:
            return head
        left= head
        left_prev = None
        right = head
        while l-1 > 0:
            left_prev = left
            left = left.next
            l-=1
        while r-1 > 0:
            right = right.next
            r-=1
        right_next = right.next
        right.next = None
        rv = reverse(left)
        
        rv_last = rv
        while rv_last.next:
            rv_last = rv_last.next
        if left_prev: 
            left_prev.next = rv
        else:
            head = rv
        rv_last.next = right_next

        return head

        

        