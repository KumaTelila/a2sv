# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sort_list(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val <= list2.val:
                list1.next = sort_list(list1.next, list2)
                return list1
            else:
                list2.next = sort_list(list1, list2.next)
                return list2
        def divide(node):
            if node:
                if not node.next:
                    return node
                slow = node
                fast = node
                while fast and fast.next and fast.next.next:
                    slow = slow.next
                    fast = fast.next.next
                right_node = slow.next
                slow.next = None
                left = divide(node)
                right = divide(right_node)
                return sort_list(left, right) 
        return divide(head)

                
        
        
        