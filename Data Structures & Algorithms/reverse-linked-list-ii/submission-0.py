# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        dummy = ListNode(0)
        dummy.next = head

        before = dummy
        pos = 1

        # Step 1: Reach the node before left
        while pos < left:
            before = before.next
            pos += 1

        # Step 2: Reverse the required portion
        t = before.next
        curr = t
        prev = None

        count = right - left + 1

        while count > 0:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            count -= 1

        # Step 3: Reconnect the linked list
        t.next = curr
        before.next = prev

        return dummy.next
        