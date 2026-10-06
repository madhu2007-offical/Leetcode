class Solution:
    def deleteMiddle(self, head):
        if head.next is None:
            return None

        # Find length
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        # Middle index = n // 2
        middle = n // 2

        # Move to node before middle
        curr = head

        for _ in range(middle - 1):
            curr = curr.next

        # Delete middle node
        curr.next = curr.next.next

        return head