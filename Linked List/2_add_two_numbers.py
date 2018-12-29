# 两个非空链表代表两个非负整数，数字逆序存储在每个结点，返回相加的链表
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807

# 思路：
# a + b >= 10，写个进位出来。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Linklist:
    def __init__(self):
        self.head = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        result = head
        carry = 0
        if not l1 and not l2:
            return False
        while l1 and l2:
            sum = l1.val + l2.val + carry
            if sum >= 10:
                head.next = ListNode(0)
                carry = 1
            else:
                head.next = ListNode(sum)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        return result.next

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    ListNode.print(result)


