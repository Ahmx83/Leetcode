import cProfile

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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1 = []
        while l1:
            list1.append(str(l1.val))
            l1 = l1.next

        list2 = []
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next

        num1 = int(''.join(list1))
        num2 = int(''.join(list2))

        total = str(num1 + num2)

        head = ListNode()
        current = head
        for i in range(len(total)-1):
            n = total[i]
            current.val = int(n)
            current.next = ListNode()
            current = current.next
        current.val = int(total[-1])

        return head


func = Solution().addTwoNumbers
x = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
y = ListNode(5, ListNode(6, ListNode(4)))
func(x, y)
# cProfile.run("func(x, y)")