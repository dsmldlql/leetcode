# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        list_return = list_merged = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                list_merged.next = list1
                list1 = list1.next
            else:
                list_merged.next = list2
                list2 = list2.next
            list_merged = list_merged.next
        list_merged.next = list1 or list2
        return list_return.next
