# Definition for singly-linked list.
import cProfile
import pprint


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        current = head
        carry = 0

        while l1 and l2:
            val1 = l1.val
            val2 = l2.val

            added = val1 + val2 + carry
            carry, unit = divmod(added, 10)
            current.next = ListNode(unit)

            current = current.next
            l1 = l1.next
            l2 = l2.next

        l = None
        if l1:
            l = l1
        elif l2:
            l = l2

        if l:
            while l:
                val = l.val

                added = val + carry
                carry, unit = divmod(added, 10)
                current.next = ListNode(unit)

                current = current.next
                l = l.next

        if carry:
            current.next = ListNode(carry)

        return head.next

func = Solution().addTwoNumbers
x = ListNode(2, ListNode(4, ListNode(3)))
y = ListNode(5, ListNode(6, ListNode(4)))

cProfile.run("func(x, y)")
