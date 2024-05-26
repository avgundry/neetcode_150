# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        slow = head

        # want the curr node to be n steps ahead, instead of n - 1, so we can pop easily
        for i in range(n):
            # There are exactly n - 1 nodes, so we want to pop the first one.
            if curr == None:
                return head.next
            curr = curr.next

        if curr == None:
            return head.next
            
        while curr.next != None:
            slow = slow.next
            curr = curr.next

        if slow.next == None:
            return None 
        slow.next = slow.next.next

        return head
        
    