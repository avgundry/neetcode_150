from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1.val < list2.val:
            newlist = ListNode(list1.val)
            list1 = list1.next
        else:
            newList = ListNode(list2.val)
            list2 = list2.next

        head = newList

        while list1 and list2:
            if list1.val < list2.val:
                newlist.next = ListNode(list1.val)
                newlist = newlist.next
                list1 = list1.next
            else:
                newlist.next = ListNode(list2.val)
                newlist = newlist.next
                list2 = list2.next

        while list1:
            newlist.next = ListNode(list1.val)
            newlist = newlist.next

        while list2:
            newlist.next = ListNode(list2.val)
            newlist = newlist.next

        return newlist
        