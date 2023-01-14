# v1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            head.val = 'a'
            head = head.next
            if not head:
                return False
            elif head.val == 'a':
                return True
