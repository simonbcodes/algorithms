# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    new_l = ListNode(None)
    carry = 0
    while(l1 and l2):
        total = l1.val + l2.val + carry
        new_l.val = total % 10
        carry = total // 10
        l1 = l1.next
        l2 = l2.next
    while l1:
        total = l1.val + carry
        new_l.val = total % 10
        carry = total // 10
        l1 = l1.next
    while l2:
        total = l2.val + carry
        new_l.val = total % 10
        carry = total // 10
        l2 = l2.next
    return new_l


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
