from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = 0
        curr = head
        while curr != None:
            n += 1
            curr = curr.next

        # Split the lists into halves.
        prev = None
        mid = head
        mid_count = 0
        while mid_count < n / 2:
            prev = mid
            mid = mid.next
            mid_count += 1

        curr = head 
        prev.next = None

        # Reverse the right half of the list...
        prev = None
        while mid != None:
            # print(f"nxt: {mid.next}")
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt
            # print(f"prev: {prev}")

        # print(head)
        # print(prev)

        # Then interlink the nodes together.
        while curr != None and prev != None:
            temp_left = curr.next
            temp_right = prev.next
            curr.next = prev
            prev.next = temp_left
            curr = temp_left
            prev = temp_right

        return head

        