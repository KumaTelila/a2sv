# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count+=1
        a = count - n
        temp = head
        prev= ListNode()
        while a > 0 and temp:
            prev = temp
            temp = temp.next
            a-=1
        if count == n and head:
            head = head.next
        prev.next = temp.next
        temp.next = None
        return head
        