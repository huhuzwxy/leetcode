# 给定一个链表和非负数k，从k位置处旋转该链表。
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:  rotate 1 steps to the right: 5->1->2->3->4->NULL
#               rotate 2 steps to the right: 4->5->1->2->3->NULL

# 思路：
# 递归，用k控制递归次数。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print(self):
        while self:
            print(self.val)
            self = self.next

class Solution:
    def rotateRight(self, head, k):
        m = n = head
        for i in range(k):
            head = self.rotate(head)
        return head

    def rotate(self, head):
        p = q = head
        while q.next.next:
            q = q.next
        p = q.next
        tmp = p
        q.next = None
        tmp.next = head
        return tmp

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    k = 2

    s = Solution()
    result = s.rotateRight(head, k)
    ListNode.print(result)


