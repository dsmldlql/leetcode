# v1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None):
            return head
        head_step = head.next
        head_return = head
        while head and head_step:
            if head.val != head_step.val:
                head.next = head_step
                head = head.next
            head_step = head_step.next
        if head_step is None:
            head.next = None
        return head_return
