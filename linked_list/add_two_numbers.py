from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # brute force approach is to just go through both lists, turn them
        # into numbers, add them together, then turn that into another LL.
        if l1.val == 0 and l1.next == None:
            return l2
        elif l2.val == 0 and l2.next == None:
            return l1

        str1 = ""
        str2 = ""

        while l1 != None:
            str1 += str(l1.val)
            l1 = l1.next
        while l2 != None:
            str2 += str(l2.val)
            l2 = l2.next

        total = list(str(int(str1[::-1]) + int(str2[::-1])))
        # print(total)

        
        newhead = ListNode(total.pop(), None)
        curr = newhead
        while total:
            temp = ListNode(total.pop(), None)
            curr.next = temp
            curr = temp
            
        return newhead