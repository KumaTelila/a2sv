# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n = 0
        h1 = headA
        while h1:
            n+=1
            h1 = h1.next
        m = 0
        h2 = headB
        while h2:
            m+=1
            h2 = h2.next
        h1 = headA
        h2 = headB
        while n != m and h1 and h2:
            if n > m:
                h1 = h1.next
                n-=1
            else:
                h2 = h2.next
                m-=1
        while h1 and h2:
            if h1 == h2:
                return h1
            else:
                h1 = h1.next
                h2 = h2.next
        return None
        
        