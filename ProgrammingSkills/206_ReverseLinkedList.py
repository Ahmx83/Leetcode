# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printlist(l):
    while l:
        print(l.val, " -> ", end="")
        l = l.next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        hold = []
        current = res

        while head:
            hold.append(head)
            head = head.next

        hold.reverse()

        for node in hold:
            current.next = node
            current = current.next
        current.next = None

        return res.next
