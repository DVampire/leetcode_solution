# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        p = dummy
        carry = 0
        while l1 or l2:
            tmp = 0
            # 注意考虑l1和l2长度不一致
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            tmp += carry

            cur_node = ListNode(tmp % 10)
            carry = tmp // 10

            p.next = cur_node
            p = p.next

        # 注意考虑进位不为0
        if carry:
            p.next = ListNode(carry)

        return dummy.next

