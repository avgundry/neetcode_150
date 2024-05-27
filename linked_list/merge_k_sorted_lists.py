import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # set up a min-heap to pop from.
        heap = []
        for lst in lists:
            if lst != None:
                heapq.heappush(heap, (lst.val, id(lst), lst))

        if len(heap) == 0:
            return None

        x = heapq.heappop(heap)
        head = ListNode(x[0], None)
        if x[2].next != None:
            heapq.heappush(heap, (x[2].next.val, id(x[2].next), x[2].next))


        curr = head
        while heap:
            temp = heapq.heappop(heap)
            if temp[2].next != None:
                heapq.heappush(heap, (temp[2].next.val, id(temp[2]), temp[2].next))
            curr.next = ListNode(temp[0], None)
            curr = curr.next

        return head
        