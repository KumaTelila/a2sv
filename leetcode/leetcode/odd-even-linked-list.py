# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd = head
        even = head.next
        temp = even
        while odd.next and odd.next.next:
            odd.next = temp.next
            odd = temp.next
            temp.next = odd.next
            temp = odd.next
        odd.next = even
        return head


        
        