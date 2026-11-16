class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        count = 1

        while tail.next != None:
            tail = tail.next
            count += 1

        del_pos = count - n + 1

        if del_pos == 1:
            return head.next

        curr = head

        for i in range(1, del_pos - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head