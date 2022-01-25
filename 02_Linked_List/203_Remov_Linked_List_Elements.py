# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        dummy_head = ListNode(next = head)
        init = dummy_head

        while init.next != None:
            if init.next.val == val: init.next = init.next.next
            else: init = init.next

        return dummy_head.next

