# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # Step 1: Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Separate the second half
        second = slow.next
        slow.next = None

        # Step 3: Reverse the second half
        curr = second
        prev = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        second = prev

        # Step 4: Merge both halves
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2