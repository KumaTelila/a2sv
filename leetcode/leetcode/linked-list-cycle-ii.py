# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        found = False
        if not head:
            return None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                found = True
                break
        if found:
            temp = head
            while temp:
                if temp == slow:
                    return temp
                temp = temp.next
                slow= slow.next
        return None

        