# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        start = dummy

        while True:

            # Step 1: Find the kth node
            kth = start

            for i in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            # Step 2: Store the next group and current group's first node
            new_start = kth.next
            group_start = start.next

            # Step 3: Reverse the current group
            curr = start.next
            prev = new_start

            while curr != new_start:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex

            # Step 4: Reconnect the reversed group
            start.next = prev

            # Step 5: Move start to the next group's previous node
            start = group_start
        