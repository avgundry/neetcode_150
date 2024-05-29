from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or k == 1:
            return head

        
        curr = head
        prev = None
        i = 0
        while curr != None:
            if i % k == 0:
                # The tail of the previous now-reversed sublist is saved
                # so that it can point to the head of the next sublist correctly
                nxt = curr.next
                temp = self.reverseK(prev, curr, k)
                if i == 0:
                    ret = temp[0]
                prev.next = temp[0]
                prev = temp[1]
                prev.next = nxt

            curr = curr.next

            i += 1
            

        return ret 

        
    # Reverses the sublist consisting of head and the next k - 1 nodes
    # Returns the new head and tail of the sublist.
    def reverseK(self, prev: Optional[ListNode], head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # get the tail first in order to reverse
        curr = head
        # Move forward k - 1 nodes.
        for i in range(k - 1):
            # If we ever reach the end, the sublist is < k elements, so we return
            # it completely unchanged.
            if curr.next == None:
                return head
            curr = curr.next

        # Curr will be at the tail end of the sublist now.
        # Store the value the end of our list will point to.
        # temp = curr.next

        newhead = curr
        prv = None
        curr = head
        nxt = curr.next

        # while we aren't past the original tail of the sublist
        while curr != newhead.next:
            # reverse the list
            curr.next = prv
            prv = curr
            curr = nxt
            nxt = curr.next

        return [newhead, head]
            

