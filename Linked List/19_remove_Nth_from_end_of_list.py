# 给定一个链表和非负数n，从链表中移除从末端起的第n个结点，返回链表。
# Input: 1->2->3->4->5, n = 2
# Output: 1->2->3->5

# 思路：
# p,q两个指针，分成除倒n个结点的两段，直接p.next = q。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Solution:
    def removeNthRromEnd(self, head, n):
        p = q = head
        for i in range(n):
            p = p.next
        while p.next:
            p = p.next
            q = q.next
        q.next = p
        return head

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    n = 2

    s = Solution()
    result = s.removeNthRromEnd(head, n)
    ListNode.print(head)