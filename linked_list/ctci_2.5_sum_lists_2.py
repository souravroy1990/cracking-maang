"""
LeetCode: https://leetcode.com/problems/add-two-numbers-ii/

Problem: 1200 + 209 = 1409

Time: O(n + m)
Space: O(1)
"""

from linked_list import ListNode
from typing import Optional


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Reverse both lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        # Step 2: Add the numbers
        carry = 0
        dummy = ListNode()
        current = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add the digits and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            # Move to the next digits
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # Step 3: Reverse the result to restore the correct order
        return self.reverseList(dummy.next)
    
c = Solution()
l1 = [7,2,4,3]
l2 = [5,6,4]
print(c.addTwoNumbers(l1, l2))
