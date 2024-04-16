# Problem: Merge K Sorted List - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
        dummy = ListNode()
        head = dummy
        while heap:
            idx = heap[0][1]
            node  = lists[idx]
            head.next = node
            head = head.next
            if node.next:
                heapreplace(heap, (node.next.val, idx))
                lists[idx] = node.next
            else:
                heappop(heap)
        return dummy.next
        