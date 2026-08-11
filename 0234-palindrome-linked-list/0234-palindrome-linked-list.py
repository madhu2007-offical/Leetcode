class Solution:
    def isPalindrome(self, head):
        def reverseList(node):
            prev = None
            curr = node

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            return prev

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        second_half = reverseList(slow)

        while second_half:
            if head.val != second_half.val:
                return False

            head = head.next
            second_half = second_half.next

        return True