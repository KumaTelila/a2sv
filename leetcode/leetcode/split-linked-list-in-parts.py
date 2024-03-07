# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        n = 0
        temp  = head
        while temp:
            n+=1
            temp = temp.next
        div = n//k
        rem = n%k
        prev = temp = head
        for i in range(k):
            if rem > 0:
                div+=1
                rem-=1
            while temp and div > 1:
                temp = temp.next
                div-=1
            div = n//k
            if temp and temp.next:
                curr = temp.next
                temp.next = None
                ans.append(prev)
                prev = curr
                temp = curr
            else:
                ans.append(prev)
                prev = None
        return ans
        